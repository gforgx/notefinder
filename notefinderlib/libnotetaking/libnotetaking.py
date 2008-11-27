#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2007-2008 Simonenko Sergey <gforgx@lavabit.com>
#
#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#
#       * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following disclaimer
#       in the documentation and/or other materials provided with the
#       distribution.
#       * Neither the name of the project NoteFinder and author's name nor the names of 
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#      "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Standard library imports
import os
import ConfigParser

# Backend imports
from notefinderlib.libnotetaking.backends.dokuwiki import DokuWiki
from notefinderlib.libnotetaking.backends.files import Files
from notefinderlib.libnotetaking.backends.filesystem import FileSystem
from notefinderlib.libnotetaking.backends.ical import iCal
from notefinderlib.libnotetaking.backends.ipod import iPod
from notefinderlib.libnotetaking.backends.mail import Mail
from notefinderlib.libnotetaking.backends.rss import RSS
from notefinderlib.libnotetaking.backends.wixi import Wixi
from notefinderlib.libnotetaking.backends.zim import Zim

# Backends dictionary
backends = {
    'FileSystem':FileSystem,
    'Files':Files,
    'iCal':iCal,
    'iPod':iPod,
    'DokuWiki':DokuWiki,
    'RSS':RSS,
    'Mail':Mail,
    'Zim':Zim,
    'Wixi':Wixi
    }

class Config(ConfigParser.ConfigParser):
    def __init__(self):
        ConfigParser.ConfigParser.__init__(self)
        
        # Makes option names case-sensitive
        self.optionxform = str
        
        self.file = os.path.expanduser('~/.config/notefinder/notefinder.ini')
        confDir = os.path.expanduser('~/.config')
        if not os.path.exists(confDir):
            os.mkdir(confDir)
        if not os.path.exists(os.path.join(confDir, 'notefinder')):
            os.mkdir(os.path.join(confDir, 'notefinder'))
        if os.path.exists(self.file):
            self.read(self.file)
    
    def addNotebook(self, name, backend, markup, settings):
        if not self.has_section('Notebooks'):
            self.add_section('Notebooks')
        self.set('Notebooks', name, backend)

        if not self.has_section(backend):
            self.add_section(backend)
        self.set(backend, name, ';'.join(settings))

        if not self.has_section('Markup'):
            self.add_section('Markup')
        self.set('Markup', name, markup)

        self.write(open(self.file, 'w'))
        
    def deleteNotebook(self, name):
        self.remove_option('Notebooks', name)
        self.remove_option(self.getBackend(name), name)
        self.remove_option('Markup', name)

        self.write(open(self.file, 'w'))
    
    def setDefault(self, name):
        if not self.has_section('General'):
            self.add_section('General')
        self.set('General', 'Notebook', name)

        self.write(open(self.file, 'w'))

    def getNotebook(self):
        if self.has_option('General', 'Notebook'):
            return self.get('General', 'Notebook')

    def getNotebooks(self):
        if self.has_section('Notebooks'):
            return self.options('Notebooks')

    def getBackend(self, name):
        if self.has_option('Notebooks', name):
            return self.get('Notebooks', name)
 
# Initializing configuration parser
config = Config()

class Notebook(object):
    def __init__(self, name):
        self.name = name

        # Selects backend from dictionary above
        try:
            self.backend = backends[config.getBackend(self.name)](config, self.name)
        except KeyError:
            raise Exception("Notebook doesn't exist")

        self.markup = config.get('Markup', self.name)

        self.Wiki = (self.markup == 'Wiki')

    def getNotes(self):
        return self.backend.getNotes()

    def getNotesNumber(self):
        return len(self.getNotes())

    def getDates(self):
        return self.backend.getDates()

    def getTags(self):
        tags = self.backend.getTags()
        tags.sort()
        return tags

    def getTagsNumber(self):
        return len(self.getTags())

    def getNotesByDate(self, date):
        return self.backend.getNotesByDate(date)
    
    def getNotesByTag(self, tag):
        return self.backend.getNotesByTag(tag)
    
    def getNotesByText(self, text):
        return [note for note in self.getNotes() if Note(note, self).matches(text)]

    def search(self, items):
        results = []

        # Processing search items
        for item in items:

            try:
                # Trying to split item into parameter, keyword pair
                parameter, keyword = item.split(':')

                # Checking date
                if parameter == 'date': notes = self.getNotesByDate(keyword)

                # Checking year
                elif parameter == 'year':
                    notes = []
                    for date in self.getDates():
                        if date.split('-')[0] == keyword: notes.extend(self.getNotesByDate(date))

                # Checking month
                elif parameter == 'month':
                    notes = []
                    for date in self.getDates():
                        if date.split('-')[1] == keyword: notes.extend(self.getNotesByDate(date))

                # Checking day
                elif parameter == 'day':
                    notes = []
                    for date in self.getDates():
                        if date.split('-')[2] == keyword:  notes.extend(self.getNotesByDate(date))

                # Checking tag
                elif parameter == 'tag': notes = self.getNotesByTag(keyword)

                # Checking text
                elif parameter == 'text': notes = self.getNotesByText(keyword)

                # Checking title
                elif parameter == 'title':
                    notes = [i for i in [keyword] if self.backend.noteExists(keyword)]

                else:  notes = []

            except ValueError:

                notes = self.getNotesByDate(item) + self.getNotesByTag(item) + self.getNotesByText(item)
                if self.backend.noteExists(item):
                    if item not in notes: notes.append(item)

            results.append(notes)
    
        intersection = lambda list: set(list[0]) if len(list) == 1 else set(list[0]).intersection(intersection(list[1::]))

        return list(intersection(results))
    
    def addTag(self, tag):
        self.backend.createTag(tag)
    
    def deleteTag(self, tag):
        self.backend.removeTag(tag)

    def error(self, text):
        raise NotebookError(text)

class Note(object):
    """ Note class """
    def __init__(self, name, notebook):
        self.name = name
        
        # Entry notebook, used for backend interaction
        self.notebook = notebook

    def exists(self):
        return self.notebook.backend.noteExists(self.name)

    def getDate(self):
        return self.notebook.backend.getNoteDate(self.name)

    def getTags(self):
        return self.notebook.backend.getNoteTags(self.name)

    def getText(self):
        return self.notebook.backend.getText(self.name)
    
    def matches(self, expression):
        return (expression in self.getText())

    def getBacklinks(self):
        return [note for note in self.notebook.getNotes()
            if Note(note, self.notebook).matches('[[%s' % (self.name))]

    def getURL(self):
        return self.notebook.backend.getURL(self.name)

    def findRelated(self):
        notes = []
        for tag in self.getTags():
            for note in self.notebook.getNotesByTag(tag):
                if not note in notes:
                    notes.append(note)
        return notes

    def getLength(self):
        return len(self.getText())

    def write(self, text):
        self.notebook.backend.write(self.name, text)

    def tag(self, tags):
        self.notebook.backend.tag(self.name, tags)

    def copyToNotebook(self, notebooks, move=False):
        for nb in notebooks:
            Note(self.name, Notebook(nb)).write(self.getText())
        if move:
            self.delete()
         
    def import_(self, file):
        self.write(open(file).read())

    def delete(self):
        self.notebook.backend.deleteNote(self.name)

    def rename(self, name):
        note = Note(name, self.notebook)
        note.write(self.getText())
        note.tag(self.getTags())
        self.delete()
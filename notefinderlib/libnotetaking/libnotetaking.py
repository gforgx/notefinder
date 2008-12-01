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
import re

from backend import *
from config import *

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

    def add(self, note, text):
        self.backend.write(note, text)

    def tag(self, note, tags):
        self.backend.tag(note, tags)

    def delete(self, note):
        return self.backend.deleteNote(note)

    def rename(self, note, new):
        self.add(new, self.get(note))
        self.tag(new, self.noteTags(note))
        self.delete(note)

    def copy(self, note, notebooks, move=False):
        for i in notebooks:
            Notebook(i).add(self.get(note))

        if move:
            self.delete(note)

    def get(self, note):
        return self.backend.getText(note)

    def noteDate(self, note):
        return self.backend.getNoteDate(note)

    def noteTags(self, note):
        return self.backend.getNoteTags(note)

    def url(self, note):
        return self.notebook.backend.getURL(note)

    def backlinks(self, note):
        return [i for i in self.notes() if re.compile(r'^.*\[\[%s(\|.*)?\]\].*$' % (note), re.DOTALL).match(self.get(i))]

    def related(self, note):
        notes = []

        for tag in self.noteTags(note):
            for note in self.byTag(tag):
                if not note in notes:
                    notes.append(note)

        return notes

    def notes(self):
        return self.backend.getNotes()

    def dates(self):
        return self.backend.getDates()

    def tags(self):
        return self.backend.getTags()

    def has(self, note):
        return self.backend.noteExists(note)

    def byDate(self, date):
        return self.backend.getNotesByDate(date)
    
    def byTag(self, tag):
        return self.backend.getNotesByTag(tag)
    
    def byText(self, t):
        return [i for i in self.notes() if re.compile('^.*%s.*$' % (self.get(i)), re.DOTALL, re.IGNORECASE).match(t)]

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
    
        isection = lambda list: set(list[0]) if len(list) == 1 else set(list[0]).isection(isection(list[1::]))

        return list(isection(results))
    
    def addTag(self, tag):
        self.backend.createTag(tag)
    
    def deleteTag(self, tag):
        self.backend.removeTag(tag)
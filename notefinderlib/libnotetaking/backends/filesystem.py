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

import os
from time import localtime

class FileSystem(object):
    """ Backend for storing entries on file system """
    
    desc = 'Backend for storing entries on file system'
    
    ### SETTINGS DESCRIPTION ###
    path = True
    url = False
    login = False
    passwd = False
    
    ### FEATURE SET ###
    Date = True
    Tag = True
    ReadOnly = False
    URL = True
    
    def __init__(self, config, notebook):
        self.name = 'FileSystem'
        self.notebook = notebook

        # Configuration
        path = config.get(self.name, self.notebook)
        
        # Creating root directory if not exists
        if not os.path.exists(path):
            os.mkdir(path)

        # Subdirectories
        self.path, self.tagPath = os.path.join(path, 'date'), os.path.join(path, 'tag')

        # Creating subdirectories (date, tag) if not exist
        for i in (self.path, self.tagPath):
            if not os.path.exists(os.path.join(path, i)):
                os.makedirs(os.path.join(path, i))

    def _today(self):
        return '%d-%d-%d' % localtime()[:3]

    def _getPath(self, entry):
        for date in self.getDates():
            if entry in self.getNotesByDate(date):
                path = os.path.join(self.path, date, entry)
                return path

    def getDates(self):
        return os.listdir(self.path)

    def getTags(self):
        return os.listdir(self.tagPath)

    def getURL(self, entry):
        return 'file://' + self._getPath(entry)
        
    def getNotes(self):
        notes = []

        for i in self.getDates():
            notes.extend(os.listdir(os.path.join(self.path, i)))

        return notes

    def getNotesByDate(self, date):
        if date in self.getDates():
            return os.listdir(os.path.join(self.path, date))
        else:
            return []

    def getNotesByTag(self, tag):
        if tag in self.getTags():
            return os.listdir(os.path.join(self.tagPath, tag))
        else:
            return []

    def getText(self, entry):
       return ''.join(open(self._getPath(entry)).readlines())

    def getNoteDate(self, entry):
        return os.path.split(os.path.split(self._getPath(entry))[0])[1]

    def getNoteTags(self, entry):
        return [tag for tag in self.getTags() if entry in self.getNotesByTag(tag)]

    def noteExists(self, entry):
        return (entry in self.getNotes())

    def createDate(self, date):
        if not date in self.getDates():
            os.mkdir(os.path.join(self.path, date))

    def createTag(self, tag):
        if not tag in self.getTags():
            os.mkdir(os.path.join(self.tagPath, tag))

    def removeDate(self, date):
        if date in self.getDates() and len(self.getNotesByDate(date)) == 0:
            os.rmdir(os.path.join(self.path, date))

    def removeTag(self, tag):
        if tag in self.getTags():

            for i in self.getNotesByTag(tag):
                os.remove(os.path.join(self.tagPath, tag, i))

            os.rmdir(os.path.join(self.tagPath, tag))

    def deleteNote(self, entry):
        if self.noteExists(entry):
            date = self.getNoteDate(entry)

            for tag in self.getNoteTags(entry):
                os.remove(os.path.join(self.tagPath, tag, entry))

                if len(self.getNotesByTag(tag)) == 0:
                    self.removeTag(tag)

            os.remove(self._getPath(entry))
            self.removeDate(date)

    def write(self, entry, text):
        if not self.noteExists(entry):
            date = self._today()
            self.createDate(date)
            open(os.path.join(self.path, date, entry), 'w').write(text)

        else:
            open(self._getPath(entry), 'w').write(text)

    def tag(self, entry, tags):
        src = self.getNoteTags(entry)

        for tag in tags:
            if tag not in src:
                self.createTag(tag)

                try:
                    os.symlink(os.path.join('../../date', self.getNoteDate(entry), entry),
                        os.path.join(self.tagPath, tag, entry))
    
                except AttributeError:
                    open(os.path.join(self.tagPath, tag, entry), 'w')

        for tag in src:
            if tag not in tags:
                os.remove(os.path.join(self.tagPath, tag, entry))
                self.removeTag(tag)
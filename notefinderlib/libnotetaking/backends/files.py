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

class Files(object):
    """ Backend for storing entries as non-organized files """

    desc = 'Backend for storing entries as non-organized files'
    
    ### SETTINGS DESCRIPTION ###
    path = True
    url = False
    login = False
    passwd = False

    ### FEATURE SET ###
    Tag = False
    ReadOnly = False
    URL = True

    def __init__(self, config, notebook):
        self.name = 'Files'
        self.notebook = notebook

        self.path = config.get(self.name, self.notebook)

        # Raising exception if path is wrong
        if not os.path.exists(self.path):
            raise Exception("Directory doesn't exist")
        
        if not os.path.isdir(self.path):
            raise Exception("Specified path isn't a directory")

    def getNotes(self):
        return os.listdir(self.path)
    
    def getDates(self):
        return []

    def getTags(self):
        return []

    def getURL(self, entry):
        return 'file://' + os.path.join(self.path, entry)

    def getNotesByDate(self, date):
        return []
    
    def getNotesByTag(self, tag):
        return []
    
    def getText(self, entry):
        return open(os.path.join(self.path, entry)).read()
    
    def getNoteDate(self, entry):
        return ''

    def getNoteTags(self, entry):
        return []
    
    def noteExists(self, entry):
        return (entry in self.getNotes())
    
    def write(self, entry, text):
        open(os.path.join(self.path, entry), 'w').write(text)

    def tag(self, entry, tags):
        pass

    def deleteNote(self, entry):
        os.remove(os.path.join(self.path, entry))
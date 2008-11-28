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

from xmlrpclib import ServerProxy
from urllib import urlencode, urlopen

class DokuWiki(ServerProxy):
    """ Backend for storing entries in DokuWiki """

    desc = 'Backend for storing entries in DokuWiki'
    
    ### SETTINGS DESCRIPTION ###
    path = False
    url = True
    login = True
    passwd = True

    ### FEATURE SET ###
    Date = False
    Tag = False
    ReadOnly = False
    URL = True

    def __init__(self, config, notebook):
        self.name = 'DokuWiki'
        self.notebook = notebook
        
        # Configuration
        self.url, username, pwd = config.get(self.name, self.notebook).split(';')
        ServerProxy.__init__(self, self.url + '/lib/exe/xmlrpc.php?' + urlencode({'u':username, 'p':pwd}))
        
    def getDates(self):
        return []

    def getTags(self):
        return []

    def getURL(self, entry):
        return self.url + '/doku.php?id=%s' % (entry)

    def getNotesByDate(self, date):
        return []
    
    def getNotesByTag(self, tag):
        return []

    def getNotes(self):
        return [i['id'].encode('utf8').replace('_', ' ') for i in self.wiki.getAllPages()]

    def getText(self, entry):
       """ Opens file for reading and returns text """
       return self.wiki.getPage(entry).encode('utf8')

    def getNoteDate(self, entry):
        return ''

    def getNoteTags(self, entry):
        return []

    def noteExists(self, entry):
        return not self.getText(entry) == ''

    def write(self, entry, text):
        self.wiki.putPage(entry, text, {})

    def tag(self, entry, tags):
        pass

    def deleteNote(self, entry):
        self.wiki.putPage(entry, '', {})
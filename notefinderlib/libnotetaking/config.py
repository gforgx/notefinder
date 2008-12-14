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
import ConfigParser

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
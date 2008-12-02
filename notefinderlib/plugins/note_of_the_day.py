#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2007-2008 Simonenko Sergey <gforgx@gmail.com>
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

from time import localtime

from PyQt4 import Qt

from notefinderlib.libnotetaking import *
from notefinderlib.notefinder import plugin, notefinder_rc

class NoteOfTheDay(plugin.Plugin):
    
    name = 'NoteOfTheDay'
    
    def __init__(self, parent):
        plugin.Plugin.__init__(self, parent)
        self.setText('Note of the day')
        self.setToolTip('Open note of the day')
        self.setIcon(Qt.QIcon(':/icons/%s/date.png' % (self.app.settings['String']['Icons'])))
        self.addToTray()
        
    def onLoad(self):
        note = '%d-%d-%d' % localtime()[:3]
        if not self.app.notebook.has(note):
            self.app.notebook.add(note, '**Notes and thoughts for %s**\n----' % ('%d-%d-%d' % localtime()[:3]))
            self.emit(Qt.SIGNAL('done()'))
    
    def do(self):
        self.onLoad()
        self.app.openNote('%d-%d-%d' % localtime()[:3])
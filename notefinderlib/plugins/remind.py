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

import os

from PyQt4 import Qt

from notefinderlib.libnotetaking import *
from notefinderlib.notefinder import plugin, notefinder_rc

# You can change some settings here
dialog = 'kdialog'
wtitle = '--title'
wmsg = '--msgbox'

class Remind(plugin.Plugin):
    
    name = 'Remind'
    
    def __init__(self, parent):
        plugin.Plugin.__init__(self, parent)
        self.setText('Remind')
        self.setToolTip('Add reminder')
        self.setIcon(Qt.QIcon(':/icons/%s/calendar.png' % (self.app.settings['String']['Icons'])))
        self.addToTray()

        self.dialog = Qt.QDialog()
        self.dialog.setWindowModality(Qt.Qt.ApplicationModal)
        self.dialog.setWindowIcon(self.icon())
        self.dialog.setWindowTitle(self.toolTip())
        self.layout = Qt.QVBoxLayout(self.dialog)
        self.label = Qt.QLabel('Enter reminder date in any human-readable format like\n "12:30", "11pm", "11:00 next week" or "11:00 tomorrow"')
        self.timeEdit = Qt.QLineEdit()
        self.buttonBox = Qt.QDialogButtonBox()
        self.buttonBox.setStandardButtons(Qt.QDialogButtonBox.Cancel|Qt.QDialogButtonBox.Ok)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.timeEdit)
        self.layout.addWidget(self.buttonBox)
        
        self.connect(self.buttonBox, Qt.SIGNAL('rejected()'), self.dialog.close)
        self.connect(self.buttonBox, Qt.SIGNAL('accepted()'), self.add)

    def do(self):
        self.dialog.show()

    def add(self):
        if len(self.app.selectedNotes()) == 1:
            title = self.app.currentNote()
            text = self.app.notebook.get(title)
            time = str(self.timeEdit.text().toUtf8())
            os.system('echo "DISPLAY=:0 %s %s \'%s\' %s \'%s\'" | at %s' % (dialog, wtitle, title, wmsg, text, time))
            self.dialog.close()
        else:
            self.showMessage('You should select one entry')
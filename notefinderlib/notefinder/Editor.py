#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2008 GFORGX <gforgx@gmail.com>
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
#       * Neither the name of the  nor the names of its
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

from PyQt4 import Qt

from notefinderlib.libnotetaking import *
from notefinderlib.creoleparser import text2html

from notefinderlib.notefinder.EditorWidget import Ui_Form

from notefinderlib.notefinder import notefinder_rc

class EditorWidget(Qt.QWidget):
    def __init__(self, app):
        Qt.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.app = app
        
        self.ui.autoTagButton.setIcon(Qt.QIcon(':/icons/%s/tag.png' % (self.app.settings['String']['Icons'])))
        self.ui.addTagButton.setIcon(Qt.QIcon(':/icons/%s/add.png' % (self.app.settings['String']['Icons'])))
        self.ui.delTagButton.setIcon(Qt.QIcon(':/icons/%s/delete.png' % (self.app.settings['String']['Icons'])))

        self.connect(self.ui.addTagButton, Qt.SIGNAL('clicked()'), self.addTag)
        self.connect(self.ui.tagEdit.lineEdit(), Qt.SIGNAL('returnPressed()'), self.addTag)
        self.connect(self.ui.tagsList, Qt.SIGNAL('itemDoubleClicked(QListWidgetItem *)'), self.editTag)
        self.connect(self.ui.delTagButton, Qt.SIGNAL('clicked()'), self.deleteTag)
        
        self.connect(self.ui.textEdit, Qt.SIGNAL('textChanged()'), self.update)
        
        self.connect(self.ui.textBrowser, Qt.SIGNAL('anchorClicked(const QUrl)'), self.openUrl)
        
        self.connect(self.ui.findButton, Qt.SIGNAL('clicked()'), self.find)
        self.connect(self.ui.searchEdit, Qt.SIGNAL('returnPressed()'), self.find)

        self.refresh()

    def refresh(self):
        self.ui.tagEdit.clear()

        for tag in self.app.notebook.tags():
            self.ui.tagEdit.addItem(unicode(tag, 'utf'))

        self.ui.tagEdit.setEditText('')

    def addTag(self, line=None):
        if line is None:
            line = str(self.ui.tagEdit.currentText().toUtf8())

        if not line == '' and not line in self.tags():
            notes = self.app.notebook.byTag(line)
            
            Qt.QListWidgetItem(Qt.QIcon(':/icons/%s/tag.png' \
                % (self.app.settings['String']['Icons'])), unicode(line, 'utf'), self.ui.tagsList).setToolTip(self.trUtf8('Notes (%i): %s' % (len(notes), ', '.join(notes))))
    
            self.ui.tagEdit.lineEdit().clear()

    def deleteTag(self):
        self.ui.tagsList.takeItem(self.ui.tagsList.currentRow())

    def editTag(self):
        self.ui.tagsList.openPersistentEditor(self.ui.tagsList.currentRow())

    def tags(self):
        return [str(self.ui.tagsList.item(i).text().toUtf8()) for i in xrange(self.ui.tagsList.count())]

    def openUrl(self, url):
        if str(url.scheme().toUtf8()) != "":
            Qt.QDesktopServices().openUrl(url)
        else:
            if self.app.notebook.has(str(url.path().toUtf8())):
                self.app.openNote(str(url.path().toUtf8()))
            else:
                self.app.new(str(url.path().toUtf8()))

    def find(self, text=None):
        if text is None:
            text = self.ui.searchEdit.text()

        self.ui.textBrowser.find(text)
        self.ui.textEdit.find(text)

    def update(self):
        self.ui.textBrowser.setHtml(unicode(self.app.markup.html(str(self.ui.textEdit.toPlainText().toUtf8())), 'utf'))
        if self.app.settings['Bool']['AutoSave']:
            self.app.saveNote()
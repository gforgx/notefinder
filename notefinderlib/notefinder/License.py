# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI/license.ui'
#
# Created: Tue Oct 14 20:17:54 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LicenseDialog(object):
    def setupUi(self, LicenseDialog):
        LicenseDialog.setObjectName("LicenseDialog")
        LicenseDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        LicenseDialog.resize(495, 444)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LicenseDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(LicenseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(LicenseDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 473, 382))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.license = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.license.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.license.setObjectName("license")
        self.gridLayout.addWidget(self.license, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(LicenseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LicenseDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LicenseDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LicenseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LicenseDialog)

    def retranslateUi(self, LicenseDialog):
        LicenseDialog.setWindowTitle(QtGui.QApplication.translate("LicenseDialog", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.license.setText(QtGui.QApplication.translate("LicenseDialog", "       Copyright (c) 2008 GFORGX <gforgx@gmail.com>\n"
"\n"
"       Redistribution and use in source and binary forms, with or without\n"
"       modification, are permitted provided that the following conditions are\n"
"       met:\n"
"       \n"
"       * Redistributions of source code must retain the above copyright\n"
"         notice, this list of conditions and the following disclaimer.\n"
"       * Redistributions in binary form must reproduce the above\n"
"         copyright notice, this list of conditions and the following disclaimer\n"
"         in the documentation and/or other materials provided with the\n"
"         distribution.\n"
"       * Neither the name of the  nor the names of its\n"
"         contributors may be used to endorse or promote products derived from\n"
"         this software without specific prior written permission.\n"
"       \n"
"       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n"
"       \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n"
"       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n"
"       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n"
"       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n"
"       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n"
"       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n"
"       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n"
"       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n"
"       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n"
"       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

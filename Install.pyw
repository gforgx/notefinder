# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI-tests/install.ui'
#
# Created: Sun Jul 27 22:28:41 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from time import sleep

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(214,71)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label,0,0,1,1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox,1,0,1,1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.label.setText(QtGui.QApplication.translate("Dialog", "Do you wish to install NoteFinder?", None, QtGui.QApplication.UnicodeUTF8))

class Installer(QtGui.QDialog):
    ''' Installer class '''
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    
        # Connections
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.install)
    
    def install(self):
        self.ui.buttonBox.setEnabled(False)
        self.ui.label.setText("Installing...")
        sleep(1)
        os.system("C:\Python25\python.exe setup.py install")
        self.accept()

app = QtGui.QApplication(sys.argv)
installer = Installer()
installer.show()
sys.exit(app.exec_())
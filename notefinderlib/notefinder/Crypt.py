# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/crypt.ui'
#
# Created: Thu Dec  4 17:27:36 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CryptDialog(object):
    def setupUi(self, CryptDialog):
        CryptDialog.setObjectName("CryptDialog")
        CryptDialog.resize(250, 100)
        self.gridLayout = QtGui.QGridLayout(CryptDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(CryptDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CryptDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.keyEdit = QtGui.QLineEdit(CryptDialog)
        self.keyEdit.setObjectName("keyEdit")
        self.gridLayout.addWidget(self.keyEdit, 1, 0, 1, 1)

        self.retranslateUi(CryptDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CryptDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CryptDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CryptDialog)

    def retranslateUi(self, CryptDialog):
        CryptDialog.setWindowTitle(QtGui.QApplication.translate("CryptDialog", "Encryption", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CryptDialog", "<b>Enter key</b>", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copy.ui'
#
# Created: Thu Oct  9 19:52:35 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CopyDialog(object):
    def setupUi(self, CopyDialog):
        CopyDialog.setObjectName("CopyDialog")
        CopyDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CopyDialog.resize(307, 300)
        self.gridLayout = QtGui.QGridLayout(CopyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(CopyDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.notebooks = QtGui.QListWidget(CopyDialog)
        self.notebooks.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.notebooks.setObjectName("notebooks")
        self.gridLayout.addWidget(self.notebooks, 2, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(CopyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.deleteBox = QtGui.QCheckBox(CopyDialog)
        self.deleteBox.setObjectName("deleteBox")
        self.gridLayout.addWidget(self.deleteBox, 3, 1, 1, 1)

        self.retranslateUi(CopyDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CopyDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CopyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CopyDialog)

    def retranslateUi(self, CopyDialog):
        CopyDialog.setWindowTitle(QtGui.QApplication.translate("CopyDialog", "Copy entry to another notebooks", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CopyDialog", "Select notebooks", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBox.setText(QtGui.QApplication.translate("CopyDialog", "Delete from current notebook", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

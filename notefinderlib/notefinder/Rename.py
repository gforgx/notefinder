# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI_I/rename.ui'
#
# Created: Tue Nov 25 19:40:04 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RenameDialog(object):
    def setupUi(self, RenameDialog):
        RenameDialog.setObjectName("RenameDialog")
        RenameDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        RenameDialog.resize(315, 122)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RenameDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(RenameDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(RenameDialog)
        self.label_2.setPixmap(QtGui.QPixmap(":/rename_small.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(RenameDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(RenameDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(RenameDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(RenameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(RenameDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), RenameDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), RenameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RenameDialog)

    def retranslateUi(self, RenameDialog):
        self.label_3.setText(QtGui.QApplication.translate("RenameDialog", "<b>Rename entry</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RenameDialog", "Rename to:", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

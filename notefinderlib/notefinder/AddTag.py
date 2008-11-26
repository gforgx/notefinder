# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI_I/add_tag.ui'
#
# Created: Tue Nov 25 19:30:25 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AddTagDialog(object):
    def setupUi(self, AddTagDialog):
        AddTagDialog.setObjectName("AddTagDialog")
        AddTagDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddTagDialog.resize(310, 157)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddTagDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(AddTagDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.iconLabel = QtGui.QLabel(AddTagDialog)
        self.iconLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout.addWidget(self.iconLabel, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(AddTagDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 1, 1)
        self.helpLabel = QtGui.QLabel(AddTagDialog)
        self.helpLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.helpLabel.setObjectName("helpLabel")
        self.gridLayout.addWidget(self.helpLabel, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AddTagDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 1)
        self.label = QtGui.QLabel(AddTagDialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.retranslateUi(AddTagDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AddTagDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AddTagDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTagDialog)

    def retranslateUi(self, AddTagDialog):
        self.helpLabel.setText(QtGui.QApplication.translate("AddTagDialog", "Tag is a keyword that helps to organize and \n"
"find notes quickly.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddTagDialog", "<b>Add new tag</b>", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

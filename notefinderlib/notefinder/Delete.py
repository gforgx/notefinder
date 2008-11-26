# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI_I/delete.ui'
#
# Created: Tue Nov 25 19:31:42 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        DeleteDialog.setObjectName("DeleteDialog")
        DeleteDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DeleteDialog.resize(283, 125)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DeleteDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Label = QtGui.QLabel(DeleteDialog)
        self.Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.deleteLabel = QtGui.QLabel(DeleteDialog)
        self.deleteLabel.setObjectName("deleteLabel")
        self.gridLayout.addWidget(self.deleteLabel, 0, 1, 1, 1)
        self.label = QtGui.QLabel(DeleteDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(DeleteDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DeleteDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DeleteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        self.Label.setText(QtGui.QApplication.translate("DeleteDialog", "Are you really sure you want to delete \n"
"selected entries?", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteLabel.setText(QtGui.QApplication.translate("DeleteDialog", "<b>Delete entries</b>", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

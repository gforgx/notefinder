# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI_I/delete_notebook.ui'
#
# Created: Tue Nov 25 19:31:53 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeleteNotebookDialog(object):
    def setupUi(self, DeleteNotebookDialog):
        DeleteNotebookDialog.setObjectName("DeleteNotebookDialog")
        DeleteNotebookDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DeleteNotebookDialog.resize(250, 157)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteNotebookDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DeleteNotebookDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Label = QtGui.QLabel(DeleteNotebookDialog)
        self.Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteNotebookDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.deleteLabel = QtGui.QLabel(DeleteNotebookDialog)
        self.deleteLabel.setObjectName("deleteLabel")
        self.gridLayout.addWidget(self.deleteLabel, 0, 1, 1, 1)
        self.label = QtGui.QLabel(DeleteNotebookDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(DeleteNotebookDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DeleteNotebookDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DeleteNotebookDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteNotebookDialog)

    def retranslateUi(self, DeleteNotebookDialog):
        self.Label.setText(QtGui.QApplication.translate("DeleteNotebookDialog", "Are you really sure you want to delete \n"
"selected notebook?\n"
"Deleting it won\'t delete it\'s notes.\n"
"You can recreate this notebook again.", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteLabel.setText(QtGui.QApplication.translate("DeleteNotebookDialog", "<b>Delete notebook</b>", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

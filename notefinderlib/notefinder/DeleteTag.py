# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_tag.ui'
#
# Created: Thu Oct  9 19:53:03 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DeleteTagDialog(object):
    def setupUi(self, DeleteTagDialog):
        DeleteTagDialog.setObjectName("DeleteTagDialog")
        DeleteTagDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DeleteTagDialog.resize(254, 134)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteTagDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(DeleteTagDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Label = QtGui.QLabel(DeleteTagDialog)
        self.Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Label.setObjectName("Label")
        self.gridLayout.addWidget(self.Label, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteTagDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.deleteLabel = QtGui.QLabel(DeleteTagDialog)
        self.deleteLabel.setObjectName("deleteLabel")
        self.gridLayout.addWidget(self.deleteLabel, 0, 1, 1, 1)
        self.label = QtGui.QLabel(DeleteTagDialog)
        self.label.setPixmap(QtGui.QPixmap(":/list-remove_small.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(DeleteTagDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DeleteTagDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DeleteTagDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteTagDialog)

    def retranslateUi(self, DeleteTagDialog):
        self.Label.setText(QtGui.QApplication.translate("DeleteTagDialog", "Are you really sure you want to delete \n"
"selected tag?\n"
"Deleting tag won\'t delete related notes.", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteLabel.setText(QtGui.QApplication.translate("DeleteTagDialog", "<b>Delete tag</b>", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

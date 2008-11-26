# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI_I/message.ui'
#
# Created: Tue Nov 25 19:34:17 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MessageDialog(object):
    def setupUi(self, MessageDialog):
        MessageDialog.setObjectName("MessageDialog")
        MessageDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        MessageDialog.resize(363, 109)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MessageDialog.setWindowIcon(icon)
        MessageDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(MessageDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.message = QtGui.QLabel(MessageDialog)
        self.message.setOpenExternalLinks(True)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 0, 1, 1, 1)
        self.iconLabel = QtGui.QLabel(MessageDialog)
        self.iconLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout.addWidget(self.iconLabel, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(MessageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(MessageDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MessageDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MessageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MessageDialog)

    def retranslateUi(self, MessageDialog):
        pass

import notefinder_rc

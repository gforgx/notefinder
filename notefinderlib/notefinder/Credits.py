# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI/credits.ui'
#
# Created: Wed Nov 19 19:39:39 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CreditsDialog(object):
    def setupUi(self, CreditsDialog):
        CreditsDialog.setObjectName("CreditsDialog")
        CreditsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CreditsDialog.resize(520, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreditsDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(CreditsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(CreditsDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 498, 195))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.credits = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.credits.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.credits.setObjectName("credits")
        self.gridLayout.addWidget(self.credits, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(CreditsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreditsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CreditsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CreditsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CreditsDialog)

    def retranslateUi(self, CreditsDialog):
        CreditsDialog.setWindowTitle(QtGui.QApplication.translate("CreditsDialog", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.credits.setText(QtGui.QApplication.translate("CreditsDialog", "Author: Simonenko Sergey <gforgx@gmail.com>\n"
"PyCreole library: Peter Hoffmann <tosh54@gmail.com>\n"
"NoteFinder Icon designer: Zagorujko Olga <melfina2106@mail.ru>\n"
"SVG logo author: genius <nasledieprofessora@gmail.com>\n"
"Creative ideas: drw <drwpub@gmail.com>\n"
"Windows Beta-testing: Горын <crazylimo@gmail.com>\n"
"PyTesser library: Michael J.T. O\'Kelly <mokelly@mit.edu>\n"
"Icons set, CSS for Web Notebook Plugin: Pavluhin Andrey <dr.onx@mail.ru>\n"
"Russian l10n: Alexey Kolesnikov <ackerman@gmail.com>\n"
"iCal parser library: Max M <maxm@mxm.dk>\n"
"Mandriva mantainer: Funda Wang <fundawang@mandriva.org>\n"
"CreoleParser library (replaced PyCreole in 0.2.5): Stephan Day <stephen_day@gmail.com>", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

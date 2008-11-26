# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gforgx/UI_I/about.ui'
#
# Created: Tue Nov 25 19:30:01 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutDialog.resize(535, 275)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.vboxlayout = QtGui.QVBoxLayout(AboutDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.logoLabel = QtGui.QLabel(AboutDialog)
        self.logoLabel.setPixmap(QtGui.QPixmap(":/icons/logo.png"))
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setObjectName("logoLabel")
        self.vboxlayout.addWidget(self.logoLabel)
        self.versionLabel = QtGui.QLabel(AboutDialog)
        self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.vboxlayout.addWidget(self.versionLabel)
        self.dscLabel = QtGui.QLabel(AboutDialog)
        self.dscLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dscLabel.setObjectName("dscLabel")
        self.vboxlayout.addWidget(self.dscLabel)
        self.copyLabel = QtGui.QLabel(AboutDialog)
        self.copyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.copyLabel.setOpenExternalLinks(True)
        self.copyLabel.setObjectName("copyLabel")
        self.vboxlayout.addWidget(self.copyLabel)
        self.urlLabel = QtGui.QLabel(AboutDialog)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setOpenExternalLinks(True)
        self.urlLabel.setObjectName("urlLabel")
        self.vboxlayout.addWidget(self.urlLabel)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.creditsButton = QtGui.QPushButton(AboutDialog)
        self.creditsButton.setMinimumSize(QtCore.QSize(80, 0))
        self.creditsButton.setObjectName("creditsButton")
        self.hboxlayout.addWidget(self.creditsButton)
        self.licenseButton = QtGui.QPushButton(AboutDialog)
        self.licenseButton.setObjectName("licenseButton")
        self.hboxlayout.addWidget(self.licenseButton)
        self.closeButton = QtGui.QPushButton(AboutDialog)
        self.closeButton.setObjectName("closeButton")
        self.hboxlayout.addWidget(self.closeButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), AboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About - NoteFinder", None, QtGui.QApplication.UnicodeUTF8))
        self.dscLabel.setText(QtGui.QApplication.translate("AboutDialog", "Easy to use desktop note-taking application", None, QtGui.QApplication.UnicodeUTF8))
        self.copyLabel.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\">Copyright © 2007-2008 Simonenko Sergey &lt;<a href=\"mailto:gforgx@lavabit.com\"><span style=\" text-decoration: underline; color:#0057ae;\">gforgx@lavabit.com</span></a>&gt;</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.urlLabel.setText(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><a href=\"http://notefinder.co.cc\"><span style=\" text-decoration: underline; color:#0000ff;\">http://notefinder.co.cc</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.creditsButton.setText(QtGui.QApplication.translate("AboutDialog", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseButton.setText(QtGui.QApplication.translate("AboutDialog", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("AboutDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

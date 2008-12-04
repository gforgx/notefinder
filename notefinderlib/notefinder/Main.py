# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/main.ui'
#
# Created: Thu Dec  4 17:36:08 2008
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 619)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.entriesTab = QtGui.QWidget()
        self.entriesTab.setObjectName("entriesTab")
        self.gridLayout = QtGui.QGridLayout(self.entriesTab)
        self.gridLayout.setMargin(1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.entriesTab)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dateEdit = QtGui.QDateEdit(self.layoutWidget)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.metaList = QtGui.QListWidget(self.layoutWidget)
        self.metaList.setObjectName("metaList")
        self.verticalLayout_2.addWidget(self.metaList)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLabel = QtGui.QLabel(self.layoutWidget1)
        self.searchLabel.setObjectName("searchLabel")
        self.horizontalLayout.addWidget(self.searchLabel)
        self.searchEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.saveSearchButton = QtGui.QToolButton(self.layoutWidget1)
        self.saveSearchButton.setObjectName("saveSearchButton")
        self.horizontalLayout.addWidget(self.saveSearchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.notesList = QtGui.QListWidget(self.layoutWidget1)
        self.notesList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.notesList.setLayoutMode(QtGui.QListView.Batched)
        self.notesList.setObjectName("notesList")
        self.verticalLayout.addWidget(self.notesList)
        self.numberLabel = QtGui.QLabel(self.layoutWidget1)
        self.numberLabel.setObjectName("numberLabel")
        self.verticalLayout.addWidget(self.numberLabel)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.entriesTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuNoteFinder = QtGui.QMenu(self.menuBar)
        self.menuNoteFinder.setObjectName("menuNoteFinder")
        self.menuEntry = QtGui.QMenu(self.menuBar)
        self.menuEntry.setObjectName("menuEntry")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuPlugins = QtGui.QMenu(self.menuBar)
        self.menuPlugins.setObjectName("menuPlugins")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTag = QtGui.QMenu(self.menuBar)
        self.menuTag.setObjectName("menuTag")
        self.menuNotebooks = QtGui.QMenu(self.menuBar)
        self.menuNotebooks.setObjectName("menuNotebooks")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolbar = QtGui.QToolBar(MainWindow)
        self.mainToolbar.setIconSize(QtCore.QSize(16, 16))
        self.mainToolbar.setObjectName("mainToolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolbar)
        self.editToolbar = QtGui.QToolBar(MainWindow)
        self.editToolbar.setIconSize(QtCore.QSize(16, 16))
        self.editToolbar.setObjectName("editToolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.editToolbar)
        self.pluginsToolbar = QtGui.QToolBar(MainWindow)
        self.pluginsToolbar.setIconSize(QtCore.QSize(16, 16))
        self.pluginsToolbar.setObjectName("pluginsToolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.pluginsToolbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionToday = QtGui.QAction(MainWindow)
        self.actionToday.setObjectName("actionToday")
        self.actionAll = QtGui.QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.actionFindRelated = QtGui.QAction(MainWindow)
        self.actionFindRelated.setObjectName("actionFindRelated")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAddTag = QtGui.QAction(MainWindow)
        self.actionAddTag.setObjectName("actionAddTag")
        self.actionDeleteTag = QtGui.QAction(MainWindow)
        self.actionDeleteTag.setObjectName("actionDeleteTag")
        self.actionDeleteSelectedSearch = QtGui.QAction(MainWindow)
        self.actionDeleteSelectedSearch.setObjectName("actionDeleteSelectedSearch")
        self.actionE_Mail = QtGui.QAction(MainWindow)
        self.actionE_Mail.setObjectName("actionE_Mail")
        self.actionRename = QtGui.QAction(MainWindow)
        self.actionRename.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionRename.setObjectName("actionRename")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionBold = QtGui.QAction(MainWindow)
        self.actionBold.setCheckable(False)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(MainWindow)
        self.actionItalic.setCheckable(False)
        self.actionItalic.setChecked(False)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderlined = QtGui.QAction(MainWindow)
        self.actionUnderlined.setCheckable(False)
        self.actionUnderlined.setObjectName("actionUnderlined")
        self.actionHighlight = QtGui.QAction(MainWindow)
        self.actionHighlight.setCheckable(False)
        self.actionHighlight.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionHighlight.setObjectName("actionHighlight")
        self.actionTimestamp = QtGui.QAction(MainWindow)
        self.actionTimestamp.setObjectName("actionTimestamp")
        self.actionDeleteNotebook = QtGui.QAction(MainWindow)
        self.actionDeleteNotebook.setObjectName("actionDeleteNotebook")
        self.actionAddNotebook = QtGui.QAction(MainWindow)
        self.actionAddNotebook.setObjectName("actionAddNotebook")
        self.actionCopyEntry = QtGui.QAction(MainWindow)
        self.actionCopyEntry.setObjectName("actionCopyEntry")
        self.actionBacklinks = QtGui.QAction(MainWindow)
        self.actionBacklinks.setObjectName("actionBacklinks")
        self.actionCreateIndex = QtGui.QAction(MainWindow)
        self.actionCreateIndex.setObjectName("actionCreateIndex")
        self.actionMerge = QtGui.QAction(MainWindow)
        self.actionMerge.setObjectName("actionMerge")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionOpenExternally = QtGui.QAction(MainWindow)
        self.actionOpenExternally.setObjectName("actionOpenExternally")
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        self.actionImage = QtGui.QAction(MainWindow)
        self.actionImage.setObjectName("actionImage")
        self.actionBulletedList = QtGui.QAction(MainWindow)
        self.actionBulletedList.setObjectName("actionBulletedList")
        self.actionEncrypt = QtGui.QAction(MainWindow)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.menuNoteFinder.addAction(self.actionPreferences)
        self.menuNoteFinder.addSeparator()
        self.menuNoteFinder.addAction(self.actionExit)
        self.menuEntry.addAction(self.actionNew)
        self.menuEntry.addAction(self.actionDelete)
        self.menuEntry.addAction(self.actionEncrypt)
        self.menuEntry.addSeparator()
        self.menuEntry.addAction(self.actionCopyEntry)
        self.menuEntry.addAction(self.actionRename)
        self.menuEntry.addSeparator()
        self.menuEntry.addAction(self.actionE_Mail)
        self.menuEntry.addSeparator()
        self.menuEntry.addAction(self.actionBacklinks)
        self.menuEntry.addAction(self.actionFindRelated)
        self.menuEntry.addSeparator()
        self.menuEntry.addAction(self.actionCreateIndex)
        self.menuEntry.addAction(self.actionMerge)
        self.menuEntry.addSeparator()
        self.menuEntry.addAction(self.actionOpenExternally)
        self.menuView.addAction(self.actionAll)
        self.menuView.addAction(self.actionToday)
        self.menuView.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuTag.addAction(self.actionAddTag)
        self.menuTag.addAction(self.actionDeleteTag)
        self.menuNotebooks.addAction(self.actionAddNotebook)
        self.menuNotebooks.addAction(self.actionDeleteNotebook)
        self.menuNotebooks.addSeparator()
        self.menuEdit.addAction(self.actionBold)
        self.menuEdit.addAction(self.actionItalic)
        self.menuEdit.addAction(self.actionUnderlined)
        self.menuEdit.addAction(self.actionHighlight)
        self.menuEdit.addAction(self.actionBulletedList)
        self.menuEdit.addAction(self.actionImage)
        self.menuEdit.addAction(self.actionTimestamp)
        self.menuBar.addAction(self.menuNoteFinder.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuNotebooks.menuAction())
        self.menuBar.addAction(self.menuTag.menuAction())
        self.menuBar.addAction(self.menuEntry.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuPlugins.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.mainToolbar.addAction(self.actionNew)
        self.mainToolbar.addAction(self.actionSave)
        self.mainToolbar.addAction(self.actionAll)
        self.mainToolbar.addAction(self.actionToday)
        self.editToolbar.addAction(self.actionBold)
        self.editToolbar.addAction(self.actionItalic)
        self.editToolbar.addAction(self.actionUnderlined)
        self.editToolbar.addAction(self.actionHighlight)
        self.editToolbar.addAction(self.actionBulletedList)
        self.editToolbar.addAction(self.actionImage)
        self.editToolbar.addAction(self.actionTimestamp)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "NoteFinder", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "yyyy-M-d", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLabel.setText(QtGui.QApplication.translate("MainWindow", "Search: ", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSearchButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.entriesTab), QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNoteFinder.setTitle(QtGui.QApplication.translate("MainWindow", "Note&Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEntry.setTitle(QtGui.QApplication.translate("MainWindow", "Ent&ries", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "&Show", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("MainWindow", "&Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTag.setTitle(QtGui.QApplication.translate("MainWindow", "Ta&gs", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNotebooks.setTitle(QtGui.QApplication.translate("MainWindow", "&Notebooks", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.editToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginsToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToday.setText(QtGui.QApplication.translate("MainWindow", "Today", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToday.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAll.setText(QtGui.QApplication.translate("MainWindow", "All notes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindRelated.setText(QtGui.QApplication.translate("MainWindow", "Find related notes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddTag.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteTag.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteSelectedSearch.setText(QtGui.QApplication.translate("MainWindow", "Delete selected search", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_Mail.setText(QtGui.QApplication.translate("MainWindow", "E-Mail", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setText(QtGui.QApplication.translate("MainWindow", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRename.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBold.setText(QtGui.QApplication.translate("MainWindow", "Bold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBold.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionItalic.setText(QtGui.QApplication.translate("MainWindow", "Italic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionItalic.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnderlined.setText(QtGui.QApplication.translate("MainWindow", "Underlined", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnderlined.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHighlight.setText(QtGui.QApplication.translate("MainWindow", "Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTimestamp.setText(QtGui.QApplication.translate("MainWindow", "Timestamp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteNotebook.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddNotebook.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopyEntry.setText(QtGui.QApplication.translate("MainWindow", "Copy to another notebooks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopyEntry.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBacklinks.setText(QtGui.QApplication.translate("MainWindow", "Backlinks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreateIndex.setText(QtGui.QApplication.translate("MainWindow", "Create index", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMerge.setText(QtGui.QApplication.translate("MainWindow", "Merge", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenExternally.setText(QtGui.QApplication.translate("MainWindow", "Open externally", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImage.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBulletedList.setText(QtGui.QApplication.translate("MainWindow", "Bulleted List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEncrypt.setText(QtGui.QApplication.translate("MainWindow", "Encrypt", None, QtGui.QApplication.UnicodeUTF8))

import notefinder_rc

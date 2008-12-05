#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2008 Simonenko Sergey <gforgx@gmail.com>
#
#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#
#       * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following disclaimer
#       in the documentation and/or other materials provided with the
#       distribution.
#       * Neither the name of the  nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#      "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Standard library imports
import sys
from datetime import datetime
from time import localtime
from inspect import isclass

try:
    from pkg_resources import iter_entry_points
    PLUGINS = True
except ImportError:
    PLUGINS = False

from PyQt4 import Qt

# Library imports
from notefinderlib.libnotetaking import *
from notefinderlib.creoleparser import text2html

# Interface imports
from notefinderlib.notefinder.About import Ui_AboutDialog
from notefinderlib.notefinder.AddTag import Ui_AddTagDialog
from notefinderlib.notefinder.CopyEntry import Ui_CopyDialog
from notefinderlib.notefinder.Credits import Ui_CreditsDialog
from notefinderlib.notefinder.Crypt import Ui_CryptDialog
from notefinderlib.notefinder.Decrypt import Ui_DecryptDialog
from notefinderlib.notefinder.Delete import Ui_DeleteDialog
from notefinderlib.notefinder.DeleteNotebook import Ui_DeleteNotebookDialog
from notefinderlib.notefinder.DeleteTag import Ui_DeleteTagDialog
from notefinderlib.notefinder.Editor import EditorWidget
from notefinderlib.notefinder.License import Ui_LicenseDialog
from notefinderlib.notefinder.Main import Ui_MainWindow
from notefinderlib.notefinder.Message import Ui_MessageDialog
from notefinderlib.notefinder.Notebook import Ui_NotebookDialog
from notefinderlib.notefinder.plugin import Plugin
from notefinderlib.notefinder.Rename import Ui_RenameDialog
from notefinderlib.notefinder.Settings import Ui_SettingsDialog
from notefinderlib.notefinder.notefinder_rc import *

__version__ = '0.3.7'

class Application(Qt.QObject):
    def __init__(self):
        Qt.QObject.__init__(self)
        self.application = Qt.QApplication(sys.argv)

        # l10n
        translator = Qt.QTranslator()
        translator.load('notefinder_' + Qt.QLocale.system().name() + '.qm', ':/')
        self.application.installTranslator(translator)

        # Default settings
        self.settings = {
            'Bool': {
                'AutoSave' : True,
                'BackendIcons' : True,
                'Dates' : False,
                'Sessions' : True,
                'SearchCompletion' : True,
                'SearchOnTheFly' : True,
                'Toolbars' : True,
                'TrayIcon' : True,
                'Tooltips' : True,
            },
            'String': {
                'Icons' : 'silk'
            },
            'Int': {
                'SplitterLeft' : 220,
                'SplitterRight' : 1030,
            },
            'List': {
                'Session' : [],
                'Searches' : [],
            }
        }

        # Backend icons
        self.backendIcons = {
            'DokuWiki' : ':/icons/dokuwiki.png',
            'iPod' : ':/icons/ipod.png',
            'Zim' : ':/icons/zim.png',
            'iCal' : ':/icons/ical.png',
            'Files' : ':/icons/icon.png',
            'FileSystem' : ':/icons/icon.png',
            'Wixi' : ':/icons/wixi.png',
            'RSS' : ':/icons/rss.png',
            'Mail': ':/icons/%s/mail.png' % (self.settings['String']['Icons'])
        }


        # Main window stuff
        self.mainWindow = Qt.QMainWindow()
        self.mainWindow.ui = Ui_MainWindow()
        self.mainWindow.ui.setupUi(self.mainWindow)
        self.mainWindow.setWindowIcon(Qt.QIcon(':/icons/icon.png'))
    
        self.mainWindow.ui.closeButton = Qt.QToolButton(self.mainWindow)
        self.mainWindow.ui.closeButton.setShortcut('Ctrl+W')
        self.mainWindow.ui.tabWidget.setCornerWidget(self.mainWindow.ui.closeButton)

        self.mainWindow.closeEvent = self.closeEvent

        # Сontext menus
        noteMenu = (
            self.mainWindow.ui.actionE_Mail,
            self.mainWindow.ui.actionBacklinks,
            self.mainWindow.ui.actionFindRelated,
            self.mainWindow.ui.actionCreateIndex,
            self.mainWindow.ui.actionMerge,
            self.mainWindow.ui.actionRename,
            self.mainWindow.ui.actionCopyEntry,
            self.mainWindow.ui.actionOpenExternally,
            self.mainWindow.ui.actionEncrypt,
            self.mainWindow.ui.actionDelete
            )

        metaMenu = (
            self.mainWindow.ui.actionDeleteNotebook,
            self.mainWindow.ui.actionDeleteTag,
            self.mainWindow.ui.actionDeleteSelectedSearch
            )

        self.mainWindow.ui.notesList.setContextMenuPolicy(Qt.Qt.ActionsContextMenu)
        self.mainWindow.ui.metaList.setContextMenuPolicy(Qt.Qt.ActionsContextMenu)

        self.mainWindow.ui.notesList.addActions(noteMenu)
        self.mainWindow.ui.metaList.addActions(metaMenu)

        self.connect(self.mainWindow.ui.actionAboutQt, Qt.SIGNAL('triggered()'), self.application.aboutQt)
        self.connect(self.mainWindow.ui.metaList, Qt.SIGNAL('itemSelectionChanged()'), self.refreshMenu)
        self.connect(self.mainWindow.ui.closeButton, Qt.SIGNAL('clicked()'), self.closeTab)
        self.connect(self.mainWindow.ui.actionExit, Qt.SIGNAL('triggered()'), self.application.quit)
        
        self.connect(self.mainWindow.ui.dateEdit, Qt.SIGNAL('editingFinished()'), self.openDate)
        self.connect(self.mainWindow.ui.metaList, Qt.SIGNAL('itemClicked(QListWidgetItem *)'), self.openMeta)
        self.connect(self.mainWindow.ui.searchEdit, QtCore.SIGNAL("returnPressed()"), self.search)
        
        self.connect(self.mainWindow.ui.actionNew, Qt.SIGNAL('triggered()'), self.new)
        self.connect(self.mainWindow.ui.actionCreateIndex,  Qt.SIGNAL('triggered()'), self.buildListIndex)
        self.connect(self.mainWindow.ui.actionMerge, Qt.SIGNAL('triggered()'), self.merge)
        self.connect(self.mainWindow.ui.notesList, Qt.SIGNAL('itemDoubleClicked(QListWidgetItem *)'), self.openFromList) 
        self.connect(self.mainWindow.ui.actionSave, Qt.SIGNAL('triggered()'), self.saveNote)

        self.connect(self.mainWindow.ui.actionE_Mail, Qt.SIGNAL('triggered()'), self.email)
        self.connect(self.mainWindow.ui.actionOpenExternally, Qt.SIGNAL('triggered()'), self.openExternally)
        self.connect(self.mainWindow.ui.actionFindRelated, Qt.SIGNAL('triggered()'), self.findRelated)
        self.connect(self.mainWindow.ui.actionBacklinks, Qt.SIGNAL('triggered()'), self.backlinks)

        self.connect(self.mainWindow.ui.actionAll, Qt.SIGNAL('triggered()'), self.showAll)
        self.connect(self.mainWindow.ui.actionToday, Qt.SIGNAL('triggered()'), self.today)
        
        self.connect(self.mainWindow.ui.saveSearchButton, Qt.SIGNAL('clicked()'), self.saveSearch)
        self.connect(self.mainWindow.ui.actionDeleteSelectedSearch, Qt.SIGNAL('triggered()'), self.deleteSearch)

        self.connect(self.mainWindow.ui.actionBold, Qt.SIGNAL('triggered()'), self.bold)
        self.connect(self.mainWindow.ui.actionItalic, Qt.SIGNAL('triggered()'), self.italic)
        self.connect(self.mainWindow.ui.actionUnderlined, Qt.SIGNAL('triggered()'), self.underline)
        self.connect(self.mainWindow.ui.actionHighlight, Qt.SIGNAL('triggered()'), self.highlight)
        self.connect(self.mainWindow.ui.actionImage, Qt.SIGNAL('triggered()'), self.image)
        self.connect(self.mainWindow.ui.actionTimestamp, Qt.SIGNAL('triggered()'), self.insertTime)
        self.connect(self.mainWindow.ui.actionBulletedList, Qt.SIGNAL('triggered()'), self.list)

        self.connect(self.mainWindow.ui.splitter, Qt.SIGNAL('splitterMoved (int,int)'), self.saveSizer)

        self.writeActions = (
            self.mainWindow.ui.actionNew,
            self.mainWindow.ui.actionRename,
            self.mainWindow.ui.actionDelete,
            self.mainWindow.ui.actionSave,
            self.mainWindow.ui.actionEncrypt,
            )

        self.wikiActions = (
            self.mainWindow.ui.actionBacklinks,
            self.mainWindow.ui.actionCreateIndex,
            self.mainWindow.ui.actionMerge
        )

        # Tray
        self.tray = Qt.QSystemTrayIcon(self)
        self.tray.setIcon(Qt.QIcon(':/icons/icon.png'))

        self.headerAction = Qt.QWidgetAction(self)
        self.headerFrame = Qt.QFrame()
        self.headerFrame.setFrameShape(Qt.QFrame.StyledPanel)
        self.headerAction.setDefaultWidget(self.headerFrame)
        self.headerLayout = Qt.QHBoxLayout()
        self.headerLayout.setMargin(3)
        self.headerLayout.setSpacing(5)
        self.headerFrame.setLayout(self.headerLayout)
        self.headerLabel = Qt.QLabel()
        self.headerLabel.setPixmap(Qt.QPixmap(':/icons/%s/small/note.png' % (self.settings['String']['Icons'])))
        self.headerLayout.insertWidget(-1, self.headerLabel, 0)
        self.headerText = Qt.QLabel('<b>NoteFinder %s</b>' % (__version__))
        self.headerLayout.insertWidget(-1, self.headerText, 20)
        
        self.menu = Qt.QMenu()
        self.menu.addActions((self.headerAction, self.mainWindow.ui.actionNew))
        self.menu.addSeparator()
        self.pluginsMenu = Qt.QMenu('Plugins')
        self.menu.addMenu(self.pluginsMenu)
        self.menu.addSeparator()
        self.menu.addActions((self.mainWindow.ui.actionPreferences, self.mainWindow.ui.actionExit))
        self.tray.setContextMenu(self.menu)
        
        # Other dialogs
        self.aboutDialog = Qt.QDialog()
        self.aboutDialog.ui = Ui_AboutDialog()
        self.aboutDialog.ui.setupUi(self.aboutDialog)
        self.aboutDialog.ui.versionLabel.setText('<h2>%s</h2>' % (__version__))

        self.connect(self.mainWindow.ui.actionAbout, Qt.SIGNAL('triggered()'), self.aboutDialog.show)

        self.addTagDialog = Qt.QDialog()
        self.addTagDialog.ui = Ui_AddTagDialog()
        self.addTagDialog.ui.setupUi(self.addTagDialog)
 
        self.connect(self.mainWindow.ui.actionAddTag, Qt.SIGNAL('triggered()'), self.addTagDialog.show)
        self.connect(self.addTagDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.addTag)

        self.copyDialog = Qt.QDialog()
        self.copyDialog.ui = Ui_CopyDialog()
        self.copyDialog.ui.setupUi(self.copyDialog)

        self.connect(self.mainWindow.ui.actionCopyEntry, Qt.SIGNAL('triggered()'), self.copyDialog.show)
        self.connect(self.copyDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.copyEntry)

        self.creditsDialog = Qt.QDialog()
        self.creditsDialog.ui = Ui_CreditsDialog()
        self.creditsDialog.ui.setupUi(self.creditsDialog)

        self.connect(self.aboutDialog.ui.creditsButton, Qt.SIGNAL('clicked()'), self.creditsDialog.show)

        self.cryptDialog = Qt.QDialog()
        self.cryptDialog.ui = Ui_CryptDialog()
        self.cryptDialog.ui.setupUi(self.cryptDialog)

        self.connect(self.mainWindow.ui.actionEncrypt, Qt.SIGNAL('triggered()'), self.cryptDialog.show)
        self.connect(self.cryptDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.encrypt)

        self.decryptDialog = Qt.QDialog()
        self.decryptDialog.ui = Ui_DecryptDialog()
        self.decryptDialog.ui.setupUi(self.decryptDialog)

        self.deleteDialog = Qt.QDialog()
        self.deleteDialog.ui = Ui_DeleteDialog()
        self.deleteDialog.ui.setupUi(self.deleteDialog)

        self.connect(self.mainWindow.ui.actionDelete, Qt.SIGNAL('triggered()'), self.deleteDialog.show)
        self.connect(self.deleteDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.deleteNotes)
        
        self.deleteNotebookDialog = Qt.QDialog()
        self.deleteNotebookDialog.ui = Ui_DeleteNotebookDialog()
        self.deleteNotebookDialog.ui.setupUi(self.deleteNotebookDialog)

        self.connect(self.mainWindow.ui.actionDeleteNotebook, Qt.SIGNAL('triggered()'), self.deleteNotebookDialog.show)
        self.connect(self.deleteNotebookDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.deleteNotebook)

        self.deleteTagDialog = Qt.QDialog()
        self.deleteTagDialog.ui = Ui_DeleteTagDialog()
        self.deleteTagDialog.ui.setupUi(self.deleteTagDialog)

        self.connect(self.mainWindow.ui.actionDeleteTag, Qt.SIGNAL('triggered()'), self.deleteTagDialog.show)
        self.connect(self.deleteTagDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.deleteTag)

        self.licenseDialog = Qt.QDialog()
        self.licenseDialog.ui = Ui_LicenseDialog()
        self.licenseDialog.ui.setupUi(self.licenseDialog)

        self.connect(self.aboutDialog.ui.licenseButton, Qt.SIGNAL('clicked()'), self.licenseDialog.show)

        self.messageDialog = Qt.QDialog()
        self.messageDialog.ui = Ui_MessageDialog()
        self.messageDialog.ui.setupUi(self.messageDialog)
        
        self.notebookDialog = Qt.QDialog()
        self.notebookDialog.ui = Ui_NotebookDialog()
        self.notebookDialog.ui.setupUi(self.notebookDialog)

        self.notebookDialog.settings = {}
        for i in backends:
            self.notebookDialog.ui.backends.addItem(Qt.QIcon(self.backendIcons[i]), i)
        
        self.selectBackend()

        self.connect(self.mainWindow.ui.actionAddNotebook, Qt.SIGNAL('triggered()'), self.notebookDialog.show)
        self.connect(self.notebookDialog.ui.backends, Qt.SIGNAL('currentIndexChanged(const QString)'), self.selectBackend)
        self.connect(self.notebookDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.addNotebook)

        self.renameDialog = Qt.QDialog()
        self.renameDialog.ui = Ui_RenameDialog()
        self.renameDialog.ui.setupUi(self.renameDialog)

        self.connect(self.mainWindow.ui.actionRename, Qt.SIGNAL('triggered()'), self.renameDialog.show)
        self.connect(self.renameDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.renameNote)
        
        # Settings dialog
        self.settingsDialog = Qt.QDialog()
        self.settingsDialog.ui = Ui_SettingsDialog()
        self.settingsDialog.ui.setupUi(self.settingsDialog)
        self.settingsDialog.ui.updatePluginAction = Qt.QAction(self.settingsDialog)
        self.settingsDialog.ui.listWidget.setContextMenuPolicy(Qt.Qt.ActionsContextMenu)
        self.settingsDialog.ui.listWidget.addAction(self.settingsDialog.ui.updatePluginAction)

        self.connect(self.mainWindow.ui.actionPreferences, Qt.SIGNAL('triggered()'), self.settingsDialog.show)
        self.connect(self.settingsDialog.ui.buttonBox, Qt.SIGNAL('accepted()'), self.writeSettings)
        self.connect(self.settingsDialog.ui.listWidget, Qt.SIGNAL('itemSelectionChanged()'), self.updatePluginMenu)
        self.connect(self.settingsDialog.ui.updatePluginAction, Qt.SIGNAL('triggered()'), self.setPlugins)
        self.connect(self.settingsDialog.ui.applyThemeButton, Qt.SIGNAL('clicked()'), self.updateIcons)
        
        # Bold font
        self.boldFont = Qt.QFont()
        self.boldFont.setBold(True)
        
        self.readSettings()
        self.applySettings()
        self.mainWindow.ui.splitter.setSizes([self.settings['Int']['SplitterLeft'], self.settings['Int']['SplitterRight']])
        
        # Initializing notebook
        self.setNotebook(config.getNotebook(), True)

        self.loadPlugins()

        self.refresh()

        if self.settings['Bool']['Sessions']:
            for i in self.settings['List']['Session']:
                try:
                    self.openNote(i)
                except:
                    pass

    def readSettings(self):
        config = Config()
        for i in self.settings['Bool']:
            try:
                self.settings['Bool'][i] = config.getboolean('UI', i)
            except:
                pass
        
        for i in self.settings['String']:
            try:
                self.settings['String'][i] = config.get('UI', i)
            except:
                pass

        for i in self.settings['Int']:
            try:
                self.settings['Int'][i] = config.getint('UI', i)
            except:
                pass

        for i in self.settings['List']:
            try:
                st = config.get('UI', i)
                if not st == '':
                    self.settings['List'][i] = config.get('UI', i).split('|||')
            except:
                pass

    def applySettings(self):
        self.settingsDialog.ui.toolTips.setChecked(self.settings['Bool']['Tooltips'])
        self.settingsDialog.ui.backendIcons.setChecked(self.settings['Bool']['BackendIcons'])
        self.settingsDialog.ui.trayIcon.setChecked(self.settings['Bool']['TrayIcon'])
        self.settingsDialog.ui.autoSave.setChecked(self.settings['Bool']['AutoSave'])
        self.settingsDialog.ui.searchCompletion.setChecked(self.settings['Bool']['SearchCompletion'])
        self.settingsDialog.ui.searchOnTheFly.setChecked(self.settings['Bool']['SearchOnTheFly'])
        self.settingsDialog.ui.showDates.setChecked(self.settings['Bool']['Dates'])
        self.settingsDialog.ui.sessions.setChecked(self.settings['Bool']['Sessions'])


        if self.settings['Bool']['TrayIcon']:
            self.tray.show()
            self.connect(self.tray, Qt.SIGNAL('activated(QSystemTrayIcon::ActivationReason)'), self.showHide)

        if self.settings['Bool']['SearchOnTheFly']:
            self.connect(self.mainWindow.ui.searchEdit, Qt.SIGNAL('textChanged(const QString)'), self.search)
    
        self.setIcons()

    def setIcons(self):
        # Main window
        ## Action icons
        self.mainWindow.ui.actionNew.setIcon(Qt.QIcon(':/icons/%s/add.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionSave.setIcon(Qt.QIcon(':/icons/%s/save.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionDelete.setIcon(Qt.QIcon(':/icons/%s/delete.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionAll.setIcon(Qt.QIcon(':/icons/%s/notebook.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionToday.setIcon(Qt.QIcon(':/icons/%s/calendar.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionBold.setIcon(Qt.QIcon(':/icons/%s/bold.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionUnderlined.setIcon(Qt.QIcon(':/icons/%s/underline.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionHighlight.setIcon(Qt.QIcon(':/icons/%s/highlight.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionItalic.setIcon(Qt.QIcon(':/icons/%s/italic.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionBulletedList.setIcon(Qt.QIcon(':/icons/%s/list.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionImage.setIcon(Qt.QIcon(':/icons/%s/image.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionTimestamp.setIcon(Qt.QIcon(':/icons/%s/time.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionPreferences.setIcon(Qt.QIcon(':/icons/%s/preferences.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionExit.setIcon(Qt.QIcon(':/icons/%s/exit.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionAddNotebook.setIcon(Qt.QIcon(':/icons/%s/add.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionDeleteNotebook.setIcon(Qt.QIcon(':/icons/%s/delete.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionAddTag.setIcon(Qt.QIcon(':/icons/%s/add.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionDeleteTag.setIcon(Qt.QIcon(':/icons/%s/delete.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionCopyEntry.setIcon(Qt.QIcon(':/icons/%s/copy.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionRename.setIcon(Qt.QIcon(':/icons/%s/rename.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionE_Mail.setIcon(Qt.QIcon(':/icons/%s/mail.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionBacklinks.setIcon(Qt.QIcon(':/icons/%s/undo.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionFindRelated.setIcon(Qt.QIcon(':/icons/%s/find.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionCreateIndex.setIcon(Qt.QIcon(':/icons/%s/list.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionMerge.setIcon(Qt.QIcon(':/icons/%s/list.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionOpenExternally.setIcon(Qt.QIcon(':/icons/%s/open.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionAbout.setIcon(Qt.QIcon(':/icons/%s/about.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionAboutQt.setIcon(Qt.QIcon(':/icons/%s/about.png' % (self.settings['String']['Icons'])))
        self.mainWindow.ui.actionDeleteSelectedSearch.setIcon(Qt.QIcon(':/icons/%s/delete.png' % (self.settings['String']['Icons'])))

        ## Misc
        self.mainWindow.ui.tabWidget.setTabIcon(0, Qt.QIcon(':/icons/%s/notebook.png' % (self.settings['String']['Icons'])))

        self.mainWindow.ui.closeButton.setIcon(Qt.QIcon(':/icons/%s/close.png' % (self.settings['String']['Icons'])))

        # Dialogs
        self.deleteDialog.ui.label.setPixmap(Qt.QPixmap(':/icons/%s/small/delete.png' % (self.settings['String']['Icons'])))
        self.addTagDialog.ui.iconLabel.setPixmap(Qt.QPixmap(':/icons/%s/add.png' % (self.settings['String']['Icons'])))
        self.deleteTagDialog.ui.label.setPixmap(Qt.QPixmap(':/icons/%s/small/delete.png' % (self.settings['String']['Icons'])))
        self.deleteNotebookDialog.ui.label.setPixmap(Qt.QPixmap(':/icons/%s/small/delete.png' % (self.settings['String']['Icons'])))
        self.renameDialog.ui.label.setPixmap(Qt.QPixmap(':/icons/%s/small/rename.png' % (self.settings['String']['Icons'])))
        self.notebookDialog.ui.icon.setPixmap(Qt.QPixmap(':/icons/%s/small/notebook.png' % (self.settings['String']['Icons'])))
        self.messageDialog.ui.iconLabel.setPixmap(Qt.QPixmap(':/icons/icon_small.png'))
        self.settingsDialog.ui.tabWidget.setTabIcon(0, Qt.QIcon(':/icons/icon.png'))
        self.settingsDialog.ui.tabWidget.setTabIcon(1, Qt.QIcon(':/icons/%s/search.png' % (self.settings['String']['Icons'])))
        self.settingsDialog.ui.tabWidget.setTabIcon(2, Qt.QIcon(':/icons/%s/note.png' % (self.settings['String']['Icons'])))
        self.settingsDialog.ui.tabWidget.setTabIcon(3, Qt.QIcon(':/icons/%s/add.png' % (self.settings['String']['Icons'])))

    def updateIcons(self):
        if not config.has_section('UI'):
            config.add_section('UI')
    
        self.settings['String']['Icons'] = str(self.settingsDialog.ui.themeEdit.currentText().toUtf8())
        config.set('UI', 'Icons', self.settings['String']['Icons'])
        config.write(open(config.file, 'w'))

        self.setIcons()

    def writeSettings(self):
        if not config.has_section('UI'):
            config.add_section('UI')

        config.set('UI', 'AutoSave', self.settingsDialog.ui.autoSave.isChecked())
        config.set('UI', 'BackendIcons', self.settingsDialog.ui.backendIcons.isChecked())
        config.set('UI', 'SearchCompletion', self.settingsDialog.ui.searchCompletion.isChecked())
        config.set('UI', 'SearchOnTheFly', self.settingsDialog.ui.searchOnTheFly.isChecked())
        config.set('UI', 'Sessions', self.settingsDialog.ui.sessions.isChecked())
        config.set('UI', 'Tooltips', self.settingsDialog.ui.toolTips.isChecked())
        config.set('UI', 'TrayIcon', self.settingsDialog.ui.trayIcon.isChecked())
        config.set('UI', 'Dates', self.settingsDialog.ui.showDates.isChecked())

        config.write(open(config.file, 'w'))

        self.readSettings()
        self.refresh()

    def loadPlugins(self):
        if PLUGINS:
            for ep in iter_entry_points('notefinder.plugins'):
                try:
                    plugin = ep.load()
                    if isclass(plugin):
                        if issubclass(plugin, Plugin):
                            p = plugin(self)
                            
                            item = Qt.QListWidgetItem(p.icon(), p.text(), self.settingsDialog.ui.listWidget)
                            item.name = p.name
                            item.setToolTip(p.toolTip())
                            item.pluginEnabled = False

                            if config.has_option('Plugins', plugin.name):
                                if config.getboolean('Plugins', plugin.name):
                                    p.load()
    
                                    item.pluginEnabled = True
                except:
                    pass

    def setPlugins(self):
        item = self.settingsDialog.ui.listWidget.currentItem()
        item.pluginEnabled = not item.pluginEnabled
        self.updatePluginMenu()
        if not config.has_section('Plugins'):
            config.add_section('Plugins')
        config.set('Plugins', item.name, str(item.pluginEnabled))
        config.write(open(config.file, 'w'))

    def updatePluginMenu(self):
        item = self.settingsDialog.ui.listWidget.currentItem()
        if item.pluginEnabled:
            self.settingsDialog.ui.updatePluginAction.setText(self.trUtf8('Disable'))
        else:
            self.settingsDialog.ui.updatePluginAction.setText(self.trUtf8('Enable'))

    def selectBackend(self):
        backend = backends[str(self.notebookDialog.ui.backends.currentText().toUtf8())]
        for i in (self.notebookDialog.ui.path, self.notebookDialog.ui.pathEdit):
            i.setHidden(not backend.path)
            self.notebookDialog.settings[self.notebookDialog.ui.pathEdit] = backend.path
        for i in (self.notebookDialog.ui.url, self.notebookDialog.ui.urlEdit):
            i.setHidden(not backend.url)
            self.notebookDialog.settings[self.notebookDialog.ui.urlEdit] = backend.url
        for i in (self.notebookDialog.ui.login, self.notebookDialog.ui.loginEdit):
            i.setHidden(not backend.login)
            self.notebookDialog.settings[self.notebookDialog.ui.loginEdit] = backend.login
        for i in (self.notebookDialog.ui.passwd, self.notebookDialog.ui.passwdEdit):
            i.setHidden(not backend.passwd)
            self.notebookDialog.settings[self.notebookDialog.ui.passwdEdit] = backend.passwd

        self.notebookDialog.ui.desc.setText(self.trUtf8(backend.desc))
        self.notebookDialog.adjustSize()

    def setNotebook(self, notebook, fr=False):
        if not fr:
            previous = self.notebook.name

        try:
            self.notebook = Notebook(notebook)
            config.setDefault(notebook)
            self.parameter = [self.notebook.notes]
            self.display(self.parameter)
        except Exception, err:
            print err
            self.showMessage(str(err))
            if not fr:
                self.setNotebook(previous, fr)
            else:
                config.addNotebook('Default', 'FileSystem', 'Wiki', [os.path.expanduser('~/.notes')])
                self.setNotebook('Default', fr)

        for i in self.writeActions: i.setVisible(not self.notebook.backend.ReadOnly)
        for i in self.wikiActions: i.setVisible(self.notebook.Wiki)

        self.mainWindow.ui.dateEdit.setVisible(self.notebook.backend.Date)
        self.mainWindow.ui.menuTag.setEnabled(self.notebook.backend.Tag)
        self.mainWindow.ui.actionOpenExternally.setVisible(self.notebook.backend.URL)

        if not fr:
            if self.settings['Bool']['Sessions']:
                self.settings['List']['Session'] = []

                self.saveSession()

    def closeTab(self):
        tab = self.mainWindow.ui.tabWidget.currentIndex()

        if self.settings['Bool']['Sessions']:
            try:
                self.settings['List']['Session'].remove(self.mainWindow.ui.tabWidget.currentWidget().note)
                self.saveSession()
            except:
                pass
        
        if tab != 0: self.mainWindow.ui.tabWidget.removeTab(tab)

    def showHide(self, reason):
        if reason == Qt.QSystemTrayIcon.Trigger:
            if self.mainWindow.isHidden():
                self.mainWindow.show()
                self.mainWindow.activateWindow()
            else:
                self.mainWindow.hide()

    def showMessage(self, message):
        self.messageDialog.ui.message.setText(unicode(message, 'utf'))
        self.messageDialog.show()

    def refresh(self):
        self.mainWindow.ui.metaList.clear()
        self.copyDialog.ui.notebooks.clear()

        notebooks = config.getNotebooks()
        notebooks.sort()

        if not len(notebooks) == 1:
            for i in notebooks:

                backend = config.getBackend(i)
    
                if self.settings['Bool']['BackendIcons']: icon = self.backendIcons[backend]
                else: icon = ':/icons/%s/notebook.png' % (self.settings['String']['Icons'])

                item = Qt.QListWidgetItem(Qt.QIcon(icon), unicode(i, 'utf'), self.mainWindow.ui.metaList)
                if not i == self.notebook.name and not backends[backend].ReadOnly:
                    Qt.QListWidgetItem(Qt.QIcon(icon), unicode(i, 'utf'), self.copyDialog.ui.notebooks)
                item.setToolTip(self.trUtf8('Backend: %s' % backend))
                item.type = 'notebook'
                
                if i == self.notebook.name:
                    item.setFont(self.boldFont)

        self.mainWindow.ui.dateEdit.setDate(Qt.QDate.currentDate())

        dates = self.notebook.dates()
        dates.sort()

        if self.settings['Bool']['Dates']:
            for i in dates:
                item = Qt.QListWidgetItem(Qt.QIcon(':/icons/%s/date.png' % (self.settings['String']['Icons'])), unicode(i, 'utf'), self.mainWindow.ui.metaList)
                item.type = 'date'

        tags = self.notebook.tags()
        tags.sort()

        for i in tags:
            item = Qt.QListWidgetItem(Qt.QIcon(':/icons/%s/tag.png' % (self.settings['String']['Icons'])), unicode(i, 'utf'), self.mainWindow.ui.metaList)

            notes = self.notebook.byTag(i)
            item.setToolTip(unicode('Notes (%i): %s' % (len(notes), ', '.join(notes)), 'utf'))
            item.type = 'tag'

        for i in self.settings['List']['Searches']:
            item = Qt.QListWidgetItem(Qt.QIcon(':/icons/%s/search.png' % (self.settings['String']['Icons'])), unicode(i, 'utf'), self.mainWindow.ui.metaList)
            item.type = 'search'
        
        # Displaying entries
        self.display(self.parameter)

        # Adding search completer items
        if self.settings['Bool']['SearchCompletion']:
            self.completer = Qt.QCompleter(['tag:' + unicode(i, 'utf') for i in tags] \
            + ['date:' + unicode(i, 'utf') for i in dates])
            self.mainWindow.ui.searchEdit.setCompleter(self.completer)

        # Refreshing summary
        status = unicode('Today is %s  Tags: %i  Notes: %i' % \
        ('%d-%d-%d' % localtime()[:3],  len(tags), len(self.notebook.notes())), 'utf')
        self.mainWindow.ui.statusbar.showMessage(status)
        self.tray.setToolTip(status)

    def openMeta(self, item):
        if item.type == 'tag':
            self.parameter = [self.notebook.byTag, str(item.text().toUtf8())]
            self.display(self.parameter)
            desc = self.parameter[1]
        elif item.type == 'date':
            self.parameter = [self.notebook.byDate, str(item.text().toUtf8())]
            self.display(self.parameter)
            desc = self.parameter[1]
        elif item.type == 'search':
            i = item.text()
            self.search(i)
            desc = str(i.toUtf8())
        elif item.type == 'notebook':
            name = str(item.text().toUtf8())
            try:
                self.setNotebook(name)
                self.parameter = [self.notebook.notes]
                self.refresh()
                desc = 'All'
            except Exception, err:
                self.showMessage(str(err))
        
        self.mainWindow.ui.tabWidget.setTabText(0, unicode('%s > %s' % (self.notebook.name, desc), 'utf'))
    
    def openDate(self):
        date = self.mainWindow.ui.dateEdit.date()
        self.parameter = [self.notebook.byDate, str(date.year()) + '-' + str(date.month()) + '-' + str(date.day())]
        self.display(self.parameter)
    
    def today(self):
        self.parameter = [self.notebook.byDate, '%d-%d-%d' % localtime()[:3]]
        self.display(self.parameter)
    
    def findRelated(self):
        if len(self.selectedNotes()) == 1:
            self.parameter = [self.notebook.related, self.currentNote()]
            self.display(self.parameter)
    
    def backlinks(self):
        if len(self.selectedNotes()) == 1:
            self.parameter = [self.backlinks, self.currentNote()]
            self.display(self.parameter)
    
    def search(self, text = None):
        if text is None:
            text = self.mainWindow.ui.searchEdit.text()
        self.parameter = [self.notebook.search, str(text.toUtf8()).split(' ')]
        self.display(self.parameter)

    def refreshMenu(self):
        item = self.mainWindow.ui.metaList.currentItem()
        self.mainWindow.ui.actionDeleteNotebook.setVisible(item.type == 'notebook')
        self.mainWindow.ui.actionDeleteTag.setVisible(item.type == 'tag')
        self.mainWindow.ui.actionDeleteSelectedSearch.setVisible(item.type == 'search')   

    def display(self, parameter):
        if len(self.parameter) == 1: entries = self.parameter[0]()
        else: entries = self.parameter[0](self.parameter[1])
        
        self.mainWindow.ui.notesList.clear()
        
        self.mainWindow.ui.numberLabel.setText(self.trUtf8("%i result(s)" % (len(entries))))
        
        for i in entries:
            try:
                item = Qt.QListWidgetItem(Qt.QIcon(':/icons/%s/note.png' % (self.settings['String']['Icons'])), unicode(i, 'utf'), self.mainWindow.ui.notesList)
                
                if self.settings['Bool']['Tooltips']:
                    text = self.notebook.get(i)
                    if self.notebook.markup == 'Wiki': 
                        html = text2html(unicode(text, 'utf'))
                    else: 
                        html = text

                    item.setToolTip(unicode('Title: %s<br>Date: %s<br>Tags: %s<br>Text: %s<br>Length: %i characters' \
                    % (i, self.notebook.noteDate(i), ', '.join(self.notebook.noteTags(i)), html, len(text)), 'utf'))
            except:
                pass
    
    def new(self, name=None, text=None):
        if self.mainWindow.isHidden():
            self.mainWindow.show()
        tab = EditorWidget(self)
        tab.ui.nameEdit.setEnabled(True)

        tab.key = None

        if name is None:
            name = 'New note %s' % (datetime.strftime(datetime.today(), '%Y-%m-%d %H-%M-%S'))
        if not text is None:
            tab.ui.textEdit.setText(unicode(text, 'utf'))
    
        for i in (tab.ui.tagEdit,tab.ui.tagsList, tab.ui.addTagButton,tab.ui.delTagButton, tab.ui.autoTagButton):
            i.setHidden(not self.notebook.backend.Tag)

        if self.parameter[0] == self.notebook.byTag:
            tab.addTag(self.parameter[1])
    
        tab.ui.nameEdit.setText(unicode(name, 'utf'))
        tab.ui.date.setText('%d-%d-%d' % localtime()[:3])
        self.mainWindow.ui.tabWidget.addTab(tab, name)
        self.mainWindow.ui.tabWidget.setCurrentIndex(self.mainWindow.ui.tabWidget.indexOf(tab))
        self.mainWindow.ui.tabWidget.setTabIcon(self.mainWindow.ui.tabWidget.indexOf(tab), Qt.QIcon(':/icons/%s/note.png' % (self.settings['String']['Icons'])))
        tab.ui.nameEdit.setFocus()
    
    def openNote(self, entry):
        if self.mainWindow.isHidden():
            self.mainWindow.show()
            
        tab = EditorWidget(self)
    
        # Open preview mode by default
        tab.ui.tabWidget.setCurrentIndex(0)
    
        # Disabling namebar
        tab.ui.nameEdit.setEnabled(False)
    
        # Setting name
        tab.ui.nameEdit.setText(unicode(entry, 'utf'))
    
        # Creating Note instance
        tab.note = entry
        tab.ui.date.setText(self.trUtf8(self.notebook.noteDate(entry)))

        if entry in config.options('Encrypted'):
            key = str(Qt.QInputDialog.getText(self.mainWindow, 'Enter key', 'Key: ', Qt.QLineEdit.Password)[0].toUtf8())
        else:
            key = None

        try:
            text = self.notebook.get(entry, key)

            tab.key = key

            tab.ui.textEdit.setPlainText(unicode(text, 'utf'))
    
            # Displaying tags
            for i in (tab.ui.tagEdit, tab.ui.tagsList, tab.ui.addTagButton, tab.ui.delTagButton, tab.ui.autoTagButton):
                i.setHidden(not self.notebook.backend.Tag)
    
            if self.notebook.backend.Tag:
                for tag in self.notebook.noteTags(entry):
                    tab.addTag(tag)
    
            self.mainWindow.ui.tabWidget.addTab(tab, '')
            self.mainWindow.ui.tabWidget.setCurrentIndex(self.mainWindow.ui.tabWidget.indexOf(tab))
            self.mainWindow.ui.tabWidget.setTabText(self.mainWindow.ui.tabWidget.indexOf(tab), unicode(entry, 'utf'))
            self.mainWindow.ui.tabWidget.setTabIcon(self.mainWindow.ui.tabWidget.indexOf(tab), Qt.QIcon(':/icons/%s/note.png' % (self.settings['String']['Icons'])))

            if self.settings['Bool']['Sessions']:
                if not entry in self.settings['List']['Session']:
                    self.settings['List']['Session'].append(entry)

                    self.saveSession()

        except Exception, err:
            self.showMessage(str(err))



        # If search was performed:
        if self.parameter[0] == self.notebook.search:
            if len(self.parameter[1]) == 1:
                searchtext = self.trUtf8(self.parameter[1][0])
                tab.ui.searchEdit.setText(searchtext)
                tab.find(searchtext)
    
    def saveNote(self):
        tab = self.mainWindow.ui.tabWidget.currentIndex()
        if tab != 0: 
            widget = self.currentWidget()
            text = str(widget.ui.textEdit.toPlainText().toUtf8())
            tags = widget.tags()

            if not hasattr(widget, 'note'):
                widget.note = str(widget.ui.nameEdit.text().toUtf8())
                self.mainWindow.ui.tabWidget.setTabText(self.mainWindow.ui.tabWidget.indexOf(widget), unicode(widget.note, 'utf'))

            try:
                self.notebook.add(widget.note, text, widget.key)
                self.notebook.tag(widget.note, tags)
                self.refresh()
                widget.ui.nameEdit.setEnabled(False)
                widget.refresh()

                if self.settings['Bool']['Sessions']:
                    if not widget.note in self.settings['List']['Session']:
                        self.settings['List']['Session'].append(widget.note)

                        self.saveSession()
            
            except Exception, err:
                self.showMessage("Can't save entry:\n<b>%s</b>" % (str(err)))

    def buildListIndex(self):
        self.new(text='\n'.join(["* [[" + i + "]]" for i in self.selectedNotes()]))
    
    def merge(self):
        self.new(text='\n----\n'.join(["[[" + note + "]]\n\n" + self.notebook.get(note) for note in self.selectedNotes()]))
    
    def currentNote(self):
        index = self.mainWindow.ui.notesList.currentRow()
        item = self.mainWindow.ui.notesList.item(index)
        if not item is None:
            return str(item.text().toUtf8())
    
    def openFromList(self):
        self.openNote(self.currentNote())
    
    def selectedNotes(self):
        return ([str(item.text().toUtf8()) for item in self.mainWindow.ui.notesList.selectedItems()])
    
    def email(self):
        if len(self.selectedNotes()) == 1:
            name = self.currentNote()
            if not name is None:
                Qt.QDesktopServices.openUrl(Qt.QUrl(unicode('mailto:?subject=%s&body=%s' % (name, self.notebook.get(name)), 'utf')))

    def openExternally(self):
        if len(self.selectedNotes()) == 1:
            name = self.currentNote()
            if not name is None:
                Qt.QDesktopServices().openUrl(Qt.QUrl(unicode(self.notebook.url(name), 'utf')))
    
    def deleteNotes(self):
        if not config.has_section('Encrypted'):
            config.add_section('Encrypted')
            
        for note in self.selectedNotes():
            self.notebook.delete(note)
            if note in config.options('Encrypted'):
                config.remove_option('Encrypted', note)

        config.write(open(config.file, 'w'))
        self.refresh()
   
    def renameNote(self):
        if len(self.selectedNotes()) == 1:
            c = self.currentNote()

            if not config.has_section('Encrypted'):
                config.add_section('Encrypted')

            name = str(self.renameDialog.ui.lineEdit.text().toUtf8())
            if name != '' and not name in self.notebook.notes():
                self.notebook.rename(c, name)

                if c in config.options('Encrypted'):

                    config.remove_option('Encrypted', c)
                    config.set('Encrypted', name, 'Yes')

                    config.write(open(config.file, 'w'))

                self.refresh()
        else:
            self.showMessage('Only 1 note can be renamed at a time')

    def encrypt(self):
        key = str(self.cryptDialog.ui.keyEdit.text().toUtf8())

        if not config.has_section('Encrypted'):
            config.add_section('Encrypted')

        for i in self.selectedNotes():
            self.notebook.add(i, self.notebook.get(i), key)
            config.set('Encrypted', i, 'Yes')

        config.write(open(config.file, 'w'))

    def decrypt(self):
        self.decryptDialog.show()
        return str(self.decryptDialog.ui.keyEdit.text().toUtf8())

    def copyEntry(self):
        move = self.copyDialog.ui.deleteBox.isChecked()
        for note in self.selectedNotes():
            self.notebook.copy(note, [str(i.text().toUtf8()) for i in self.copyDialog.ui.notebooks.selectedItems()], move)
        self.refresh()

    def addNotebook(self):
        config.addNotebook(
            str(self.notebookDialog.ui.nameEdit.text().toUtf8()),
            str(self.notebookDialog.ui.backends.currentText().toUtf8()),
            str(self.notebookDialog.ui.markups.currentText().toUtf8()),
            [str(i.text().toUtf8()) for i in
                (
                self.notebookDialog.ui.pathEdit,
                self.notebookDialog.ui.urlEdit,
                self.notebookDialog.ui.loginEdit,
                self.notebookDialog.ui.passwdEdit
                )
                if self.notebookDialog.settings[i]
             ]
        )
        self.refresh()
    
    def deleteNotebook(self):
        notebook = str(self.mainWindow.ui.metaList.currentItem().text().toUtf8())
        if not notebook == self.notebook.name:
            config.deleteNotebook(notebook)
            self.refresh()
        else:
            self.showMessage('This notebook is active now')

    def addTag(self):
        tag = str(self.addTagDialog.ui.lineEdit.text().toUtf8())
        if tag != '' and not tag in self.notebook.getTags():
            self.notebook.addTag(tag)
            self.refresh()
    
    def deleteTag(self):
        self.notebook.deleteTag(str(self.mainWindow.ui.metaList.currentItem().text().toUtf8()))
        self.refresh()
    
    def showAll(self):
        self.parameter = [self.notebook.notes]
        self.display(self.parameter)
    
    def saveSearch(self):
        if not config.has_section('UI'):
            config.add_section('UI')

        s = str(self.mainWindow.ui.searchEdit.text().toUtf8())
        if (s != '') and (not s in self.settings['List']['Searches']):
            self.settings['List']['Searches'].append(s)
            config.set('UI', 'Searches', '|||'.join(self.settings['List']['Searches']))
            config.write(open(config.file, 'w'))
            self.refresh()

    def deleteSearch(self):
        if not config.has_section('UI'):
            config.add_section('UI')

        s = str(self.mainWindow.ui.metaList.currentItem().text().toUtf8())
        self.settings['List']['Searches'].remove(s)
        config.set('UI', 'Searches', '|||'.join(self.settings['List']['Searches']))
        config.write(open(config.file, 'w'))
        self.refresh()

    def currentWidget(self):
        return self.mainWindow.ui.tabWidget.currentWidget()

    def getSelection(self):
        return self.currentWidget().ui.textEdit.textCursor().selectedText()

    def insertMarkup(self, ft, et, text=None):
        if not self.mainWindow.ui.tabWidget.currentIndex() == 0:
            if text is None:
                text = self.getSelection()
            self.currentWidget().ui.textEdit.insertPlainText(ft + text + et)
    
    def bold(self):
        if self.notebook.markup == 'Wiki':
            ft = et = '**'
        else:
            ft = '<b>'
            et = '</b>'
        self.insertMarkup(ft, et)

    def italic(self):
        if self.notebook.markup == 'Wiki':
            ft = et = '//'
        else:
            ft = '<i>'
            et = '</i>'
        self.insertMarkup(ft, et)
    
    def underline(self):
        if self.notebook.markup == 'Wiki':
            ft = et = '__'
        else:
            ft = '<u>'
            et = '</u>'
        self.insertMarkup(ft, et)
    
    def highlight(self):
        if self.notebook.markup == 'Wiki':
            ft = et = '%%'
        else:
            ft = '<span style="background: yellow;">'
            et = '</span>'
        self.insertMarkup(ft, et)
   
    def image(self):
        fileDialog = Qt.QFileDialog()
        fileDialog.setWindowTitle(self.trUtf8('Select image'))
        fileDialog.setFileMode(fileDialog.ExistingFile)
        fileDialog.setAcceptMode(fileDialog.AcceptOpen)
        fileDialog.exec_()
        path = fileDialog.selectedFiles()[0]
        
        if self.notebook.markup == 'Wiki':
            ft = '{{'
            et = '}}'
        else:
            ft = '<img src="'
            et = '">'
        self.insertMarkup(ft, et, path)

    def list(self):
        if self.notebook.markup == 'Wiki':
            ft = '* '
            et = ''
            fl = el = ''
        else:
            ft = '<li>'
            et = '</li>'
            fl = '<ul>'
            el = '</ul>'
        
        self.insertMarkup(fl, el, text=unicode('\n'.join([ft + i + et for i in str(self.getSelection().toUtf8()).split('\xe2\x80\xa9')]), 'utf'))
    
    def insertTime(self):
        self.insertMarkup('', '', datetime.strftime(datetime.today(), '%Y-%m-%d, %H:%M:%S'))

    def closeEvent(self, event):
        self.mainWindow.hide()
        event.ignore()

    def saveSizer(self):
        if not config.has_section('UI'):
            config.add_section('UI')
        
        l, r = self.mainWindow.ui.splitter.sizes()

        config.set('UI', 'SplitterLeft', l)
        config.set('UI', 'SplitterRight', r)

        config.write(open(config.file, 'w'))

    def saveSession(self):
        if not config.has_section('UI'):
            config.add_section('UI')

        config.set('UI', 'Session', '|||'.join(self.settings['List']['Session']))
        config.write(open(config.file, 'w'))   

    def run(self):
        self.mainWindow.show()
        sys.exit(self.application.exec_())
    
Application().run()
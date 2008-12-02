#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2007-2008 Simonenko Sergey <gforgx@gmail.com>
#       Copyright (C) 2008 Pavluhin Andrey <dr.onx@mail.ru>
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
#       * Neither the name of the project NoteFinder and author's name nor the names of 
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

import sys

from notefinderlib.notefinder import plugin, notefinder_rc
from PyQt4 import Qt

from notefinderlib.libnotetaking import *
from notefinderlib.creoleparser import text2html

css = "\
/* Copyright (c) 2008 Pavluhin Andrey <dr.onx@mail.ru> */\n\
body{\n\
        padding: 0px;\n\
        font-family:	verdana;\n\
        BORDER:		0px solid;}\n\
a{\n\
        TEXT-DECORATION: underline;\n\
        font-family:	verdana;\n\
        font-size:	12px;\n\
        color:		'#000000';}\n\
A:hover{\n\
	TEXT-DECORATION:	none;\n\
	color:	A3CF62;}\n\
h1{\n\
	font-size:	24;}\n"

class WebNotebook(plugin.Plugin):
    
    name = "WebNotebook"
    
    def __init__(self, parent):
        plugin.Plugin.__init__(self, parent)
        self.setText("Web Notebook")
        self.setToolTip("Create web notebook")
        self.setIcon(Qt.QIcon(':/icons/%s/export.png' % (self.app.settings['String']['Icons'])))
        self.addToTray()
   
    def do(self):
        # Show filechooser
        fileDialog = Qt.QFileDialog()
        fileDialog.setWindowTitle(self.trUtf8("Select path"))
        fileDialog.setFileMode(fileDialog.Directory)
        fileDialog.exec_()
        path = unicode(str(fileDialog.selectedFiles()[0].toUtf8()), 'utf').encode(sys.getfilesystemencoding())
        
        # Creating directories
        if not os.path.exists(os.path.join(path, "notes")):
            os.makedirs(os.path.join(path, "notes"))
        if not os.path.exists(os.path.join(path, "dates")):
            os.makedirs(os.path.join(path, "dates"))
        if not os.path.exists(os.path.join(path, "tags")):
            os.makedirs(os.path.join(path, "tags"))
        
        # Writing CSS
        open(os.path.join(path, "style.css"), 'w').write(css)
   
        # Creating index
        index = "<html>\n<head>\n<title>Web Notebook</title>\n\
            <link rel='stylesheet' type='text/css' href='style.css'>\n\
            <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
            </head>\n\
            <body>\n<h1>NoteFinder Web Notebook</h1>\n\
            <ul>\n<li><a href='all.html'>All entries</a></li>\n\
            <li><a href='dates.html'>Dates</a></li>\n\
            <li><a href = 'tags.html'>Tags</a></li>\n\
            </body></html>"
        open(os.path.join(path, "index.html"), 'w').write(index)
        
        # Creating notes
        for note in self.app.notebook.notes():
            date = self.app.notebook.noteDate(note)
            html = "<html>\n<head>\n<title>%s</title>\n\
                <link rel='stylesheet' type='text/css' href='../style.css'>\n\
                <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
                </head>\n\
                <body>\nDate: <a href = '../dates/%s.html'>%s</a>\n<br>\nTags: " % (note, date, date)
            for tag in self.app.notebook.noteTags(note):
                html += "<a href = '../tags/%s.html'>%s</a> " % (tag, tag)
            if self.app.notebook.markup == 'Wiki':
                htmlcode = text2html(unicode(self.app.notebook.get(note), "utf"))
            else:
                htmlcode = self.app.notebook.get(note)
            html += "<br>\n %s</body>\n</html>" % (htmlcode)
            open(os.path.join(path, "notes", note+".html"), 'w').write(html)
        
        # Creating dates
        dateIndex = "<html>\n<head>\n<title>Dates</title>\n\
            <link rel='stylesheet' type='text/css' href='style.css'>\n\
            <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
            </head>\n\
            <body>\n<ul>\n"
        for date in self.app.notebook.dates():
            dateIndex += "<li><a href = dates/%s.html>%s</a></li>\n" % (date, date)
            html = "<html>\n<head>\n<title>%s</title>\n\
                <link rel='stylesheet' type='text/css' href='../style.css'>\n\
                <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
                </head>\n\
                <body>\n<ul>\n" % (date)
            for note in self.app.notebook.byDate(date):
                html += "<li><a href = '../notes/%s.html'>%s</a></li>\n" % (note, note)
            html += "</ul>\n</body>\n</html>"
            open(os.path.join(path, "dates", date+".html"), 'w').write(html)
        dateIndex += "</ul>\n</body>\n</html>\n"
        open(os.path.join(path, "dates.html"), 'w').write(dateIndex)
        
        # Creating tags
        tagIndex = "<html>\n<head>\n<title>Tags</title>\n\
            <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
            <link rel='stylesheet' type='text/css' href='style.css'>\n\
            </head>\n\
            <body>\n<ul>\n"
        for tag in self.app.notebook.tags():
            tagIndex += "<li><a href = 'tags/%s.html'>%s</a></li>\n" % (tag, tag)
            html = "<html>\n<head>\n<title>%s</title>\n\
                <link rel='stylesheet' type='text/css' href='../style.css'>\n\
                <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
                </head>\n\
                <body>\n<ul>\n" % (tag)
            for note in self.app.notebook.byTag(tag):
                html += "<li><a href = '../notes/%s.html'>%s</a></li>\n" % (note, note)
            html += "</ul></body></html>"
            open(os.path.join(path, "tags", tag+".html"), 'w').write(html)
        tagIndex += "</ul>\n</body>\n</html>"
        open(os.path.join(path, "tags.html"), 'w').write(tagIndex)

      
        # Creating summary page
        all  = "<html>\n<head>\n<title>All entries</title>\n\
            <link rel='stylesheet' type='text/css' href='style.css'>\n\
            <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\n\
            </head>\n\
            <body>\n<ul>\n"
        for note in self.app.notebook.notes():
            all += "<li><a href = 'notes/%s.html'>%s</a></li>\n" % (note, note)
        all += "</ul>\n</body>\n</html>"
        open(os.path.join(path, "all.html"), 'w').write(all)
        
        self.showMessage("Done!<br>You can access your Web notebook <a href=%s>here</a>" % (os.path.join(path, "index.html")))
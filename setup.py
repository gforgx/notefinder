#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2007-2008 Simonenko Sergey <gforgx@gmail.com>
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
from setuptools import setup

# Variables
if sys.platform.startswith("win"): # If Windows
	shortcut = "share/NoteFinder.lnk"
	exec_dst = shortcut_dst = icon_dst = "C:\Program Files\NoteFinder"
else: # If something else
	shortcut = "share/notefinder.desktop"
	shortcut_dst = "share/applications"
	exec_dst = "bin"
	icon_dst = "share/notefinder"


setup(
        name = 'notefinder',
        # Install general stuff
	packages = ['notefinderlib', 'notefinderlib.libnotetaking', 'notefinderlib.libnotetaking.backends', 'notefinderlib.libmarkup', 'notefinderlib.libmarkup.engines', 'notefinderlib.creoleparser', 'notefinderlib.icalendar', 'notefinderlib.notefinder', 'notefinderlib.plugins'],
	py_modules = ['notefinderlib.p3'],
        data_files = [(shortcut_dst, [shortcut]), (exec_dst, ["notefinder", "NoteFinder.pyw", "Reminder.py"]), (icon_dst, ["share/icon.png"])],
        entry_points = {
            # Install plugins
            'notefinder.plugins': [
                'clipboard_capture = notefinderlib.plugins.clipboard_capture:ClipboardCapture',
                'web_notebook = notefinderlib.plugins.web_notebook:WebNotebook',
                'note_of_the_day=notefinderlib.plugins.note_of_the_day:NoteOfTheDay',
                'remove_empty = notefinderlib.plugins.remove_empty:RemoveEmpty',
		'remind = notefinderlib.plugins.remind:Remind',
            ],
        })

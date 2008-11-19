#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#       Copyright (C) 2007-2008 Simonenko Sergey <gforgx@lavabit.com>
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

import os

from notefinderlib.icalendar import Calendar, Journal, prop

class iCal(object):
    """ iCalendar backend """

    desc = 'iCalendar backend'
    
    ### SETTINGS DESCRIPTION ###
    path = True
    url = False
    login = False
    passwd = False

    ### FEATURE SET ###
    Tag = False
    ReadOnly = True
    URL = False

    def __init__(self, config, notebook):
        self.name = 'iCal'
        self.notebook = notebook

        self.path = config.get(self.name, self.notebook)

        # Raising exception if path is wrong
        if not os.path.exists(self.path):
            raise Exception("iCalendar file doesn't exist")
        
        if os.path.isdir(self.path):
            raise Exception("Specified path isn't an iCalendar file")

    def getNotes(self):
        return [str(i['SUMMARY']) for i in Calendar.from_string(open(self.path).read()).subcomponents]
    
    def getDates(self):
        dates = []
        for i in Calendar.from_string(open(self.path).read()).subcomponents:
            date = str(i['CREATED'].dt).split(' ')[0]
            if not date in dates:
                dates.append(date)
        return dates

    def getTags(self):
        return []

    def getURL(self, entry):
        pass

    def getNotesByDate(self, date):
        return [str(i['SUMMARY']) for i in Calendar.from_string(open(self.path).read()).subcomponents \
        if str(i['CREATED'].dt).split(" ")[0] == date]
    
    def getNotesByTag(self, tag):
        return []
    
    def getText(self, entry):
        for i in Calendar.from_string(open(self.path).read()).subcomponents:
            if str(i['SUMMARY']) == entry:
                text = prop.vText.from_ical(i['DESCRIPTION'].ical()).encode('utf8')
                break
        return text
    
    def getNoteDate(self, entry):
        for i in Calendar.from_string(open(self.path).read()).subcomponents:
            if str(i['SUMMARY']) == entry:
                date = str(i['CREATED'].dt).split(' ')[0]
                break
        return date

    def getNoteTags(self, entry):
        return []
    
    def noteExists(self, entry):
        return (entry in self.getNotes())
    
    def write(self, entry, text):
        pass

    def tag(self, entry, tags):
        pass

    def deleteNote(self, entry):
        pass
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

from poplib import POP3
from email import message_from_string
from email.header import decode_header
from email.iterators import typed_subpart_iterator

class Mail(object):
    """ Backend for using POP3 incoming e-mail """

    desc = 'Backend for using POP3 incoming e-mail'

    # Some e-mail parsing
    # http://ginstrom.com/scribbles/2007/11/19/parsing-multilingual-email-with-python

    ### SETTINGS DESCRIPTION ###
    path = False
    url = True
    login = True
    passwd = True

    ### FEATURE SET ###
    Tag = False
    ReadOnly = True
    URL = False

    def __init__(self, config, notebook):
        self.name = 'Mail'
        self.notebook = notebook
        
        server, login, pwd = config.get(self.name, self.notebook).split(';')
       
        # Creating client
        try:
            self.client = POP3(server)
            self.client.user(login)
            self.client.pass_(pwd)
        except:
            raise Exception('Failed to connect to POP3 server')

    def get_charset(self, message, default='ascii'):
        if message.get_content_charset():
            return message.get_content_charset()
        if message.get_charset():
            return message.get_charset()
        return default

    def get_body(self, message):
        if message.is_multipart():
            text_parts = [part for part in typed_subpart_iterator(message, 'text', 'plain')]
            body = []
            for part in text_parts:
                charset = self.get_charset(part, self.get_charset(message))
                body.append(unicode(part.get_payload(), charset, 'replace'))
            return u'\n'.join(body).strip()
        else:
            body = unicode(message.get_payload(decode=True), self.get_charset(message), 'replace')
            return body.strip()

    def getNotes(self):
        notes = []
        for i in xrange(len(self.client.list())):
            notes.append(
                u''.join([unicode(text, charset or 'ascii') for text, charset in
                decode_header(message_from_string('\n'.join(self.client.retr(i + 1)[1]))['subject'])]).encode('utf8'))
        return notes

    def getDates(self):
        return []

    def getTags(self):
        return []

    def getURL(self, entry):
        pass

    def getNotesByDate(self, date):
        return []

    def getNotesByTag(self, tag):
        return []

    def getText(self, entry):
        for i in xrange(len(self.client.list())):
            message = message_from_string('\n'.join(self.client.retr(i + 1)[1]))
            if u''.join([unicode(text, charset or 'ascii') for text, charset in
                decode_header(message['subject'])]).encode('utf8') == entry:
                return self.get_body(message).encode('utf8')

    def getNoteDate(self, entry):
        return ''

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
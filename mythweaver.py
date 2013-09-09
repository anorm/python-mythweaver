#!/usr/bin/env python
import md5
import requests
import sys
from lxml import etree

class MythWeaver:
    def login(self, username, password):
        self.session = requests.Session()
        phash=md5.new(password).hexdigest()
        url="http://www.myth-weavers.com/login.php?do=login"
        opts={
            'do':                       'login',
            'vb_login_username':        username,
            'vb_login_md5password':     phash,
            'vb_login_md5password_utf': phash,
            's':                        '',
            'security_token':           'guest'
        }
        response = self.session.post(url, data=opts)
        return response.cookies.get_dict().has_key('bbsessionhash')

    def downloadSheet(self, sheetid):
        url="http://www.myth-weavers.com/sheet.php"
        opts={
            'do':      'download',
            'sheetid': sheetid
        }
        response = self.session.post(url, data=opts)
        return etree.fromstring(response.content)


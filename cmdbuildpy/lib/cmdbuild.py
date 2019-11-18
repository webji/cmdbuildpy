#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import json, requests
from .util import Logger, API_VERSION, HTTP_METHOD

logger = Logger(__name__).get_logger()

class CMDBuild(object):

    def __init__(self, host: str, usename: str, password: str, version:API_VERSION=API_VERSION.V2):
        self.host = host
        self.username = usename
        self.password = password
        self.version = version
        self.session_id = None
       
    def __repr__(self):
        return f'<CMDBuild: host={self.host}, username={self.username}, password={self.password}, version={self.version}, session_id={self.session_id}>'

    def url(self, path):
        host = self.host.strip('/')
        path = path.strip()
        version = self.version
        return f'{host}/services/rest/{version}/{path}/'

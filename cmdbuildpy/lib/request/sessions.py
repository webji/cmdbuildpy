#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import requests, json

from cmdbuildpy.lib.util import HTTP_METHOD, API_VERSION, Logger
from cmdbuildpy.lib.model import Session
from cmdbuildpy.lib.cmdbuild import CMDBuild

from . import Request

logger = Logger(__name__).get_logger()

class Sessions(Request):
    path = 'sessions'

    def create(self) -> Session:
        session = Session(self.cmdbuild.username, self.cmdbuild.password)
        self.method = HTTP_METHOD.POST
        self.data = session.__dict__
        self.request()
        return self.get_session()


    def read(self, id: str) -> Session:
        self.method = HTTP_METHOD.GET
        self.path += f'/{id}'
        self.request()
        return self.get_session()


    def update(self, id: str, session: Session) -> Session:
        self.method = HTTP_METHOD.PUT
        self.path += f'/{id}'
        self.data = session.__dict__
        self.request()
        return self.get_session()


    def delete(self, id: str):
        self.method = HTTP_METHOD.DELETE
        self.path += f'/{id}'
        self.request()
    

    def get_session(self) -> Session:
        data = self.ret['data']
        self.validate_type(data, dict)
        return Session().from_dict(data)
        

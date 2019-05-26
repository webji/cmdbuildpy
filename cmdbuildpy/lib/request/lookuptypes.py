#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import requests, json

from cmdbuildpy.lib.util import HTTP_METHOD, API_VERSION, Logger
from cmdbuildpy.lib.model import LookupTypeDetail
from cmdbuildpy.lib.cmdbuild import CMDBuild

from . import Request

logger = Logger(__name__).get_logger()

class LookupTypes(Request):
    path = 'lookup_types'

    def read(self, id: str) -> LookupTypeDetail:
        self.method = HTTP_METHOD.GET
        self.path += f'/{id}'
        self.request()
        return self.get_lookuptypedetail()

    def read_all(self, active_only: bool = None, limit: int = None, start: int = None) -> list:
        self.method = HTTP_METHOD.GET
        self.params = {
            "active": active_only,
            "limit": limit,
            "start": start
        }
        self.request()
        return self.get_lookuptypedetails()

    def get_lookuptypedetail(self) -> LookupTypeDetail:
        data = self.validate_data_type(dict)
        return LookupTypeDetail().from_dict(data)
        
    def get_lookuptypedetails(self) -> list:
        data = self.validate_data_type(list)
        type_list = []
        for type_dict in data:
            type_basic = LookupTypeDetail().from_dict(type_dict)
            type_list.append(type_basic)
        return type_list

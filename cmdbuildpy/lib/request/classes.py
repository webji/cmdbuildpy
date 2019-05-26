#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import requests, json

from cmdbuildpy.lib.util import HTTP_METHOD, API_VERSION, Logger
from cmdbuildpy.lib.model import ClassWithBasicDetails, ClassWithFullDetails
from cmdbuildpy.lib.cmdbuild import CMDBuild

from . import Request

logger = Logger(__name__).get_logger()

class Classes(Request):
    path = 'classes'

    def read(self, id: str) -> ClassWithFullDetails:
        self.method = HTTP_METHOD.GET
        self.path += f'/{id}'
        self.request()
        return self.get_class()

    def read_all(self, active_only: bool = None, limit: int = None, start: int = None) -> list:
        self.method = HTTP_METHOD.GET
        self.params = {
            "active": active_only,
            "limit": limit,
            "start": start
        }
        self.request()
        return self.get_classes()

    def get_class(self) -> ClassWithFullDetails:
        data = self.validate_data_type(dict)
        return ClassWithFullDetails().from_dict(data)
        
    def get_classes(self) -> list:
        data = self.validate_data_type(data, list)
        class_list = []
        for class_dict in data:
            class_basic = ClassWithBasicDetails().from_dict(class_dict)
            class_list.append(class_basic)
        return class_list

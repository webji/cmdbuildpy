#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

from . import Request
# from cmdbuildpy.lib.model import Card, Values
from cmdbuildpy.lib.util import HTTP_METHOD

class ClassesAttributes(Request):
    path = 'classes'

    def read_all(self, classId: str, active: bool = None, limit: int = None, start: int = None):
        self.method = HTTP_METHOD.GET
        self.path += f'/{classId}/attributes'
        self.params = {
            'active': active,
            'limit': limit,
            'start': start
        }
        self.request()
        return self.get_attributes()


    def get_attributes(self):
        data = self.validate_data_type(list)

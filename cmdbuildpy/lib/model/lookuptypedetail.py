#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8

import json
from collections import OrderedDict

from cmdbuildpy.lib.util import Logger
from . import ModelWithStringId

logger = Logger(__name__).get_logger()

class LookupTypeDetail(ModelWithStringId):
    name: str = None
    parent: str = None

    def __repr__(self):
        return f'<Class: name={self.name}, parent={self.parent}, _id={self._id}>'


    
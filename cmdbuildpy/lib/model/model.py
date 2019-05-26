#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8

import json
from collections import OrderedDict
from decimal import Decimal
from datetime import datetime, date

from cmdbuildpy.lib.util import Logger

logger = Logger(__name__).get_logger()

class Model(object):
    pass

class ModelWithStringId(Model):
    _id: str

    def from_dict(self, args):
        for k, v in args.items():
            if v != None:
                setattr(self, k, v)
        return self

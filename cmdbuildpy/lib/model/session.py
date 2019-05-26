#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8

import json
from collections import OrderedDict
from decimal import Decimal
from datetime import datetime, date

from cmdbuildpy.lib.util import Logger
from . import ModelWithStringId

logger = Logger(__name__).get_logger()

class Session(ModelWithStringId):
    username: str
    password: str
    role: str
    availableRoles: []

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<Session: username={self.username}, password={self.password}, role={self.role}, availableRoles={self.availableRoles}, _id={self._id}>'



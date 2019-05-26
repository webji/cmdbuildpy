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

class ClassWithBasicDetails(ModelWithStringId):
    name: str = None
    description: str = None
    parent: str = None
    prototype: bool = None

    def __repr__(self):
        return f'<Class: name={self.name}, description={self.description}, parent={self.parent}, prototype={self.prototype}, _id={self._id}>'


class ClassWithFullDetails(ClassWithBasicDetails):
    descriptionAttributeName: str
    order: []

    
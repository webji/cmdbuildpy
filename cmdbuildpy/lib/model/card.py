#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8

from . import ModelWithStringId, Values

class Card(ModelWithStringId):
    values: Values

    def __repr__(self):
        return f'Card: values={self.values}'
        
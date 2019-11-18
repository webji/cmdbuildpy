#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8

from . import ModelWithStringId, Values

class Attribute(ModelWithStringId):
    type: str = None
    name: str = None
    description: str = None
    displayableInList: bool = None
    domainName: str = None
    unique: bool = None
    mandatory: bool = None
    # values: Values = None

    # def __init__(self):
    #     self.values = Values()

    # def __repr__(self):
    #     return f'<Card: values={self.values}>'

    # def as_dict(self):
    #     card_dict = self.__dict__.copy()
    #     card_dict['values'] = self.values.as_dict()
    #     return card_dict
        
#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8


import logging, logging.config
from enum import Enum

import pathlib

class Logger(object):
    def __init__(self, name):
        """
        :param name:    日志记录的用例名
        """
        logging.basicConfig(filename='logging.conf')
        self.logger = logging.getLogger(name)
        
    def get_logger(self):
        return self.logger


class NoEnum(Enum):
    def __repr__(self):
        return f'{self.__class__.__name__}.{self.value}'

    def __str__(self):
        return f'{self.value}'


class HTTP_METHOD(NoEnum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'

    def to_str(self):
        return self.__str__()

class API_VERSION(NoEnum):
    V1 = 'v1'
    V2 = 'v2'



if __name__ == "__main__":
    m = HTTPMETHOD.GET.to_str()

    b = isinstance(m, (str))
    print(f'{m} is str {b}')
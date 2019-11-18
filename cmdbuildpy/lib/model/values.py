#!/usr/bin/env python3
# Email: willji@outlook.com
# coding=utf-8

from . import Model

class Values(Model):
    delegate: dict = None

    def __repr__(self):
        return f'<Values: delegate={self.delegate}>'

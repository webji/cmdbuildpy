#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

import cmdbuildpy


setup(
    name='cmdbuildpy',
    version=cmdbuildpy.__VERSION__,

    description=cmdbuildpy.__DESCRIPTION__,
    long_description=long_description,

    url=cmdbuildpy.__URL__,

    author=cmdbuildpy.__AUTHOR__,
    author_email=cmdbuildpy.__EMAIL__,

    license=cmdbuildpy.__LISENCE__,

    classifiers=[
        'Programming Language :: Python :: 3.6',

        'License :: OSI Approved :: Apache Software License',

        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='CMDB CMDBuild API',

    packages=find_packages(exclude=['data', 'tests*']),

    install_requires=[],

    extras_require={},

    package_data={
        'cmdbuildpy': [
            'logging.conf',
        ],
    },

    test_suite='tests.all_suite',
)
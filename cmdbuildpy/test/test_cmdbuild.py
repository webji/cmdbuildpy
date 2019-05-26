#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import unittest

from cmdbuildpy.lib.cmdbuild import CMDBuild
from cmdbuildpy.lib.client import Client
from cmdbuildpy.lib.util import Logger, API_VERSION

class CMDBuildTest(unittest.TestCase):

    def test_init(self):
        host = 'http://localhost:38080'
        username = 'admin'
        password = 'admin'
        version = API_VERSION.V2
        cmdbuild = CMDBuild(host, username, password, version)
        self.assertEqual(cmdbuild.host, host)
        self.assertEqual(cmdbuild.username, username)

if __name__ == "__main__":
    unittest.main()
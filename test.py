#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

from cmdbuildpy.lib.cmdbuild import CMDBuild
from cmdbuildpy.lib.request import Request
from cmdbuildpy.lib.util import Logger, API_VERSION
from cmdbuildpy.lib.client import Client
from cmdbuildpy.lib.model import Session

def cmdbuild():
    host = 'http://localhost:38080'
    username = 'admin'
    password = 'admin'
    version = API_VERSION.V2
    cmdbuild = CMDBuild(host, username, password, version)
    return cmdbuild


def main():
    cmdb = cmdbuild()
    client = Client(cmdb)
    client.connect()
    
    # sessions read
    # ret = client.sessions().read(id=cmdb.session_id)
    # print(ret)

    # classes read_all
    # ret = client.classes().read_all()
    # print(ret)

    # classes read
    # ret = client.classes().read(id='User')
    # print(ret)

    # lookuptypes read_all
    # ret = client.lookuptypes().read_all()
    # print(ret)

    # lookupttypes read
    # ret = client.lookuptypes().read(id='RFC priority')
    # print(ret)


if __name__ == "__main__":
    main()
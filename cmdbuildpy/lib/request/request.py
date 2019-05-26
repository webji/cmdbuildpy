#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

import requests, json

from cmdbuildpy.lib.util import HTTP_METHOD, API_VERSION, Logger
from cmdbuildpy.lib.model import Session
from cmdbuildpy.lib.cmdbuild import CMDBuild

logger = Logger(__name__).get_logger()

class Request(object):
    __headers = {
            'Content-type': 'application/json',
            'Accept': '*/*'
        }

    path: str = '/'
    method: HTTP_METHOD = HTTP_METHOD.GET
    params: list = None
    data: dict = None
    ret: any
    
    def __init__(self, host: str, username: str, password: str, version: API_VERSION = API_VERSION.V2):
        self.cmdbuild = CMDBuild(host, username, password, version)


    def __init__(self, cmdbuild: CMDBuild):
        self.cmdbuild = cmdbuild    

    def __json_data(self):
        try:
            if self.data is None:
                return self.data
            elif isinstance(self.data, dict):
                return json.dumps(self.data)
            else:
                json.load(self.data)
                return self.data
        except ValueError:
            raise ValueError("CMDBuild - ERROR: Data is not a valid JSON object")


    def __request(self):
        path = self.cmdbuild.url(self.path) 
        func = getattr(requests, self.method.value.lower())
        params = self.params
        data = self.__json_data()
        res = func(path, data=data, params=params, headers=self.headers)
        try:
            ret = res.json()
        except :
            ret = dict(errors=[dict(message=res.text)])

        self.ret = ret
        
        if res.status_code != 200:
            logger.error(f'Request: {self}, Response: {res}')
            res.raise_for_status()
        
        return self
  
    
    @property
    def headers(self):
        headers = self.__headers.copy()
        if self.cmdbuild.session_id != None:
            headers['CMDBuild-Authorization'] = self.cmdbuild.session_id
        return headers


    def request(self):
        return self.__request()

    
    def validate_type(self, data, *args):
        if not isinstance(data, *args):
            raise requests.RequestException(f'Not Valid types for {data} and {args}')
        

    def get_ret(self):
        return self.ret


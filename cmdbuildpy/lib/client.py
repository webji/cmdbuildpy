#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>


from .cmdbuild import CMDBuild
from .request import Sessions, Classes, ClassesCards, LookupTypes

class Client(object):
    
    def __init__(self, cmdbuild: CMDBuild):
        self.cmdbuild = cmdbuild

    def connect(self):
        self.cmdbuild.session_id = self.sessions().create()._id      

    def sessions(self):
        return Sessions(self.cmdbuild)
    
    def classes(self):
        return Classes(self.cmdbuild)

    def classes_cards(self):
        return ClassesCards(self.cmdbuild)

    def lookuptypes(self):
        return LookupTypes(self.cmdbuild)
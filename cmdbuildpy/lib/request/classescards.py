#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>

from . import Request
from cmdbuildpy.lib.model import Card, Values
from cmdbuildpy.lib.util import HTTP_METHOD

class ClassesCards(Request):
    path = 'classes'


    # TODO: fix the create issue, Only _id is created now
    def create(self, classId: str, card: Card) -> int:
        self.method = HTTP_METHOD.POST
        self.path += f'/{classId}/cards'
        self.data = card.as_dict()
        self.request()
        return self.get_card_id()


    def read_all(self, classId: str, filter: str = None, sort: str = None, limit: int = None, start: int = None, positionOf: set = None) -> list:
        self.path += f'/{classId}/cards'
        self.params = {
            "filter": filter,
            "sort": sort,
            "limit": limit,
            "positionOf": positionOf
        }
        self.request()
        return self.get_cards()


    def read(self, classId: str, cardId: str) -> Card:
        self.path += f'/{classId}/cards/{cardId}'
        self.request()
        return self.get_card()

    # TODO: fix the update issue, None is updated now
    def update(self, classId: str, cardId: str, card: Card):
        self.method = HTTP_METHOD.PUT
        self.path += f'/{classId}/cards/{cardId}'
        self.data = card.as_dict()
        self.request()
        
    def delete(self, classId: str, cardId: str):
        self.method = HTTP_METHOD.DELETE
        self.path += f'/{classId}/cards/{cardId}'
        self.request()


    def get_cards(self):
        data = self.validate_data_type(list)
        card_list = []
        for card_dict in data:
            card = Card()
            card.values.delegate = card_dict
            card_list.append(card)
        return card_list


    def get_card(self):
        data = self.validate_data_type(dict)
        card = Card()
        card.values.delegate = data
        return card
    
    def get_card_id(self):
        data = self.validate_data_type(int)
        return data

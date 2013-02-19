#!/usr/bin/python

import csv
from encoder import encode

class CompressedRegistry(object):
    __id_dict = { }
    __values_dict = { }

    def get_short_id(self, id):
        res = self.__id_dict.get(id)
        if res is None:
            res = encode(len(self.__id_dict))
            self.__id_dict[id] = res
        return res 
        
    def register_value(self, shortId, value):
        if shortId in self.__values_dict: return
        self.__values_dict[shortId] = value
    
    def get_values_dict(self):
        return self.__values_dict


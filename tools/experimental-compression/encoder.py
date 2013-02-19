#!/usr/bin/python

_charmap = [chr(i) for i in range(33, 127) if i != ord('"') and i != ord(',')]
_base = len(_charmap)

def encode(number):
    result = ''
    while True:
        result = _charmap[number % _base] + result;
        number = number // _base;
        if number == 0: break
    return result
    

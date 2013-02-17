#!/usr/bin/python

from helpers import *;

valuesDict = { } 

def extract_municipality(item, year):
    mid = item[1]
    name = item[0]
    if mid in valuesDict: return;
    item = [mid, name]
    valuesDict[mid] = item

foreach_budget_item(extract_municipality)
save_dimension_values('pbcz-municipalities.csv', ['municipality', 'name_cs'], valuesDict)


#!/usr/bin/python

import csv
from helpers import *

def main():
    classes = { } 
    foreach_budget_item(lambda item, year: extract_classes_from_item(classes, item))
    save_dimension_values('budget-classes.csv', ['budget_class', 'name_cs', 'parent'], classes)

def extract_classes_from_item(classes, item):
    register_class(classes, item[5], item[6], None)
    register_class(classes, item[7], item[8], item[5])
    register_class(classes, item[9], item[10], item[7])
    register_class(classes, item[11], item[12], item[9])


def register_class(classes, cid, name, parent):
    if cid in classes: return
    item = [cid, name, parent];
    classes[cid] = item
    # print 'Added new class: ', item

if __name__ == '__main__':
  main()

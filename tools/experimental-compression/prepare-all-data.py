#!/usr/bin/python

import csv
import os
import sqlite3 as sql
from helpers import *
from encoder import encode
from registry import CompressedRegistry

classes = CompressedRegistry()

municipalities = CompressedRegistry()
regionsDict = { }
countiesDict = { }
dbfile = resolve_path('data/amounts.db')

def main():
    print 'Extracting dimension values'
    foreach_budget_item(process_budget_item, first_file_only = True)
    save_dimension_values('budget-classes.csv', ['budget_class', 'name_cs', 'parent'], classes.get_values_dict())
    save_dimension_values('municipalities.csv', ['municipality', 'name_cs', 'region'], municipalities.get_values_dict())
    save_dimension_values('regions.csv', ['region', 'name_cs', 'parent'], regionsDict)
    save_dimension_values('counties.csv', ['county', 'name_cs'], countiesDict)
    print 'Extracting budgets to sqlite db'
    process_amounts()

def process_budget_item(item, year):
    extract_classes_from_item(item)
    extract_municipality(item)

### budget classes

def extract_classes_from_item(item):
    register_class(item[5], item[6], None)
    register_class(item[7], item[8], item[5])
    register_class(item[9], item[10], item[7])
    register_class(item[11], item[12], item[9])

def register_class(cid, name, parent):
    cid = classes.get_short_id(cid)
    if parent is not None:
        parent = classes.get_short_id(parent)
    item = [cid, name, parent];
    classes.register_value(cid, item)

### municipalities & regions

def extract_municipality(item):
    mid = municipalities.get_short_id(item[1])
    name = item[0]
    region_name = item[3]
    region_id = "okres#" + region_name
    county_name = item[4]
    county_id = "kraj#" + county_name

    municipalities.register_value(mid, [mid, name, region_id])
    register_region_entity(regionsDict, [region_id, "Okres " + region_name, county_id])
    register_region_entity(countiesDict, [county_id, county_name])

def register_region_entity(dict, item):
    id = item[0]
    if id in dict: return
    dict[id] = item

### amounts


def createdb(db):
    db.execute('CREATE TABLE data (Municipality STRING, class1 STRING, class2 STRING, class3 STRING, class4 STRING, year INT, amount BIGINT)')

def process_amount_item(db, item, year):
    db.execute('INSERT INTO data VALUES(?, ?, ?, ?, ?, ?, ?)',
       (municipalities.get_short_id(item[1]), # municipality
       classes.get_short_id(item[5]), classes.get_short_id(item[7]), classes.get_short_id(item[9]), classes.get_short_id(item[11]), # classes
       year,
       long(float(item[-1]))))

def dropdb(dbfile):
    try: os.remove(dbfile)
    except OSError: pass

def process_amounts():
    dropdb(dbfile)
    with sql.connect(dbfile) as db:
        createdb(db)
        foreach_budget_item(lambda item, year: process_amount_item(db, item, year))


if __name__ == '__main__':
  main()

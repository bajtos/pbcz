#!/usr/bin/python

import os
import sqlite3 as sql
from helpers import *

dbfile = resolve_path('data/amounts.db')

def createdb(db):
    db.execute('CREATE TABLE data (Municipality INT, class1 INT, class2 INT, class3 INT, class4 INT, year INT, amount BIGINT)')

def process_item(db, item, year):
    db.execute('INSERT INTO data VALUES(?, ?, ?, ?, ?, ?, ?)',
       (int(item[1]), # municipality
       int(item[5]), int(item[7]), int(item[9]), int(item[11]), # classes
       year,
       long(float(item[-1]))))

def dropdb(dbfile):
    try: os.remove(dbfile)
    except OSError: pass

dropdb(dbfile)
with sql.connect(dbfile) as db:
    createdb(db)
    foreach_budget_item(lambda item, year: process_item(db, item, year))


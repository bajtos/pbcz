#!/usr/bin/python

import csv
import glob

def foreach_budget_item(callback, first_file_only = False):
    data_files = glob.glob('data/*.csv')
    for df in data_files:
       foreach_item_in_file(df, callback)
       if (first_file_only): break
    
def foreach_item_in_file(fname, callback):
    print 'Processing file {0}'.format(fname)
    with open(fname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        reader.next()
        for row in reader:
            callback(row)


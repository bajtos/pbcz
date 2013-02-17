#!/usr/bin/python

import csv
import glob

def foreach_budget_item(callback, first_file_only = False):
    data_files = glob.glob('data/*.csv')
    for df in data_files:
       _foreach_item_in_file(df, callback)
       if (first_file_only): break
    
def _foreach_item_in_file(fname, callback):
    print 'Processing file {0}'.format(fname)
    with open(fname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        reader.next()
        for row in reader:
            callback(row)

def save_dimension_values(fname, column_names, valuesDict):
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(column_names)
        for key in sorted(valuesDict.keys()):
            writer.writerow(valuesDict[key])


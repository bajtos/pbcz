#!/usr/bin/python

import csv
import glob
import re
import os.path
import inspect

def resolve_path(path):
    thisdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    root = os.path.dirname(thisdir)
    return os.path.join(root, path)

def foreach_budget_item(callback, first_file_only = False):
    data_files = glob.glob(resolve_path('data/vsechna-data-*.csv'))
    for df in data_files:
       _foreach_item_in_file(df, callback)
       if (first_file_only): break
    
def _foreach_item_in_file(fname, callback):
    year = parse_year_from_filename(fname);
    print 'Processing file {0} (year {1})'.format(os.path.relpath(fname), year)
    with open(fname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        reader.next()
        for row in reader:
            callback(row, year)

def parse_year_from_filename(fname):
    return int(re.search('data-(\d+).csv$', fname).group(1))

def save_dimension_values(fname, column_names, valuesDict):
    with open(os.path.join(resolve_path('dspl'), fname), 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(column_names)
        for key in sorted(valuesDict.keys()):
            writer.writerow(valuesDict[key])


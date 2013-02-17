#!/usr/bin/python

import csv
import glob

def main():
    classes = { } 
    data_files = glob.glob('data/*.csv')
    for df in data_files:
       extract_classes(df, classes)
    # extract_classes(data_files[0], classes)
    save_classes(classes, 'data/pbcz-budget-classes.csv')

def extract_classes(fname, classes):
    print 'Processing file {0}'.format(fname)
    with open(fname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        reader.next()
        for row in reader:
            register_class(classes, row[5], row[6], None)
            register_class(classes, row[7], row[8], row[5])
            register_class(classes, row[9], row[10], row[7])
            register_class(classes, row[11], row[12], row[9])

def register_class(classes, cid, name, parent):
    if cid in classes: return
    item = [cid, name, parent];
    classes[cid] = item
    # print 'Added new class: ', item

def save_classes(classes, fname):
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['budget_class', 'name_cs', 'parent'])
        for key in sorted(classes.keys()):
            writer.writerow(classes[key])

if __name__ == '__main__':
  main()

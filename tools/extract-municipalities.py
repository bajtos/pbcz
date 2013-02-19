#!/usr/bin/python

from helpers import *;

municipalitiesDict = { }
regionsDict = { }
countiesDict = { }

def extract_municipality(item, year):
    mid = item[1]
    name = item[0]
    region_name = item[3]
    region_id = "okres#" + region_name
    county_name = item[4]
    county_id = "kraj#" + county_name

    register_entity(municipalitiesDict, [mid, name, region_id])
    register_entity(regionsDict, [region_id, "Okres " + region_name, county_id])
    register_entity(countiesDict, [county_id, county_name])

def register_entity(dict, item):
    id = item[0]
    if id in dict: return
    dict[id] = item


foreach_budget_item(extract_municipality, first_file_only = True)
save_dimension_values('municipalities.csv', ['municipality', 'name_cs', 'region'], municipalitiesDict)
save_dimension_values('regions.csv', ['region', 'name_cs', 'parent'], regionsDict)
save_dimension_values('counties.csv', ['county', 'name_cs'], countiesDict)


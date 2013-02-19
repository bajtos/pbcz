#!/bin/bash

cd $(dirname $0)/..

# FILTER="municipality IN (554782, 554821, 555134, 582786)"
FILTER=1

sqlite3 data/amounts.db <<EOF
.headers off
.mode csv
.output dspl/slice-budget-classes.csv
select 'budget_class', 'municipality', 'year', 'total_amount';
select class1 as class, municipality, year, sum(amount) from data where $FILTER group by municipality, class, year ORDER BY class, municipality, year;
select class2 as class, municipality, year, sum(amount) from data where $FILTER group by municipality, class, year ORDER BY class, municipality, year;
select class3 as class, municipality, year, sum(amount) from data where $FILTER group by municipality, class, year ORDER BY class, municipality, year;
select class4 as class, municipality, year, sum(amount) from data where $FILTER group by municipality, class, year ORDER BY class, municipality, year;
EOF

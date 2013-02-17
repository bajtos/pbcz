#!/bin/bash

sqlite3 data/amounts.db <<EOF
.headers off
.mode csv
.output data/budget_class_slice.csv
select 'class', 'municipality', 'year', 'amount';
select class1 as class, municipality, year, sum(amount) from data where municipality IN (554782, 554821, 555134, 582786) group by municipality, class, year ORDER BY class, municipality, year;
select class2 as class, municipality, year, sum(amount) from data where municipality IN (554782, 554821, 555134, 582786) group by municipality, class, year ORDER BY class, municipality, year;
select class3 as class, municipality, year, sum(amount) from data where municipality IN (554782, 554821, 555134, 582786) group by municipality, class, year ORDER BY class, municipality, year;
select class4 as class, municipality, year, sum(amount) from data where municipality IN (554782, 554821, 555134, 582786) group by municipality, class, year ORDER BY class, municipality, year;
EOF
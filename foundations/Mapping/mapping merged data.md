## Mapping Geocodeable Data

**AKA mapping some restaurants**

### Meet your data

It's the same data you used with the census, it's just in CSV form. Looks something like this:

|state|NAME|B19013_001E|
|---|---|---|
|01|Alabama|42934|
|02|Alaska|69014|
|04|Arizona|50752|
|05|Arkansas|40149|
|06|California|61632|
|08|Colorado|57685|
|09|Connecticut|69243|

You can find it at [census-median-income.csv](census-median-income.csv)

### Map your data

First, import the CSV the same way you did for the [mapping geocodeable data/restaurants](mapping geocodeable data.md) example. Does this map? No. Well, yes. Kind of? Try it out.

---

How I pulled the census data

```python
from census import Census
from us import states
import unicodecsv

c = Census("YOUR_KEY_HERE")
state_data = c.acs.state(('NAME', 'B19013_001E'), '*')

census_file = open('census-median-income.csv', 'wb')
fieldnames = state_data[0].keys()
writer = unicodecsv.DictWriter(census_file, fieldnames=fieldnames)
headers = dict((n,n) for n in fieldnames)
writer.writerow(headers)
for state in state_data:
    writer.writerow(state)
census_file.close()
```

**Notes:** I used the same API we covered in the Census classes. `unicodecsv` is a drop-in replacement for `csv` that works with unicode values, and DictWriter is a way of writing dictionaries to a csv.
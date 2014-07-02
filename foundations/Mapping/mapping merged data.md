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

### Merging files

Okay, so maybe we need to actually hook it up with some actual geographic data (e.g. a shapefile). First stop: **find the geographic file**. While you might have trouble tracking down SHP/KML files for watersheds, gang territory or arcane political districts, Google has luckily already [put many data sources into a useable format](https://support.google.com/fusiontables/answer/1182141?hl=en). 

Check out the US States fusion table. It's just what we need! If only you could tack on all of that income data...

**OH BUT YOU CAN!**

Keep the US States window open, and go back to your Median Income table. Select **File > Merge...**. Sometimes you'll be merging with a file you've uploaded into Fusion Tables via shpescape, but in this case it's a public Fusion Table. You can just paste the URL of the [US States fusion table](https://www.google.com/fusiontables/data?docid=17aT9Ud-YnGiXdXEJUyycH2ocUqreOeKGbzCkUw) into the field near the bottom. Click **Next** and give it a minute. Once the merged table+map is ready, click the link!

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
## Homework

[DroneStrea.am](http://dronestre.am) is a web API of United States drone strikes. Let's map them!

I went ahead and exported the contents of their API to a csv file located [here](strikes.csv). Make the following maps:

1) View the whole data as a heatmap

2) Only view drone strikes in Pakistan

3) We ask questions: only view drone strikes where children were killed

4) We're keeping things quiet: don't show drone strikes from Dande Darpa Khel

5) Color drone strikes in several categories based on the minimum numbers of people killed. What are the best numbers to make the buckets out of?

6) When you visit the info window, make it list the town, the country, the target, the number range of deaths, and include the link to a news article about the 

When you set the location column, you'll notice that you've got both a **latitude** and a **longitude**. How do you use *two columns* as a location instead of just one?

To make multiple maps, click the '+' on the top bar of the Fusion Table. Select 'add map'.

--------

If you'd like to know the code I used, it was...

```python
import urllib2
import json
import unicodecsv

response = urllib2.urlopen('http://api.dronestre.am/data')
data = response.read()
content = json.loads(data)
strikes_file = open('strikes.csv', 'wb')
fieldnames = content['strike'][0].keys()
writer = unicodecsv.DictWriter(strikes_file, fieldnames=fieldnames)
headers = dict((n,n) for n in fieldnames)
writer.writerow(headers)
for strike in content['strike']:
    writer.writerow(strike)
strikes_file.close()
```

**Notes:** You can see the format of the raw data at [http://api.dronestre.am/data](http://api.dronestre.am/data). `unicodecsv` is a drop-in replacement for `csv` that works with unicode values, and DictWriter is a way of writing dictionaries to a csv.
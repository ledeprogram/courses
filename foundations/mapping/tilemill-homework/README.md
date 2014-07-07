# TileMill Homework

## PLUTO Homework

[PLUTO](http://www.nyc.gov/html/dcp/html/bytes/applbyte.shtml#pluto) data is all sorts of fun - tax lots come with a lot of information. Download the MapPLUTO data for Manhattan and make a map of one of the following:

* Amount of office space in the building
* Amount of factory space in the building
* Number of residential units
* Year built
* Whether it's in a historic district or not
* Anything else that might be fun

> **Note:** You'll get a lot of files with your MapPLUTO download - the shapefile you're concerned with is the MNMapPLUTO.shp file.

## Evacuation Homework

Visit the NYC OpenData site and download the Hurricane Evacuation Centers dataset. Style it in TileMill (including hovers with addresses), upload it to MapBox, and add it to your existing hurricane evacuation centers map.

## Street Tree Homework

Rumor has it Manhattan has a lot of trees. But what are they all? Let's map it!

If you search the [NYC OpenData](https://nycopendata.socrata.com) site you'll be able to find a Street Tree Census of Manhattan. Examine the attributes table - it doesn't seem to list the species name, only some weird code.

Sometimes you join for *more data* as opposed to *geographic information*. How are you going to find the tree name? Fortunately for you, I massaged [this PDF of code-species mappings](http://www.nycgovparks.org/sub_your_park/trees_greenstreets/treescount/images/species_list.pdf) into [this csv](species-name.csv) (so you don't have to do the hard part). All you have to do is join the with the shapefile you find on the NYC OpenData and party down.

**Your mission:** Make a map that has a point for every tree. When you hover over the point, display the name of the tree species. Color code for maples, oaks, ash, pine, elm and linden trees.
# Point-in-Polygon for QGIS

Sometimes you have a bunch of points, and you want to map them into areas - like, say, restaurant reviews per zip code, or how many trees are in every census tract. There are two ways to do that!

## Type 1: Getting Counts

**Project One:** Download [nabes-shapefile.zip](https://github.com/ledeprogram/courses/raw/master/foundations/mapping/qgis/nabes-shapefile.zip) and [hotspots-shapefile.zip](https://github.com/ledeprogram/courses/raw/master/foundations/mapping/qgis/hotspots-shapefile.zip)

**Project Two:** Hop on over to [http://thematicmapping.org/downloads/world_borders.php](http://thematicmapping.org/downloads/world_borders.php) to grab a [shapefile of the world](http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip). Then let's grab the [strikes.csv](https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/mapping/qgis/strikes.csv) file from a while back. Let's see the number of drone strike per country.

`(+proj=lcc +lat_1=40.666667 +lat_2=41.033333 +lat_0=40.166667 +lon_0=-74 +x_0=299999.9999999811 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=us-ft +no_defs)`

## Type 2: Getting Averages/Etc

* First open the world borders shapefile in QGIS using `Add Vector Layer` (dots + lines icon)

* Then open the drone strikes csv - NOT USING `Add Vector Layer`!

* `Vector > Data Management Tools > Join Attributes by Location`

* Set Join Vector Layer to `strikes`

* [X] Take sumamry of insersecting features, and might as well select all of those

* [X] Only keep matching records
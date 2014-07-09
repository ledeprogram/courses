# Point-in-Polygon for QGIS

Sometimes you have a bunch of points, and you want to map them into areas - like, say, restaurant reviews per zip code, or how many trees are in every census tract. There are two ways to do that!

## Type 1: Getting Counts

Not yet

## Type 2: Getting Averages/Etc

Hop on over to [http://thematicmapping.org/downloads/world_borders.php](http://thematicmapping.org/downloads/world_borders.php) to grab a shapefile of the world. Then let's grab the [strikes.csv](https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/mapping/google-fusion-tables/strikes.csv) file from a while back. Let's see the average minimum deaths per drone strike per country.

* First open the world borders shapefile in QGIS using `Add Vector Layer` (dots + lines icon)

* Then open the drone strikes csv - **not using `Add Vector Layer`!

* `Vector > Data Management Tools > Join Attributes by Location`

* Set Join Vector Layer to `strikes`

* [X] Take sumamry of insersecting features, and might as well select all of those

* [X] Only keep matching records
## Building a Hurricane Evacuation Map

**AKA mapping a single shapefile with no extra data**

WNYC's [hurricane evacuation map](http://project.wnyc.org/news-maps/hurricane-zones/hurricane-zones.html) was a big, big deal during Hurricane Irene in 2011. The official NYC evacuation map had been pushed offline by too much traffic, and WNYC's version was many peoples' only resource to know whether they should flee their homes or not.

Despite the fact that it's very useful, it's also very easy to make. Using a [shapefile](http://en.wikipedia.org/wiki/Shapefile) and [Google Fusion Tables](https://drive.google.com) we're going to make the exact same map for Houson.

> **Sidenote**: In theory, we should be able to make the exact same map that John Keefe did using [this data here](https://data.cityofnewyork.us/Public-Safety/Hurricane-Evacuation-Zones/8zwp-5ant). Unfortunately the modern evacuation map doesn't import into Google Fusion Tables correctly. Our loss is Houston's gain, I guess!

## Downloading a Shapefile

You'll want to get your shapefile from [ohouston.org](http://data.ohouston.org/ro/dataset/hurricane-risk-area/resource/ad0e925e-4791-4d0b-9df7-2411aeb60a97).

We talked about Shapefiles a little bit during the census class, but the basic gist is that they're a collection of files that describe some sort of geography. They can illustrate everything from points to polygons and are widely used in the computers-mapping-stuff (GIS) world. When shapefiles are available about your data, be happy.

### Importing your Shapefile into Google Fusion Tables

Google Fusion Tables lets you import **CSV**, **XLS**, and a cousin of the shapefile called a **KML** file. Not shapefiles themselves, though! You'll need to use a tool to import them for you.

Visit [http://www.shpescape.com](http://www.shpescape.com). Choose 'shp 2 fusion tables', then authorize shpescape to manage your Fusion Tables.

You'll note it asks you for **a zip archive of one (or more) shapefiles for import into Google Fusion Tables**. This means **you can't just upload your shp files!** Typically shapefiles come as a collection of files - there's an shp (the map), a prj (the projection), a dbf (the associated data), and several more. If your Houston Hurricane Evacuation Map was automatically unzipped when you downloaded it, **re-zip it and upload it now**.

Now wait.

> You have two options, one to create a *Centroid Geometry* and one to create a *Simplified Geometry*. The latter creates a simplified version of your map, while the former marks the point right in the middle of each unit on your map. Say you had a map of states, *Centroid Geometry* would mark the center of each state. While it'll be useful later on for attaching labels to objects, we don't need it just yet.

You'll see the **Total Rows** that need to be inserted, and **Rows Processed** will slowly creep up. If you have a ton of total rows, it will process the rows 2000 at a time - don't worry, it isn't broken! After shpescape has  processed your rows, it will then start adding them to **Rows Inserted**. You'll need to wait for **Rows Inserted** to become equal to **Total Rows** - you'll often think it looks done because it's processed all the rows, but you're still waiting on the inserion. Click the link and you'll be taken to your Fusion Table.

### Styling your Fusion Table

Google Fusion Tables is a lot like Google Spreadsheets, but it's for visualizing, analyzing, and mapping data as opposed to editing it.

First thing to do is give your table a nice name - click up top and renamed it something like **Hurricane Evacuation Areas (Houston).

Next, let's take a look at our data. We've got a ton of columns relating to the geometry (including some KML), and one called **RA**. Risk Areas, maybe? It scales from 1 to 5, so it looks promising. Anyway, let's get to the fun stuff: click **Map of geometry**.

It doesn't look like much, but it's a map! As it stands, though, there's no difference between a Level 1 Evacuation Zone and a Level 5 Evacuation Zone. Time to make some style changes!

First, click 'Change feature styles...' on the left hand side. Our map is made out of **polygons**, and we want to change the color inside of them, so we should click **Fill color** under **Polygons**.

Let's start off setting a **Gradient**. Click the **Gradient tab** and click the radio button next to **Show a Gradient**. Since we want to base our coloring on the Risk Area field, select **RA** from the dropdown. Google Kindly informs you that it ranges from 1 to 5 (although, fair warning, this number is often wrong!).

Feel free to erase all but two of the colors to make a simple gradient, then click 'Save'.

Okay, let's be honest, we didn't do a great job. White shouldn't be the lowest-risk area! Go back in and change the colors to reflect a range from, say, 'danger' (red) to 'safe' (yellow). While you're at it, you can also change the **Border width** to 0 pixels to lose those thick grey lines and help your map melt into the background.

### Publishing Your Map

Once your map is all set, you'll want to Publish it for all to see. Under 'Map of Geometry', click **Publish...** and you'll get a window like this...

Uh oh, looks like a warning! Seems like our map is too **Private** for anyone else to see. Click **Change Visiblity** and change the access from **Private** to **Anyone with the link**. If you aren't publishing this and want anyone to be able to stumble across it via search, you can also choose **Public on the web**.

Now click **Done** and attempt to publish again. You can use the *Send a link in email or IM* address to give people access to the whole map, or *Paste HTML to embed in a website* to pop it onto web site that you have control over.
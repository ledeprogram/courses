Now that we've seen how easy to use Google Fusion Tables is, let's take a look at a tool that lets us put a little more design power in our hands: [Tilemill](https://www.mapbox.com/tilemill/). We'll be using it in conjunction with [MapBox](https://www.mapbox.com), which allows you to host maps.

# What's TileMill good for?

TileMill is stellar at *displaying* data, but not good for *dealing with data*. You'll need to spend some time massaging your information - joining shapefiles, calculating columns, all of that - in something like [QGIS](QGIS.md) before it's ready for TileMill. Once it's ready though, TileMill makes the design process a breeze!

TileMill is also great at exporting images of your maps to include in pieces, as well as making Google Maps-ish "slippy maps" that can feature hover effects.

> **Note:** TileMill does crash sometimes. It has a lot on its plate! If you notice TileMill being especially unresponsive, just close it and reopen it. You should be saving your work often enough that you won't actually lose anything.

## Hosting & Display

Slippy maps are [thousands and thousands of square tiles](https://www.mapbox.com/foundations/how-web-maps-work/) that are stitched together to make up a map. You've seen this when Google Maps loads tiles slowly - each part of your map at each zoom level is just another square tile!

One downside of using Tilemill is that *you've got to put your map tiles somewhere*. TileMill exports a format called MBTiles, which stands for MapBox tiles - [MapBox](https://www.mapbox.com) is the tile hosting company that created TileMill. They can host your MBTiles for you, but it [gets pricey quick](https://www.mapbox.com/plans/) although it might be worth it if you become a hot-shot maps person, or your maps don't get *too* wildly popular.

You can also convert MBTiles to raw tiles using [MBUtil](https://github.com/mapbox/mbutil), then put the tiles up on something like Amazon's [S3](http://aws.amazon.com/s3/). This method costs much much less, but you (a) lose the ability to use the heat hover stuff, and (b) need to learn a little bit of JavaScript to display maps on the web.

And if you're real fancy you can run a [TileStream](https://github.com/mapbox/tilestream) server on your server and host your tiles from there!

# Using TileMill

## 1) Getting the data

First things first: we need some data.

Remember when I said the NYC hurricane evacuation map was tough to import to Google Fusion Tables? Not because of file naming or anything, but because it ditched many of the polygons and left us missing several zones. TileMill won't leave us hanging, so let's start with that.

If you search on [NYC OpenData](https://nycopendata.socrata.com) you can find [hurricane evacuation zones](https://data.cityofnewyork.us/Public-Safety/Hurricane-Evacuation-Zones/8zwp-5ant). You'll want to click **Export** and select **Shapefile**, since we've learned that's the #1 best kind of geographic data.

## 2) Creating a new TileMill project

You've downloaded [TileMill](https://www.mapbox.com/tilemill/) by now, I hope. Open it up!

You'll be taken to a **Projects** tab with a few sample projects and a big button that says **New project**. Click that!

Set the filename as **nyc-hurricane-evac**, the name as **NYC Hurricane Evacuation Map** and add a description if you'd like.

**Include world layer and styles** gives you a rough outline of the continents and a little bit of water. I like keeping it in to make sure my data's showing up in the right spots, and then removing it later.

Click 'Add'

## 3) Adding Layers

Now you're back on the Projects page. Click **NYC Hurricane Evacuation Map** and let's get going!

When working on a TileMill project, the screen is split into two parts: the left is the **render** and the right are the **styles**.

Let's start by examining the render area!

Maps in TileMill (and everywhere else, really) are made up of **layers**. Click the bottom-left-most button in the render area - the one that looks like several sheets of paper.

You'll see that you currently have one layer: the countries. Let's add another one, the hurricane zones! Click **+ Add Layer**.

We'll be adding a file, so click **Browse** and track down your shapefile.

**ID** and **class** are used to style, but the defaults are fine. SRS determines the way [projections and coordinates](https://www.mapbox.com/tilemill/docs/manual/basics/) are dealt with, and you should leave it as Autodetect.

Click **Save & Style** to get a few default styles as your layer is added to the map.

...but where is it? It's small! NYC is nothing compared to the entire world. If it isn't open already, open up the layers popup again. You'll see **#nyhez**, that's your new layer. Click the magnifying class to 'Zoom to Extent' and fit the render window over the layer.

## 4) Styling layers

Great, it's there! Unfortunately it's very ugly, a real weird green. We'll change this by looking at the **style window** to the right.

Design in MapBox is done with a language called [CartoCSS](https://www.mapbox.com/carto/api/2.3.0/), which is a relative of CSS, which is used to style web pages. CartoCSS is both simple and powerful!

You'll notice after we added the layer we got something new on the right

```css
#nyhez {
  line-color:#594;
  line-width:0.65;
  polygon-opacity:1;
  polygon-fill:#ae8;
}
```

Lines and polygons and opacity and color, oh my! Seem familiar from Google Fusion Tables? It's close enough, just a little more legwork to get the design done.

### Opacity

First, these big green blobs are a little intense. Let's make them more transparent: `polygon-opacity`, perhaps? If `1` is fully opaque, `0.65` might be a better choice. Change it then press `Command+S` or click the `Save` button. Now it's a bit more transparent!

We'll be removing the layer underneath eventually and making the transparent layer sit on top of a *normal* map (aka a basemap). Otherwise this wouldn't be much use.

### Fill Color

Next up, that green color is ugly. `polygon-fill` is obviously the color that's being used to fill the polygon, so let's play around with it.

**HOLD UP A SEC**, what's `#ae8` even mean? It's what's known as a **hex color**, a set of red, green and blue colors encoded using hexadecimal (you count from 0-F instead of 0-9!).

What do you need to know about this? Not much, just use a [color picker](http://www.colorpicker.com) that gives you hex values!

I changed my color to `#FEF199` because that seemed pleasant enough. But do we want the whole map to be that yellow? No. Not at all.

### Conditionals

The real power in TileMill comes from **conditional styling**. This means that you can style different elements based on their attributes - kind of like how we put everything in buckets on Google Fusion Tables, but waaaay more powerful.

Open up the Layers popup again, and click the little tables-looking button next to `#nyhez`. It's a brief summary of the information hiding in the shapefile - looks like we have a field called `Zone` that's the hurricane evacuation zone, so we'll be styling with that.

We'll start from the bottom and work our way up. We'll create a red style for **Zone 0** by changing the `#nyhez` rule in the style pane to look like this:

```css
#nyhez {
  line-color:#594;
  line-width:1;
  polygon-opacity:0.65;
  polygon-fill:#FEF199;
  [Zone = '0'] {
    polygon-fill: #ff0000;
  }
}
```

Save your file and you'll see the result. Looks like it's already water! That's silly, you don't need to evacuate that at all.

How do we make it disappear? There might be other ways, but I always make it **completely transparent**. Change that `polygon-fill` line to `polygon-opacity: 0;` and see if it works!

Okay, now to deal with **Zone 1**. It'll probably be just a little higher than **Zone 0**, so it should be the most dangerous. Let's try making it red.

```css
#nyhez {
  line-color:#594;
  line-width:0.5;
  polygon-opacity:0.65;
  polygon-fill:#FEF199;
  [Zone = '0'] {
    polygon-opacity: 0;
  }
  [Zone = '1'] {
    polygon-fill: #ff0000;
  }
  [Zone = '2'] {
    polygon-fill: #ff3300;
  }
}
```

Save it, look at it, rejoice. Add styles for the remaining zones!

> **Note:** Notice how there are quotation marks around the `1` and `2`? That's because in the data they're strings. If you had numbers instead, you could use code like `Zone > 1`

**The Big Question**: Zones are 0, 1, 2, 3, 4, 5, 6, and X. What's X? Is it useful? What styles are you going to apply to it?

If you're looking for inspiration, some nice colors might be `#e75624`, `#f28523`, `#fbed30`, `#b9d431`, `#7ec34a`, `#129e7a`.

Now, get rid of some of those lines to clean up the borders a bit.

### Adding a Reference Layer

TileMill supposedly supports plugins, but there are really only a handful. One of the good ones, though, lets you put a *real map* below what you're working on.

First, click **Plugins** on the far left menu. Give it a while to load the list of plugins, then install `tilemill-reference-layer`. Once that's done head back to your project.

TileMill needs to know which map among all those in the world you'd like to use as the base map, and you set it by clicking the **wrench icon** in the upper right hand corner.

Near the bottom there's a field marked **Reference layer**. In theory we should be using one of our own maps, but you can set it to `examples.map-i86nkdio`, `examples.map-20v6611k` or `examples.map-cnkhv76j` to use different example basemaps that MapBox uses for instruction.

Click **Save** and head back.

Did you see that basemap flicker?! I did, but unfortunately the countries map is getting in the way. Let's remove it by pulling up the Layers popup and clicking the trash can next to `#countries`.

Save, and you'll notice the countries disappeared but your view is still being blocked. It's the default styles!

In the **style pane**, remove the styles both for `Map` and the leftover `#countries` ones.

Voila! You've got a beautiful map. The basemap won't go online with your layers (you'll see that in the uploading step), but it's incredibly useful to see how it's working out.

## 5) Putting your map online

We're going to do this the simple way: through MapBox.

First, create an account at [mapbox.com](http://www.mapbox.com).

Next, open up TileMill and click on the `Settings` tab on the far left. Click `Authorize` to give TileMill access to your MapBox account - this lets TileMill upload directly to the account without you having to use web forms or anything.

Now, go into your NYC Hurricane Evacuation Map project. Click `Export` in the upper right hand corner, then Upload.

The **render pane** turns into a tool that you use to select the area you want to export. Less area to export = smaller file size. Since your Starter plan on MapBox only gives you 50MB you'll need to be picky.

First, you'll notice a lack of *anything* on the screen. This is because **the basemap is not exportable**, you have to add that on later.

You also can't see any of your shapefiles because **we're zoomed all the way out**, and New York is pretty tiny on the world-scale. **How are we going to track down NYC?**

### A hacky-but-useful method to set your bounds

Go back to the style pane and make `line-width` set to `10` to make NYC stand out a *ton*. Go back to export, and keep zooming in until your content is well-framed.

Hold shift and click-and-drag across the area your content is in. This sets the **bounds**.

Click in the middle, this sets your **center**.

*Note: If it asks you something about deleting a point, just say yes. It's just talking about moving the center.*

Now, copy those values and save them somewhere: my center is `-73.9758,40.6963,10` and my bounds are `-74.2751,40.4637,-73.6846,40.9353`.

Now click `Cancel` and head back to your style pane. Change the `line-width` back to `0` and then attempt to upload again. This time, paste in your bounds and you'll see the area you need to zoom and pan into!

### Finishing your export

Under **Zoom** it'll currently say something scary like `66,503,160 tiles (100 GB+ reducing zoom level recommended)`. Let's reduce the zoom level!

You can see your current zoom level in the upper left hand corner of the map. I'm currently at 10, and no one needs to zoom out any further than that, so I'm going to change the left-hand Zoom slider to 10.

Now I'm apparently down to `66,503,149 tiles`! It's the higher zoom levels that really take up the most space.

Zoom in a few more times to see what you feel is comfortable - 13 or 14 seems good to me. Slide the right-most slider under Zoom to this number. I set it to 14 and now I'm down to `1,123 tiles (1 MB+)`. Sounds good to me!

You can ignore MetaTile size, and feel free to add a version for your map or attribution for your data.

When you're all set, click `Upload`. You'll be taken to the **Exports** screen, and TileMill will give you an estimate for how long it's going to take to export and upload the files. If it gives you something crazy like a hundred hours or several days, **you probably forgot to set your bounds or zoom level correctly**.

Once it's done uploading, click **View**. Tada! It's on the internet! ...Kind of.

## 6) Actually making a map of it.

When we made that map, we didn't actually make a *whole map*, we just made a *layer*. A "real" map takes a basemap and overlays layers on top of it, kind of like in TileMill.

To set up an actual map we'll want to go to [https://www.mapbox.com/][https://www.mapbox.com/]. Sign in with your account.

Click **Projects** and then **+ Create Project**.

> I know it might be confusing that we're setting up *two* projects, but think of the TileMill project as one part of project, and the MapBox project as the publishable piece.

Now we're looking at a map. Zoom in on New York!

Click **Data**. If you didn't feel like being a cool shapefiles-friendly developer, you could start using their **Marker**, **Line** and **Polygon** tools to draw on the map. But hey, we're badasses! Click the three-bars icon to the right and change the switch from **features** to **layers**.

Click **+ Add Layers** and select your Hurricane Map.

INCREDIBLE. **WE ARE AMAZING, FREAKING LOOK AT THAT.**

*Note: If you wanted to add other layers, you can do that, too! They all just go on top of one another, which is why opacity can be important.*

### Styling the basemap

But maybe we don't like that basemap style? No sweat! Changing the basemap is way easy.

First, click **Style**. There are a *ton* of totally overwhelming options, but there's a great way to ignore them: click `X Discard palette`.

Now you're presented with a series of presets - by clicking each of them, along with **Basic**, **Accent** and **Bold** you've got a practically-limitless set of auto-generated, rather-pleasant-looking basemaps.

## 7) Saving and Publishing

Once you've got your map styles down, click **Save** to save the project (obvs). Now you can publish it!

Select **Project**. First select **Settings** and give your map a good name and description. Then head back to the **Info** page.

#### There are a few different ways to share a map.

First, you could send people right to it. That's the `Share` link. Easy! For example, mine is `https://a.tiles.mapbox.com/v4/jsoma.imjpp25d/page.html?access_token=pk.eyJ1IjoianNvbWEiLCJhIjoibFJmYl9JWSJ9.AUm8d76cbOvVEn2mMeG_ZA#11/40.6851/-73.9076`

> **Note:** You'll be linking to the exact coordinates and zoom level that you're viewing. You'll probably want to zoom out and frame everything nicely before taking that link.

Next, you can embed it in a web page, just like, say, a YouTube video. That's where you take the `iframe` code. This works great for WordPress installs and the like. My embed code is

```html
<iframe width='100%' height='500px' frameBorder='0' src='https://a.tiles.mapbox.com/v4/jsoma.imjpp25d/attribution,zoompan,zoomwheel,geocoder,share.html?access_token=pk.eyJ1IjoianNvbWEiLCJhIjoibFJmYl9JWSJ9.AUm8d76cbOvVEn2mMeG_ZA'></iframe>
```

> **Note:** You can see an example by taking that code and saving it as a `.html` file. Open that file in a web browser and tada!

Lastly, you have your Map ID. If you're really into making maps you'll eventually want to learn JavaScript and a library like [Leaflet.js](http://leafletjs.com) or [MapBox.js](https://www.mapbox.com/mapbox.js) (which is built on top of Leaflet). These tools allow you to do all sorts of magic involving layering different maps and adding different levels of interactivity.

## 8) Being awesome

You might want to sit around and bask in your rad-itude for a little bit. You deserve it.
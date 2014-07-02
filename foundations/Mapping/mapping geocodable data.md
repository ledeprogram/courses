## Mapping Geocodeable Data

**AKA mapping some restaurants**

### Meet your data

Let's say I scraped some data from Yelp of restaurants around Columbia, just so I could search and filter and scan them a little bit better. There aren't really that many, so the list is just about this long:

|name|rating|price|address|type|
|---|---|---|---|---|
|Milano Market|4|$$|2892 Broadway|Deli|
|Buster’s|4.5|$$|892 Amsterdam Ave|American (New)|
|Maoz Vegetarian|4|$|2857 Broadway|Vegetarian|
|Roti Roll Bombay Frankie|4|$|994 Amsterdam Ave|Indian|
|Dig Inn Seasonal Market|3.5|$$|2884 Broadway|American (Traditional)|
|Tum & Yum|4|$$|917 Columbus Ave|Thai|
|Le Monde|3|$$|2885 Broadway|French|
|Mel’s Burger Bar|3|$$|2850 Broadway|Burgers|
|Miss Mamie’s Spoonbread Too|3|$$|366 W 110th St|Southern|
|Destiny Sandwich & Juice Bar|4|$|2166 Fredrick Douglass Blvd|Sandwiches|
|SEASONED VEGAN|4.5|$$|55 Saint Nicholas Ave|Vegetarian|
|Tom’s Restaurant|2.5|$$|2880 Broadway|Diners|

Since we're all computer folks, don't worry, I've got a [csv right here](restaurants.csv)

### Adding into Google Fusion Tables

This is an easier process than adding a shapefile. Visit [https://drive.google.com](https://drive.google.com), click **Create**, and select **Fusion Table**. On the next screen select **restaurants.csv** to be uploaded and click **Next**. Confirm it's importing the columns and rows correctly, then click **Next** again.

Be sure to give the table a memorable name! You might have a hundred files called **restaurants.csv**, so you'll want to call this something specific, like **Sample Restaurants Around Columbia**.

**Allow export** allows other people to take your data out in csv format (fine by us), while data attribution is useful in keeping your sources in line.

### Mapping the restaurants

Since we already know that Google Fusion Tables is great at mapping, let's just click "Map of name."

The first thing that comes up is this **Geocode** popup. **Geocoding** is the process of converting a piece of data into something mappable - typically you're going from an address to latitude & longitude. Google is generally pretty good at geocoding, so let's see how it did.

Okay, pretty poorly. So it goes. You'll note it says **Map of name** - Google thinks that the name column holds the address data, instead of the **address** column. Sounds like a problem to me, let's change it! Go back to **Rows 1** to see your data.

Next to the **address column** you have a little dropdown - select it, then **Change...**, then change the **Type** field to be **Location**.

You'll note that the **address** column is now highlighted with yellow. Google Fusion Tables highlights every field it believes can be geocoded. Now let's click back to **Map of name** to make some more changes.

Under the **Location** field next to the map, change it to **address**. Google will geocode your addresses and then do some more mapping.

Sigh, for some reason Google thinks Tum & Yum is just south of Dayon, Ohio! You might have noticed a **% ambiguous** as Google was geocoding the columns - Google isn't exactly sure *which** 917 Columbus Ave we were looking at, so it made a wild guess. A wrong wild guess! We need to give it a **hint** to know which one we're looking for.

From the **File** dropdown, select **Geocode...**. Change the **Location column** to be **address**, and then we'll want to set a **Location hint**. This helps Google know what general area we're talking about - **New York, NY** should work great.

Click **Begin geocoding** and you'll get a "Column is fully geocoded." notice. It's geocoded incorrectly, but Google doesn't know that! What you need to do to flush away the bad geocoding is to **change the address column type back to text, then back to location again**. This resets the table and lets you geocode again.

Now go back to **File > Geocode...** and try again, with the New York, NY hint. It should work this time, and your map should look great! If nothing is showing up, be sure that **address** is selected as the **Location**.

### Styling your map

A bunch of red dots isn't that useful to me - I want to highlight the good ones! Let's change the **feature styles**.

You can't do a gradient with marker icons, only **buckets**. Apparently our lowest ranking is 2.5 and the highest is 4.5, so I'm guessing we'll need to mark 2.5, 3, 3.5, 4 and 4.5. That's **five buckets**. Select **5** under **buckets**, then space out the bucket values to each cover one of the previous scores.

Click **save** and you're good to go! A nice colored map of all of the restaurants around the area.

### Filtering your data

Unfortunately, your classmates are all *incredibly picky* about what they'll eat. While that does makes them terrible people, we're kind souls, so we'll do our best to accommodate them.

Some people are vegetarians who'd rather not litter their map with burger joints. Let's filter the map for them! First, select **Filter** from the top of the map, and filter by **type**.

If you click **Vegetarian** you'll be down to two restaurants. Pretty neat. Click **Sandwiches** and we'll get another option.

Here's the thing, though: *they just don't like burgers*. Everything else is fine. So instead of selecting what we *do* want, let's select what we *don't* want displayed.

First, select **Burgers** and nothing else. Then, up and to the right there's a triple-bar icon: click it and change the setting to **Exclude selections**. Womp! Burger joints disappear, and vegetarians are left to live in peace.





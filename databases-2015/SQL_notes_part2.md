# Relational databases and SQL basics: Part 2

##Sums, minimums, maximums and averages

Going back to the MONDIAL database, let's say you wanted to find the population
of the entire world. The `country` table is our best bet for finding this data,
having as it does a `population` field:

	mondial=# SELECT population FROM country LIMIT 10;
	 population 
	------------
	    3249136
	   10538594
	    2104035
	    7379339
	     672180
	    1804838
	      72766
	   58317450
	   39181114
	    8023244
	(10 rows)

Presumably, excepting the number of stateless individuals not counted among the
population of a particular country, we could determine the world's population
by adding up all of these numbers. To save us the tedium of writing a program
to perform this task, SQL provides a particular kind of syntax to calculate
sums for all of the values in a field. It looks like this:

	mondial=# SELECT sum(population) FROM country;
	 sum     
	------------
	  5774449258
	(1 row)

The new part here is `sum()`, with the field you want summed between the
parentheses. The `sum()` function is one of several so-called "[aggregate
functions](http://www.postgresql.org/docs/9.4/static/functions-aggregate.html)"
that take the all the values from a field and reduce them down to a single
value. Another such function is `avg()`, which calculates the arithmetic mean
of a column of values:

	mondial=# SELECT avg(population) FROM country;
	          avg          
	-----------------------
	 24262391.840336134454
	(1 row)

You can use a `WHERE` clause with these queries to limit which rows are
included in the aggregate. For example, the following query selects all the MONDIAL cities
in Finland:

	mondial=# SELECT population FROM city WHERE country = 'SF';
	 population 
	------------
	       9500
	     170097
	      94234
	      42000
	      78571
	      53922
	      58345
	      31000
	      28000
	      65511
	      44000
	      97898
	      77763
	     161292
	     487428
	     160480
	      54275
	(17 rows)

Adding `sum()` around the `population` column yields the sum of just these values from the table:

	mondial=# SELECT sum(population) FROM city WHERE country = 'SF';
	   sum   
	---------
	 1714316
	(1 row)

We already covered another aggregate function, `count()`, which simply counts
the number of rows. To illustrate this with another example, consider the
`encompasses` table, which relates countries to the continents that encompass
them. (Browse this table with a `SELECT * FROM continents` to familiarize
yourself with the structure.) To count the number of countries at least
partially in Europe:

	mondial=# SELECT count(country) FROM encompasses WHERE continent = 'Europe';
	 count 
	-------
	    53
	(1 row)

Finally, the `min()` and `max()` aggregate functions return, respectively, the
minimum and maximum values for the given column. To find the country with the
smallest area, we might issue the following query:

	mondial=# SELECT min(area) FROM country;
	 min  
	------
	 0.44
	(1 row)

To find the country with the largest area:

	mondial=# SELECT max(area) FROM country;
	   max    
	----------
	 17075200
	(1 row)

The two queries can be combined into one:

	mondial=# SELECT min(area), max(area) FROM country;
	 min  |   max    
	------+----------
	 0.44 | 17075200
	(1 row)

###SELECTs with aggregate functions are different

We had been using the `SELECT` statement before as, essentially, a way to
filter and order rows from a table based on their characteristics. So you may,
at this point, notice that `SELECT` statements that include aggregate functions
operate differently from their counterparts without any aggregate functions.
Although the results of the query are returned in a tabular format, the "rows"
and "columns" in the result don't correspond to rows and columns in the
original table. (E.g., there is no column in the `country` table called `min`
and `max`; these appear only in the results of a query using those aggregate
functions.)

I bring this up because it's worth pointing out that `SELECT` with aggregates
is a little bit counterintuitive. Personally, I wish that the syntax made this
a bit clearer; everyone would benefit if, in order to use aggregate functions,
you had to use a separate statement (like `AGGREGATE table CALCULATE min(x)`
or something like that, sort of like [how MongoDB does
it](http://docs.mongodb.org/manual/reference/method/db.collection.aggregate/)).
But that's not the way SQL works, and so we close our eyes, take a deep breath,
and entrust ourselves to the solutions and abstractions so carefully invented
by the standards-makers of government and industry.

###Aggregating with `GROUP BY`

There's a particular pattern for using aggregate function that happens over and
over frequently enough that there is a special syntax for it: grouping. To
illustrate, consider the following task: we want to find the population number
for the largest city in each country, using the data in the `city` table. We
already know how to do this for individual countries, in separate queries; here
are two such queries for the US and Finland:

	mondial=# SELECT max(population) FROM city WHERE country = 'USA';
	   max   
	---------
	 7322564
	(1 row)
	
	mondial=# SELECT max(population) FROM city WHERE country = 'SF';
	  max   
	--------
	 487428
	(1 row)

If we wanted to do this with *every* country present in the `city` table, we'd
have a little programming task on our hands: find all of the unique countries,
iterate through them, issue a query for each, etc. etc. etc. Because this task
is so common, SQL provides a shortcut, which is the `GROUP BY` clause. If you
include a `GROUP BY` clause in your SQL statement, the aggregate that you
specify will be performed *not* on all of the rows that match the `WHERE`
clause, but for all rows having unique values for the column you specify.

For example, the following query calculates the maximum value for the `population` column for every unique country:

    mondial=# SELECT country, max(population) FROM city GROUP BY country;
	 country |   max    
	---------+----------
	 NEP     |   393494
	 RA      |  2988006
	 CH      |   343106
	 L       |    76600
	 AMSA    |         
	 WD      |    11000
	 LB      |         
	 BF      |         
	 EW      |   478000
	 MV      |    46334
	 BEN     |         
	 CAYM    |         
	 SY      |    24570
	 IRQ     |  4478000
	... (rows omitted) ...
	 PL      |  1655000
	 TL      |    59069
	 A       |  1583000
	 ZW      |         
	 EAU     |         
	 STP     |         
	 Q       |   217294
	 MOC     |   931591
	 RO      |  2037000
	 LS      |    75000
	 PNG     |   141500
	 BZ      |     3000
	 SLB     |    26000
	 NORF    |         
	(238 rows)

(Some countries have blanks, since apparently there are some countries whose
listed cities all have an empty population field.) This query tells us that,
e.g., the most populous city in Nepal has 393,494 people, that the most
populous city in Argentina (code `RA`) has 2,988,006 people, etc.

We can clean up the empty rows by using a `WHERE` clause to include as
candidates for aggregation only those cities that have a non-empty `population`
field:

	mondial=# SELECT country, max(population)
	    FROM city
	    WHERE population IS NOT NULL
	    GROUP BY country;
	 country |   max    
	---------+----------
	 NEP     |   393494
	 RA      |  2988006
	 CH      |   343106
	 L       |    76600
	 WD      |    11000
	 EW      |   478000
	 MV      |    46334
    ... (rows omitted) ...
	 MOC     |   931591
	 RO      |  2037000
	 LS      |    75000
	 PNG     |   141500
	 BZ      |     3000
	 SLB     |    26000
	(168 rows)
	
Queries with `GROUP BY` also allow you to use the `ORDER BY` and `LIMIT`
clauses. Here's an example that sorts the results of the query in alphabetical
order by country, limited to just the first five rows:

	mondial=# SELECT country, max(population)
        FROM city
        WHERE population IS NOT NULL
        GROUP BY country
        ORDER BY country
        LIMIT 5;
	 country |   max   
	---------+---------
	 A       | 1583000
	 AFG     |  892000
	 AG      |   36000
	 AL      |  192000
	 AND     |   15600
	(5 rows)

To order by the aggregate field, repeat the aggregate expression in the `ORDER BY` clause:
	
	mondial=# SELECT country, max(population)
        FROM city
        WHERE population IS NOT NULL
        GROUP BY country
        ORDER BY max(population) DESC
        LIMIT 5;
	 country |   max    
	---------+----------
	 ROK     | 10229262
	 IND     |  9925891
	 PK      |  9863000
	 MEX     |  9815795
	 BR      |  9811776
    (5 rows)

> NOTE: You might think that getting the *name* of the city that has the
> largest population for each country (i.e., the row containing the group-wise
> maximum) would be easy---but, unfortunately, it isn't. [Here's a good overview
> of techniques for performing this task](http://jan.kneschke.de/projects/mysql/groupwise-max/).

Here's another example of `GROUP BY`. Consider the `island` table, which is a list of islands in the world, including their area, height, island group and type:
	
	mondial=# SELECT name, islands, area, height, type FROM island LIMIT 10;
	       name        |     islands      |  area   | height |   type   
	-------------------+------------------+---------+--------+----------
	 Svalbard          | Svalbard         |   39044 |   1717 | 
	 Greenland         |                  | 2175600 |        | 
	 Iceland           |                  |  102829 |   2119 | volcanic
	 Aust-Vagoey       | Lofotes          |     526 |   1146 | 
	 Streymoy          | Faroe Islands    |     373 |    789 | 
	 Ireland           | British Isles    |   84421 |   1041 | 
	 Great Britain     | British Isles    |  229850 |   1344 | 
	 Shetland Mainland | Shetland Islands |     970 |    449 | 
	 Orkney Mainland   | Orkney Islands   |     492 |        | 
	 South Ronaldsay   | Orkney Islands   |      50 |        | 
	(10 rows)

The `type` field has a few distinct values:

	mondial=# SELECT DISTINCT(type) FROM island;
	   type   
	----------
	 
	 coral
	 volcanic
	 atoll
	 lime
	(5 rows)

So, let's find the *average area* of islands belonging to each island type:

	mondial=# SELECT type, avg(area) FROM island GROUP BY type;
	   type   |         avg          
	----------+----------------------
	          |   42409.513406593407
	 coral    | 211.7166666666666667
	 volcanic |   10318.585897435897
	 atoll    |   5.2425000000000000
	 lime     | 430.0000000000000000
	(5 rows)

Volcanic islands are awful big, aren't they?

> EXERCISE: Find the island group (i.e., the `islands` field in the `island`
> table) with the greatest average height.

###Filter aggregations with `HAVING`

We saw above that the `WHERE` clause can be used to restrict which rows are used when calculating an aggregate. But what if we want to restrict which rows are present *in the response to the aggregate query* itself? It's not difficult, but it does require a discussion of a previously undiscussed clause: `HAVING`.

To illustrate the problem, consider the `river` table. This table has a list of rivers, which includes the river's name and its outlet, which is either a sea, a lake, or another river (or possibly none of these, in the case of rivers in endorheic basins). Here's what the table looks like:

	mondial=# SELECT name, river, lake, sea FROM river LIMIT 10;
	        name         |  river  |    lake    |      sea       
	---------------------+---------+------------+----------------
	 Thjorsa             |         |            | Atlantic Ocean
	 Joekulsa a Fjoellum |         |            | Norwegian Sea
	 Glomma              |         |            | Skagerrak
	 Lagen               | Glomma  | Mjoesa-See | 
	 Goetaaelv           |         |            | Kattegat
	 Klaraelv            |         | Vaenern    | 
	 Umeaelv             |         | Storuman   | Baltic Sea
	 Dalaelv             |         |            | Baltic Sea
	 Vaesterdalaelv      | Dalaelv |            | 
	 Oesterdalaelv       | Dalaelv | Siljan     | 
	(10 rows)

These results show that, e.g., the [Thjorsa river](https://en.wikipedia.org/wiki/%C3%9Ej%C3%B3rs%C3%A1) empties into the Atlantic Ocean, while the [Klaraelv river](https://en.wikipedia.org/wiki/Klar%C3%A4lven) empties into a lake named "Vaenern."

Let's say we're interested in knowing exactly how many rivers empty into all of the known seas. We could find this out by issuing a query that counts the rivers, grouped by the name of the sea:

	mondial=# select sea, count(name) from river group by sea;
	        sea        | count 
	-------------------+-------
	                   |   130
	 Norwegian Sea     |     1
	 Persian Gulf      |     1
	 Malakka Strait    |     1
	 Atlantic Ocean    |    24
	 Barents Sea       |     3
	 Arabian Sea       |     1
	 Pacific Ocean     |     3
	 Arctic Ocean      |     2
	 The Channel       |     1
	 Mediterranean Sea |     8
	 Black Sea         |     3
	 Sea of Okhotsk    |     1
	 South China Sea   |     1
	 Gulf of Bengal    |     1
	 East China Sea    |     1
	 Yellow Sea        |     1
	 Bering Sea        |     1
	 Gulf of Mexico    |     2
	 Caribbean Sea     |     2
	 Indian Ocean      |     4
	 Sea of Azov       |     1
	 Kattegat          |     1
	 North Sea         |     5
	 Sibirian Sea      |     5
	 Andaman Sea       |     2
	 Skagerrak         |     1
	 Baltic Sea        |    11
	(28 rows)

This is fine, but it has a lot of noise! What if we wanted to get this list of
results, but *exclude* the rows that have a count of one or less. Is this
possible? If so, how?

The first way you might attempt to solve this would be with the `WHERE` clause.
That's what `WHERE` is for, after all, right? To exclude records from a query.
Let's try it:

	mondial=# SELECT sea, count(name) FROM river WHERE count(name) > 1 GROUP BY sea; 
	ERROR:  aggregate functions are not allowed in WHERE
	LINE 1: select sea, count(name) from river where count(name) > 1 gro...
	                                                 ^

Hmm. Weird. Apparently, and I quote, "aggregate functions are not allowed in
`WHERE`." It turns out that the `WHERE` clause can only be used to filter rows
*before* the aggregation operation happens---not afterward. To filter rows in
the aggregation, there's a different clause, (confusingly, IMO) called
`HAVING`. The `HAVING` clause works like this:

	mondial=# SELECT sea, count(name) FROM river GROUP BY sea HAVING count(name) > 1;
	        sea        | count 
	-------------------+-------
	                   |   130
	 Atlantic Ocean    |    24
	 Barents Sea       |     3
	 Pacific Ocean     |     3
	 Arctic Ocean      |     2
	 Mediterranean Sea |     8
	 Black Sea         |     3
	 Gulf of Mexico    |     2
	 Caribbean Sea     |     2
	 Indian Ocean      |     4
	 North Sea         |     5
	 Sibirian Sea      |     5
	 Andaman Sea       |     2
	 Baltic Sea        |    11
	(14 rows)

The `HAVING` clause looks just like a `WHERE` clause, except that it can refer
only to fields that are present in the aggregation (in this case,
`count(name)`).  As you can see, by including the `HAVING` clause in this
query, we've excluded results where the aggregation function didn't meet a
certain criterion. Perfect!

Let's do another example. The `religion` table is a list of records that relate
religions to countries. Each country has several records in the table, and each
record indicates the percentage of the population that adherents to the given
religion make up in the country. So, for example, this query:

	mondial=# select * from religion limit 10;
	 country |        name        | percentage 
	---------+--------------------+------------
	 AL      | Muslim             |         70
	 AL      | Roman Catholic     |         10
	 AL      | Christian Orthodox |         20
	 GR      | Muslim             |        1.3
	 GR      | Christian Orthodox |         98
	 MK      | Muslim             |         30
	 MK      | Christian Orthodox |         67
	 SRB     | Christian Orthodox |         85
	 SRB     | Muslim             |        3.2
	 SRB     | Roman Catholic     |        5.5
	(10 rows)

... shows that in Albania (code `AL`), 70 percent of the country is Muslim, 10
percent is Roman Catholic, and 20 percent is Christian Orthodox.

We'll use this table to find religions that are present in the fewest countries.

	mondial=# SELECT name, count(country) FROM religion GROUP BY name;
	            name             | count 
	-----------------------------+-------
	 Buddhist                    |    15
	 African Methodist Episcopal |     1
	 Ekalesia Niue               |     1
	 Jains                       |     1
	 United                      |     1
	 Judaism                     |     1
	 Armenian Apostolic          |     1
	 Taoist                      |     1
	 Kimbanguist                 |     1
	 Coptic Christian            |     1
	 Evangelical Alliance        |     1
	 Presbyterian                |     3
	 Muslim                      |    98
	 Sikh                        |     1
	 Church Tuvalu               |     1
	 United Church               |     2
	 Jewish                      |    13
	 Baptist                     |     5
	 Episcopalian                |     1
	 Christian Congregationalist |     1
	 Uniting Church Australia    |     1
	 Anglican                    |    16
	 Seventh-Day Adventist       |     7
	 Confucianism                |     1
	 Church of God               |     3
	 Church Christ               |     1
	 Chondogyo                   |     1
	 Pentecostal                 |     1
	 Christian                   |    57
	 Christian Orthodox          |    22
	 Druze                       |     1
	 Methodist                   |     4
	 Roman Catholic              |   104
	 Mormon                      |     2
	 Protestant                  |    67
	 Bahai                       |     2
	 Hindu                       |    14
	(37 rows)

These results show us that, e.g., Hinduism is present in 14 different
countries; Mormonism is present in 2; Islam is present in 98. Let's add a
`HAVING` clause so that we see *only* the religions that are present in a
single country:

	mondial=# SELECT name, count(country) FROM religion GROUP BY name HAVING count(country) = 1;
	            name             | count 
	-----------------------------+-------
	 African Methodist Episcopal |     1
	 Ekalesia Niue               |     1
	 Jains                       |     1
	 United                      |     1
	 Judaism                     |     1
	 Armenian Apostolic          |     1
	 Taoist                      |     1
	 Kimbanguist                 |     1
	 Coptic Christian            |     1
	 Evangelical Alliance        |     1
	 Sikh                        |     1
	 Church Tuvalu               |     1
	 Episcopalian                |     1
	 Christian Congregationalist |     1
	 Uniting Church Australia    |     1
	 Confucianism                |     1
	 Church Christ               |     1
	 Chondogyo                   |     1
	 Pentecostal                 |     1
	 Druze                       |     1
	(20 rows)

(Obviously, there are adherents of these religions in more than one country!
Presumably, the `religion` table only has records if the number of adherents is
large enough that it constitutes a percentage of the general population above a
certain threshold.)

Let's make our query a bit more specific and find the religions that only occur
in one country and where that religion's percentage share in the country is
less than 5%. We can do this by filtering the rows first with `WHERE`, like so:

	mondial=# SELECT name, count(country)
	    FROM religion
	    WHERE percentage < 5
	    GROUP BY name
	    HAVING count(country) = 1;
	         name         | count 
	----------------------+-------
	 Baptist              |     1
	 Druze                |     1
	 Confucianism         |     1
	 Jains                |     1
	 Sikh                 |     1
	 Church Christ        |     1
	 Chondogyo            |     1
	 Evangelical Alliance |     1
	 Pentecostal          |     1
	(9 rows)

The tricky part in this query is the *combination* of `WHERE` and `HAVING`. The
`WHERE` clause tells SQL to exclude any rows where the percentage is less than
5 *before* any aggregation happens. The `HAVING` clause tells SQL to exclude
any rows *after* the aggregation where the result of `count(country)` is not
equal to 1.

##Joins

In this section, we're going to discuss one of the things that makes SQL truly powerful: the ability to create queries that "join" tables together. 

To illustrate, let's tackle one particular task. So far, We've been running up
against a problem pretty consistently with the MONDIAL database, which is this: the
*names* of countries aren't stored in most of these tables---just their "code." When looking at the `city` table, for instance:

	mondial=# SELECT name, country FROM city ORDER BY name LIMIT 10;
	    name    | country 
	------------+---------
	 Aachen     | D
	 Aalborg    | DK
	 Aarau      | CH
	 Aarhus     | DK
	 Aarri      | WAN
	 Aba        | WAN
	 Abaetetuba | BR
	 Abakan     | R
	 Abancay    | PE
	 Abeokuta   | WAN
	(10 rows)

Unless we happen to have already memorized these codes, we have to look them up one-by-one in the `country` table to find out what they mean:

	mondial=# SELECT name FROM country WHERE code = 'WAN';
	  name   
	---------
	 Nigeria
	(1 row)

That's sort of inconvenient, and it seems like computers should be able to help
with this problem. Isn't there a way to write a query so that each row returned
from the `city` table automatically gets matched up with the `country` that has
the corresponding code?

In fact, there is, and it's called `JOIN`. We'll continue with the
`city`/`country` analogy in a second, but it's a bit easier to demonstrate how
`JOIN` works with some smaller, toy tables first. Recall from Part One our tiny
database for a news organization, which consists of a table for writers:

| name | title | start_year |
| ---- | ----- | ---------- |
| Gabriella McCullough | reporter | 2009 |
| Steven Kennedy | drama critic | 2012 |
| Jalen Shaara | columnist | 2002 |

... and then a table of articles that those writers are responsible for:

| author | title | published_date |
| ------ | ----- | -------------- |
| Gabriella McCullough | Man, opossum reach garbage accord | 2015-07-01 |
| Steven Kennedy | "The Deceit of Apricot" opens to rave reviews | 2015-07-15 |
| Jalen Shaara | What's the Big Data? Why I'm a data skeptic | 2015-07-16 |
| Gabriella McCullough | Traffic signals restored on Tunguska Ave | 2015-07-01 |

Let's say we wanted to produce a *new* table, which consists of a list of article titles and dates, along with the name of the author, the author's title, and the author's start year. In other words, we want information from *both* tables, and we want to automatically *align* that data so that we end up with the correct title and start year for each author. Basically, what we want is this:

| article.author | article.title | article.published_date | author.title | author.start_year |
| ------ | ----- | -------------- | --- | --- |
| Gabriella McCullough | Man, opossum reach garbage accord | 2015-07-01 | reporter | 2009 |
| Steven Kennedy | "The Deceit of Apricot" opens to rave reviews | 2015-07-15 |  drama critic | 2012 |
| Jalen Shaara | What's the Big Data? Why I'm a data skeptic | 2015-07-16 | columnist | 2002 |
| Gabriella McCullough | Traffic signals restored on Tunguska Ave | 2015-07-01 | reporter | 2002 |

Essentially, what we've done is taken our "articles" table, and then reshuffled
the "authors" table and glued it on to the right-hand side, making one big
monster table that joins the two together. This is what is meant by a "join"
in relational database parlance.

We're going to solve our country name problem using a join as well, and in the
process, explain the syntax for how joins work in SQL.

###Join in SQL

The syntax of a `JOIN` looks like this:

    SELECT fields
    FROM left_table
    JOIN right_table ON left_field = right_field

... where `fields` is the list of fields that you want, `left_table` is the
table you want to leave alone, and `right_table` is the table you want to
re-arrange and tack on to the left table. The `left_field` and `right_field`
values determine how the joined table will be aligned: the data from `right_table` will be joined to the 

A join consists of two tables, and a field in each table that links the two
together. In the example above, the "link" between the two tables is that the
name of the author in the articles table needs to match the name of the author
in the writers table. For the purposes of naming the countries that each city
is in, the two tables we want to join are `city` and `country`, and the "link"
between them is the country code---which is in the `country` field of the
`city` table, and the `code` field of the `country` table. Here's what the
query looks like:

	mondial=# SELECT city.name, city.population, country.code, country.name
        FROM city JOIN country ON city.country = country.code
        LIMIT 10;
	   name   | population | code |  name   
	----------+------------+------+---------
	 Tirane   |     192000 | AL   | Albania
	 Shkoder  |      62000 | AL   | Albania
	 Durres   |      60000 | AL   | Albania
	 Vlore    |      56000 | AL   | Albania
	 Elbasan  |      53000 | AL   | Albania
	 Korce    |      52000 | AL   | Albania
	 Komotini |            | GR   | Greece
	 Kavalla  |      56705 | GR   | Greece
	 Athens   |     885737 | GR   | Greece
	 Piraeus  |     196389 | GR   | Greece
	(10 rows)

There's a *lot* going on in this query, and one or two new things other than the join. So let's take it line by line. Let's start with the middle line:

    FROM city JOIN country ON city.country = country.code

This line says to select from the `city` table (this is the left table of our
join) and join it to the `country` table (the right table). The `ON` clause
tells PostgreSQL how to re-arrange the right-side table. It says, in effect:
for every row in the `city` table, find the row in the `country` table where
the country's `code` field (`country.code`) matches the city's `country` field
(`city.country`).

The dot between the name of the table and the field is something we haven't discussed yet: when you're naming a field, the dot syntax allows you to specify *which table* that field is found in. (This is important when the two tables you're joining have fields with the same name---you need to be able to disambiguate.) We see the dot again in the first line of the query:

	SELECT city.name, city.population, country.code, country.name

This line specifies *which* fields we want to see. Because we're joining two tables, we need to be explicit about which table the field we want originates from. In this query, we're getting the `name` field from the `city` table, the `population` field from the `country` table, the `code` field from the `country` table, and the `name` field from the `country` table.

> NOTE: To see what the entire joined table looks like, without any fields selected, try the following query: `SELECT * FROM city JOIN country ON city.country = country.code LIMIT 10;`

Finally, the `LIMIT 10` line works just like it does with other `SELECT` statements: it just limits the results to the given number of lines. (You can remove the `LIMIT` if you want to page through the results in `psql`.)

###Combining `JOIN` with `WHERE` and aggregation

Once you've created a joined table with a `JOIN` clause, you can operate on it just like any other table---restricting selections with `WHERE` and performing aggregates with `GROUP BY`. Let's do another example from joining the `city` and `country` tables. Here's a query that finds every city with a population over
one million people that is found in a country with fewer than five million
people:

	mondial=# SELECT city.name, city.population, country.name,
            country.population
        FROM city JOIN country ON city.country = country.code
        WHERE city.population > 1000000 AND country.population < 5000000;
	    name    | population |   name    | population 
	------------+------------+-----------+------------
	 Yerevan    |    1200000 | Armenia   |    3463574
	 Singapore  |    2558000 | Singapore |    3396924
	 Managua    |    1195000 | Nicaragua |    4272352
	 Montevideo |    1247000 | Uruguay   |    3238952
	(4 rows)

A great thing about table joins is that we can use `WHERE` to establish
criteria for fields in either the left or right table. If you're having trouble
picturing how this query works, try running it without one of the expressions
in the `WHERE` clause (i.e., leave out `city.population > 1000000` or
`country.population < 5000000`). (No idea, btw, why Singapore the city and
Singapore the country don't have the same population in MONDIAL.)

The following example combines nearly all of the concepts we've discussed so
far. It finds the sum of the population of cities in the `city` table for all
countries, and then displays those countries having at least 20 million
individuals living in cities.

	mondial=# SELECT country.name, sum(city.population)
        FROM city JOIN country ON city.country = country.code
        WHERE city.population IS NOT NULL
        GROUP BY country.name
        HAVING sum(city.population) > 20000000
        ORDER BY sum(city.population) DESC;
	      name      |    sum    
	----------------+-----------
	 China          | 158349751
	 India          |  83893675
	 Brazil         |  77092190
	 Russia         |  67935900
	 United States  |  67273489
	 Mexico         |  34325020
	 United Kingdom |  33081900
	 Pakistan       |  27512788
	 Indonesia      |  27365834
	 South Korea    |  26978665
	 Japan          |  26918691
	 Germany        |  25973481
	 Turkey         |  24065082
	 Iran           |  23493698
	(14 rows)

The tricky part here is the `GROUP BY` clause, which is grouping by a value in
the right table of the join (`country.name`).

##Joining with many-to-many relationships

So far, we've been exercising our table join chops on the `city` and `country`
tables. These two tables have a *many-to-one* relationship: one country can
contain many cities, but a city can only be in one country. It's easy to write
a `JOIN` for a one-to-many relation, since you know that the right-side table
will always have, at most, one matching record.

But the MONDIAL database (along with many other relational database schemas)
has entities that exist in a many-to-many relationship. For example, a river
can flow through multiple countries, and one country can have multiple rivers
flowing through it. Representing many-to-many relationships in SQL is a bit
tricky, and as a consequence, writing `JOIN`s for many-to-many relationships is
tricky as well.

The conventional way to model a many-to-many relationship in a relational database is with a [junction table](https://en.wikipedia.org/wiki/Junction_table) (sometimes also called a "linking table"). A junction table has rows for every instance of relationship between two tables, using a unique key to refer to the rows in those tables.

###Many writers, many articles

To illustrate, let's return to our news organization database. We have a table for writers:

| name | title | start_year |
| ---- | ----- | ---------- |
| Gabriella McCullough | reporter | 2009 |
| Steven Kennedy | drama critic | 2012 |
| Jalen Shaara | columnist | 2002 |

... and then a table of articles that those writers are responsible for:

| author | title | published_date |
| ------ | ----- | -------------- |
| Gabriella McCullough | Man, opossum reach garbage accord | 2015-07-01 |
| Steven Kennedy | "The Deceit of Apricot" opens to rave reviews | 2015-07-15 |
| Jalen Shaara | What's the Big Data? Why I'm a data skeptic | 2015-07-16 |
| Gabriella McCullough | Traffic signals restored on Tunguska Ave | 2015-07-01 |

This schema represents a simple many-to-one relationship: one writer can write
many articles, and every article has exactly one writer. But let's say that one
day, in our news organization, Gabriella McCullough and Steven Kennedy
*collaborate* on an article. How do we represent this in the database?

One option, of course, would simply be to store both of the names in the `author` field:

| author | title | published_date |
| ------ | ----- | -------------- |
| Gabriella McCullough and Steven Kennedy | Theater Chairs Uncomfortable, Experts Warn | 2015-07-28 |

There's a problem with this solution, however, which is that now a query on our database that looks like this:

    SELECT count(*) FROM articles WHERE author = 'Gabriella McCullough';

... no longer functions properly, because it won't include the article where Gabriella collaborated with Steven. Likewise, it would be difficult to construct a `JOIN` (like we did in the previous section) that would tell us the title of all of the authors involved in writing the story. (We'd have to parse out the names first in order to use them in the query, which is a hassle.)

The issue is that we've discovered that our initial modeling of the data
structure was wrong. There isn't a many-to-one relationship between articles
and writers; instead, there's a many-to-many relationship: a single writer can
write multiple stories, and any given story can be authored by more than one
writer.

To represent this relationship, we need to slightly restructure our database.
First, we'll remove the `author` field from the `articles` table and add a new
field, `article_id`, which is a unique integer assigned to each article:

| article_id | title | published_date |
| ------ | ----- | -------------- |
| 1 | Man, opossum reach garbage accord | 2015-07-01 |
| 2 | "The Deceit of Apricot" opens to rave reviews | 2015-07-15 |
| 3 | What's the Big Data? Why I'm a data skeptic | 2015-07-16 |
| 4 | Traffic signals restored on Tunguska Ave | 2015-07-01 |
| 5 | Theater Chairs Uncomfortable, Experts Warn | 2015-07-28 |

... and then create a new table, which relates author names to the articles
that they've written. We'll store one row for each instance of a relationship
between an author and an article and call it `author_article`:

| author | article_id |
| ------ | ---------- |
| Gabriella McCullough | 1 |
| Gabriella McCullough | 4 |
| Gabriella McCullough | 5 |
| Steven Kennedy | 2 |
| Steven Kennedy | 5 |
| Jalen Shaara | 3 |

This junction table tells us that Gabriella has a byline on articles 1, 4, and
5; Steven has a byline on articles 2 and 5; and Jalen has a byline on article
3. For any article, we could get a list of its authors like so:

    SELECT author FROM author_article WHERE article_id = 5;

Getting a list of titles on which a writer has a byline is slightly more complicated, and involves a join:

    SELECT article.title
    FROM author_article JOIN article
        ON article.article_id = author_article.article_id
    WHERE author_article.author = 'Gabriella McCullough';

###Rivers and countries

Let's return to the MONDIAL database for an example with real data. As
mentioned above, rivers and countries are in a many-to-many relationship. The
MONDIAL database has a table for countries, and a table for rivers, and a table
called `geo_river` that is the junction table for their many-to-many
relationship. Here's what the table looks like:

	mondial=# SELECT river, country, province FROM geo_river ORDER BY river
	    LIMIT 20;
	      river      | country |     province     
	-----------------+---------+------------------
	 Aare            | CH      | Aargau
	 Aare            | CH      | Solothurn
	 Aare            | CH      | Bern
	 Adda            | I       | Lombardia
	 Akagera         | EAT     | Mwanza
	 Akagera         | RWA     | Rwanda
	 Allegheny River | USA     | New York
	 Allegheny River | USA     | Pennsylvania
	 Aller           | D       | Niedersachsen
	 Alz             | D       | Bayern
	 Amazonas        | BR      | Amapa
	 Amazonas        | BR      | Amazonas
	 Amazonas        | PE      | Loreto
	 Amazonas        | PE      | Ucayali
	 Amazonas        | BR      | Para
	 Amazonas        | PE      | Cuzco
	 Amazonas        | CO      | Amazonas
	 Ammer           | D       | Bayern
	 Amudarja        | UZB     | Qaraqalpoghiston
	 Amudarja        | AFG     | Afghanistan
	(20 rows)
	
This result shows us that, e.g., the Amazon river flows through several different countries. (The `geo_river` table also gives us information on which *provinces* a river flows through, so we see that the Allegheny wends its way through both New York and Pennsylvania.)

All well and good so far. Let's exploit the many-to-many relationship to
get information about particular countries and rivers. To find all of the rivers that flow through Finland:

	mondial=# SELECT river, province FROM geo_river WHERE country = 'SF';
	     river     |  province  
	---------------+------------
	 Paatsjoki     | Lappia
	 Ounasjoki     | Lappia
	 Kemijoki      | Lappia
	 Oulujoki      | Oulu
	 Kymijoki      | Haeme
	 Kymijoki      | Kymi
	 Kymijoki      | Mikkeli
	 Kokemaeenjoki | Turku-Pori
	 Vuoksi        | Kuopio
	 Vuoksi        | Kymi
	(10 rows)

A list of all the countries and provinces that the Rhine runs through:

	mondial=# SELECT river, country, province FROM geo_river WHERE river = 'Rhein';
	 river | country |      province       
	-------+---------+---------------------
	 Rhein | F       | Alsace
	 Rhein | A       | Vorarlberg
	 Rhein | D       | Baden Wurttemberg
	 Rhein | D       | Hessen
	 Rhein | D       | Nordrhein Westfalen
	 Rhein | D       | Rheinland Pfalz
	 Rhein | FL      | Liechtenstein
	 Rhein | CH      | Aargau
	 Rhein | CH      | Basel-Land
	 Rhein | CH      | Basel-Stadt
	 Rhein | CH      | Graubunden
	 Rhein | CH      | Sankt Gallen
	 Rhein | CH      | Schaffhausen
	 Rhein | CH      | Thurgau
	 Rhein | CH      | Zurich
	 Rhein | NL      | Gelderland
	 Rhein | NL      | Zuid Holland
	(17 rows)

This is a bit annoying, since we're seeing the country codes again instead of the country names. In order to get the country name, we need to `JOIN` the junction table with the `country` table to get the country name out.

	mondial=# SELECT geo_river.river, country.name, geo_river.province
        FROM geo_river JOIN country ON geo_river.country = country.code
        WHERE river = 'Rhein';
	 river |     name      |      province       
	-------+---------------+---------------------
	 Rhein | France        | Alsace
	 Rhein | Austria       | Vorarlberg
	 Rhein | Germany       | Baden Wurttemberg
	 Rhein | Germany       | Hessen
	 Rhein | Germany       | Nordrhein Westfalen
	 Rhein | Germany       | Rheinland Pfalz
	 Rhein | Liechtenstein | Liechtenstein
	 Rhein | Switzerland   | Aargau
	 Rhein | Switzerland   | Basel-Land
	 Rhein | Switzerland   | Basel-Stadt
	 Rhein | Switzerland   | Graubunden
	 Rhein | Switzerland   | Sankt Gallen
	 Rhein | Switzerland   | Schaffhausen
	 Rhein | Switzerland   | Thurgau
	 Rhein | Switzerland   | Zurich
	 Rhein | Netherlands   | Gelderland
	 Rhein | Netherlands   | Zuid Holland
	(17 rows)

Let's dig a bit deeper and select rivers based on their characteristics.
We already know how to get a list of names of rivers whose length is greater
than 4500:

	mondial=# SELECT name FROM river WHERE length > 4500;
	   name   
	----------
	 Hwangho
	 Jangtse
	 Amazonas
	(3 rows)

But let's say that we want to know, for each of these rivers, the names of the countries and provinces they flow through. In order to find this, we're going to `JOIN` this statement to the `geo_river` table like so:

	mondial=# SELECT river.name, geo_river.country, geo_river.province
        FROM river JOIN geo_river ON river.name = geo_river.river
        WHERE length > 4500;
	   name   | country |     province      
	----------+---------+-------------------
	 Hwangho  | TJ      | Gansu
	 Hwangho  | TJ      | Henan
	 Hwangho  | TJ      | Qinghai
	 Hwangho  | TJ      | Shaanxi
	 Hwangho  | TJ      | Shandong
	 Hwangho  | TJ      | Nei Monggol
	 Hwangho  | TJ      | Ningxia Huizu
	 Jangtse  | TJ      | Anhui
	 Jangtse  | TJ      | Hubei
	 Jangtse  | TJ      | Hunan
	 Jangtse  | TJ      | Jiangsu
	 Jangtse  | TJ      | Jiangxi
	 Jangtse  | TJ      | Qinghai
	 Jangtse  | TJ      | Sichuan
	 Jangtse  | TJ      | Yunnan
	 Jangtse  | TJ      | Tibet
	 Jangtse  | TJ      | Shanghai (munic.)
	 Amazonas | CO      | Amazonas
	 Amazonas | BR      | Amapa
	 Amazonas | BR      | Amazonas
	 Amazonas | BR      | Para
	 Amazonas | PE      | Cuzco
	 Amazonas | PE      | Loreto
	 Amazonas | PE      | Ucayali
	(24 rows)

This join is interesting, since in the act of joining, we actually introduced *more rows* into the search results. That's what happens when the right table has more than one row that matches the condition in the `ON` clause.

Of course, we still have that pesky country code! To get rid of it, we need
to join *twice*: once on `river` and again on `country`:
	
	mondial=# SELECT river.name, country.name, geo_river.province
        FROM river
        JOIN geo_river ON river.name = geo_river.river
        JOIN country ON country.code = geo_river.country
        WHERE length > 4500;
	   name   |   name   |     province      
	----------+----------+-------------------
	 Hwangho  | China    | Gansu
	 Hwangho  | China    | Henan
	 Hwangho  | China    | Qinghai
	 Hwangho  | China    | Shaanxi
	 Hwangho  | China    | Shandong
	 Hwangho  | China    | Nei Monggol
	 Hwangho  | China    | Ningxia Huizu
	 Jangtse  | China    | Anhui
	 Jangtse  | China    | Hubei
	 Jangtse  | China    | Hunan
	 Jangtse  | China    | Jiangsu
	 Jangtse  | China    | Jiangxi
	 Jangtse  | China    | Qinghai
	 Jangtse  | China    | Sichuan
	 Jangtse  | China    | Yunnan
	 Jangtse  | China    | Tibet
	 Jangtse  | China    | Shanghai (munic.)
	 Amazonas | Colombia | Amazonas
	 Amazonas | Brazil   | Amapa
	 Amazonas | Brazil   | Amazonas
	 Amazonas | Brazil   | Para
	 Amazonas | Peru     | Cuzco
	 Amazonas | Peru     | Loreto
	 Amazonas | Peru     | Ucayali
	(24 rows)

This query essentially takes the table resulting from the first join and uses
it as the left table in a *second* join. Tricky! But powerful.

###Aggregates with many-to-many relations

You can use aggregates with junction tables fairly easily. For example, here's a query that gets the total number of provinces that each river passes through:

	mondial=# SELECT river, count(province)
	    FROM geo_river GROUP BY river
	    ORDER BY count(province) DESC
        LIMIT 10;
	  river   | count 
	----------+-------
	 Donau    |    30
	 Weichsel |    18
	 Nile     |    18
	 Rhein    |    17
	 Tigris   |    16
	 Volga    |    14
	 Euphrat  |    14
	 Parana   |    13
	 Theiss   |    11
	 Elbe     |    10
	(10 rows)

And, the other way, the total number of rivers that pass through each province:

	mondial=# SELECT province, count(river)
        FROM geo_river
        GROUP BY province
        ORDER BY count(river) DESC
        LIMIT 10;
	     province      | count 
	-------------------+-------
	 Bayern            |    10
	 Bandundu          |     7
	 Haut Zaire        |     7
	 Shaba/Katanga     |     7
	 Ethiopia          |     6
	 Tibet             |     6
	 Serbia            |     6
	 Baden Wurttemberg |     6
	 Equateur          |     6
	 Hessen            |     5
	(10 rows)

##Further reading

* For a different take on all this material, [consult Joshua Lande's excellent series, "What Every Data Scientist Needs to Know about SQL"](http://joshualande.com/data-science-sql/)
* The official PostgreSQL documentation has a [good tutorial on aggregate functions](http://www.postgresql.org/docs/9.4/static/tutorial-agg.html). See also [the list of all supported aggregate functions in PostgreSQL](http://www.postgresql.org/docs/9.4/static/functions-aggregate.html).
* The official PostgreSQL documentation also has an [introduction to the `FROM` clause](http://www.postgresql.org/docs/9.4/static/queries-table-expressions.html#QUERIES-FROM) that covers table joins in some detail.


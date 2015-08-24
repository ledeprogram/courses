# Relational databases and SQL basics: Part 1

A relational database contains a number of tables consisting of rows and
columns. Each row in the table represents some entity, with each column giving
information about that entity. For example, let's take on the data storage
needs of an imaginary news organization. A news organization might need to keep
track of all the writers they have on staff. We'll create a "writers" table
to hold this information:

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

Looks pretty okay so far! You can easily imagine using this data for any
number of purposes: to generate the home page of the publication; to do
metric evaluations on employee performance; to do text analysis on article
titles, etc.

The decisions you make about how to separate your data into tables, and how to
decide what columns to put into those tables, is called the database *schema*.
The schema above isn't an okay start, but has some problems---which we'll
discuss as the tutorial progresses.

## Relational database management software (RDBMS)

The concept of the "relational database" stretches back many decades, and over
the years a number of programmers and vendors have made available software that
implements the basic idea. The most popular that you're likely to come across:

* MySQL, an open-source RDBMS widely used in web applications
* Oracle and Microsoft's SQL Server, enterprise-grade software used in large
organizations
* SQLite, a tiny, embeddable RDMBS that you can include in essentially any
  application (the Python standard library includes a SQLite module)
* PostgreSQL, another open-source RDBMS

If you're developing an application from scratch, it can be tricky to decide
which RDBMS to use. There are many criteria that might play into your decision
(such as: How much does it cost? How does it perform with large amounts of
data? How does it perform with a large number of users?). (If you're working
with an existing database (say, a database already present in your
organization), you'll just have to learn to work with what you're given.)

In this tutorial, we're going to use PostgreSQL (sometimes called "Postgres"
for short). It's freely available, open-source software that strikes a good
balance between ease of use and being usable at serious scale.

For the remainder of this tutorial, I'm going to assume that you're using
OS X and you've installed Postgres.app on your local machine. You can easily
install PostgreSQL on other operating systems; on Linux it should be as easy
as using your package manager. If you're having trouble, let me know and I can
help you out!

## SQL

Although the details of how any given RDBMS stores its data can differ wildly,
nearly every RDBMS you use supports one computer language for data input and
data access: SQL.  SQL ("Structured Query Language," often pronounced as
"sequel" and sometimes by naming its initials) is a language that is
*specifically built* for specifying and retrieving combinations of rows and
columns from relational data. It's an extraordinarily powerful language, and
of what follows in this tutorial is learning how SQL works and what it looks
like.

In the same way that you can write HTML and have it appear basically the same
way on every web browser, you can write SQL and expect it to behave more or
less the same in every RDBMS. Or, at least, that's the ideal. But beware: every
RDBMS has slightly different rules for how to write SQL, and even if you're an
expert with one RDBMS, it can be non-trivial to learn how to work with another
one. This tutorial shows how to use PostgreSQL, and the concepts shown here
should carry to any other system. But if you do end up using another RDBMS, be
aware that you may need to consult the documentation for that RDBMS and fiddle
around with the syntax.

###A quick taste

Here's a little preview of how SQL works. Here are the tables of data that we
created above for our imaginary news organization:

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

The SQL commands for creating these tables in the database looks like this:

    create table reporters (name varchar(80), title varchar(80), start_year int);

    create table articles (author varchar(80), title varchar(140), published_date date);

The SQL commands for populating those tables with data looks like this:

    insert into reporters (name, title, start_year) values
        ('Gabriella McCullough', 'reporter', 2009),
        ('Steven Kennedy', 'drama critic', 2012),
        ('Jalen Shaara', 'columnist', 2002);

    insert into articles (author, title, published_date) values
        ('Gabriella McCullough', 'Man, opossum reach garbage accord', '2015-07-01'),
        ('Steven Kennedy', '"The Deceit of Apricot" opens to rave reviews', '2015-07-15'),
        ('Jalen Shaara', 'What''s the Big Data? Why I''m a data skeptic', '2015-07-16'),
        ('Gabriella McCullough', 'Traffic signals restored on Tunguska Ave', '2015-07-01'); 

Here are some example queries we can run on the data, along with their results.
To get a list just of reporter's names:

    select name from reporters;

            name         
    ---------------------
    Gabriella McCullough
    Steven Kennedy
    Jalen Shaara

To find out how many articles a particular writer has written:

    select count(title) from articles where author = 'Gabriella McCullough';

    count 
    -------
        2

To get a list of articles and authors, along with the titles of those authors:

    select articles.author, reporters.title, articles.title
        from articles
        join reporters on reporters.name = articles.author;

        author        |    title     |                     title                     
    ---------------------+--------------+-----------------------------------------------
    Gabriella McCullough | reporter     | Traffic signals restored on Tunguska Ave
    Gabriella McCullough | reporter     | Man, opossum reach garbage accord
    Steven Kennedy      | drama critic | "The Deceit of Apricot" opens to rave reviews
    Jalen Shaara        | columnist    | What's the Big Data? Why I'm a data skeptic

It's like magic! 

## Clients, servers and `psql`

An RDBMS generally runs on a computer in the background, as a long-running
process (or "daemon"). This process listens on the network for incoming
requests, and then delivers responses to those requests. Software that operates
in this manner is often called "server" software. When we talk about the
"PostgreSQL server," we're specifically talking about the *software* running
on the computer. (In the case of this tutorial, you'll be running that server
software on your own computer. In the "real world," organizations will often
dedicate an entire computer, or cluster of computers, to the task of running
this software.)

Software that makes requests to and interprets responses from a server is
called "client" software. You can write SQL client software in any number
of languages (we'll see how to use Python for this purpose in a bit), but
there's one piece of client software that we'll be using a lot for learning
how to use SQL and PostgreSQL: `psql`. You can think of `psql` as being a
kind of "interactive shell" (like IPython) for SQL requests. You run `psql` and
type in a query; `psql` sends that query to the server and then displays the
response. It's a convenient way to experiment with SQL.

There are two different kinds of command you can type into `psql`: SQL
statements and `psql` "meta-commands." The "meta-commands" are for doing things
specific to the `psql` interactive shell---tasks that are outside the purview
of SQL proper, like setting the format of the input, or listing available
tables. Meta-commands always begin with a backslash (`\`).

## Using PostgreSQL

We know enough now to get started. First, run `Postgres.app` on your
computer by double-clicking on its icon. This is the Postgres "server"; as
long as it's running, you can connect to it with client software and make
requests. (You can stop the server by quitting the app: go to the elephant icon
in your menu bar and select "Quit.")

Postgres.app provides an easy way to launch the `psql` tool: simply click on
the elephant icon in the menu bar and select "Open psql." It'll open up a
Terminal window with `psql` already running. You should see something like
this:

[screenshot]

###Importing data

For the purposes of this tutorial, I'm going to have you *import* some data 
into your database. In particular, we're going to use data from the [MONDIAL project](http://www.dbis.informatik.uni-goettingen.de/Mondial/), which is a
database of geographical facts gleaned from various freely available sources.
There are a number of ways to get data into a relational database; conveniently, MONDIAL makes their database available in SQL format. Download the [statements
for the table schemas here](http://www.dbis.informatik.uni-goettingen.de/Mondial/OtherDBMSs/mondial-schema-postgresql-2010.sql) and [the statements to insert the data here](http://www.dbis.informatik.uni-goettingen.de/Mondial/OtherDBMSs/mondial-inputs-postgresql-2010.sql). Remember where you put these files!

To import the data into PostgreSQL, start `psql` as described in the previous section. Type the following command at the `psql` prompt:

    create database mondial;

... and hit Return. This command creates a new "database." A "database," by the
way, is just a name for a collection of tables. Your PostgreSQL server software
can manage multiple databases.) server can contain and manage multiple such
databases.

> Don't forget the semi-colon at the end of the `create` line! Every SQL
> statement ends with a semi-colon.

You can get a list of all the databases that are currently on your server with
the `\l` meta-command (short for "list"):

    \l

You'll see something that looks like this:

                                    List of databases
    Name    |  Owner  | Encoding |   Collate   |    Ctype    |  Access privileges  
    -----------+---------+----------+-------------+-------------+---------------------
    allison   | allison | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
    mondial   | allison | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
    postgres  | allison | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
    template0 | allison | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/allison         +
            |         |          |             |             | allison=CTc/allison
    template1 | allison | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/allison         +
            |         |          |             |             | allison=CTc/allison

The `postgres` database and the `template` databases (if present) are for
internal PostgreSQL use---you don't need to mess with them. Postgres.app also
creates a "default" database named after your OSX user. You can use this as
"scratch" space for experimentation, or just leave it alone.

Now that you've created the `mondial` database, you need to "connect" to it. To
accomplish this, use the `\c` meta-command like so:

    \c mondial

Once you've connected to a database, you can list the tables in the database
with the `\d` meta-command, like so:

    \d

At this point, you should get an error message saying "No relations found."
Which makes sense---we haven't added any data yet! In order to populate our
database, we're going to import the SQL statements from MONDIAL that we
downloaded earlier. The meta-command for importing SQL statements is `\i`.
You need to give the `\i` meta-command a parameter, which should be the
location of the file you want to import. You'll need to import the `schema`
file first. I downloaded the SQL files from above into my `~/Downloads`
directory, so I might type:

    \i /Users/allison/Downloads/mondial-schema-postgresql-2010.sql

You'll see a whole list of "CREATE TABLE" lines, which acknowledge the fact
that tables have been created. Now you can import the data itself:

    \i /Users/allison/Downloads/mondial-inputs-postgresql-2010.sql 

A bunch of `INSERT 0 1` lines will fly by, one for every record that has been
inserted.

> OSX Pro-Tip: If you drag and drop a file from Finder to a terminal window,
> the path to the file you dropped will be pasted into the program you're
> using. Handy!

Now try using the `\d` meta-command again. You'll see something that looks
like this:

                List of relations
    Schema |       Name       | Type  |  Owner  
    --------+------------------+-------+---------
    public | borders          | table | allison
    public | city             | table | allison
    public | continent        | table | allison
    public | country          | table | allison
    public | desert           | table | allison
    public | economy          | table | allison
    public | encompasses      | table | allison
    public | ethnicgroup      | table | allison
    public | geo_desert       | table | allison
    public | geo_estuary      | table | allison
    public | geo_island       | table | allison
    public | geo_lake         | table | allison
    public | geo_mountain     | table | allison
    public | geo_river        | table | allison
    public | geo_sea          | table | allison
    public | geo_source       | table | allison
    public | island           | table | allison
    public | islandin         | table | allison
    public | ismember         | table | allison
    public | lake             | table | allison
    public | language         | table | allison
    public | located          | table | allison
    public | locatedon        | table | allison
    public | mergeswith       | table | allison
    public | mountain         | table | allison
    public | mountainonisland | table | allison
    public | organization     | table | allison
    public | politics         | table | allison
    public | population       | table | allison
    public | province         | table | allison
    public | religion         | table | allison
    public | river            | table | allison
    public | sea              | table | allison
    (33 rows)

Awesome work! You've successfully imported some data into your database.

###Examining tables

The `\d` meta-command on its own shows a list of all tables. If you provide
a table name after the `\d`, you'll get a description of just that table.
For example, let's see what's in the `city` table:

    \d city

HEre's what you'll see:

                Table "public.city"
    Column   |         Type          | Modifiers 
    ------------+-----------------------+-----------
    name       | character varying(35) | not null
    country    | character varying(4)  | not null
    province   | character varying(35) | not null
    population | numeric               | 
    longitude  | numeric               | 
    latitude   | numeric               | 
    Indexes:
        "citykey" PRIMARY KEY, btree (name, country, province)
    Check constraints:
        "citylat" CHECK (latitude >= (-90)::numeric AND latitude <= 90::numeric)
        "citylon" CHECK (longitude >= (-180)::numeric AND longitude <= 180::numeric)
        "citypop" CHECK (population >= 0::numeric)

This shows you what columns are present in the table, and what *data types*
those columns contain. We see above, for example, that the `city` table
has a column called `name` whose type is `character varying(35)`. There's
also a `population` column whose type is `numeric`.

> The `\d` command also displays a list of table *indexes* and *constraints*.
> An index is a way to make a queries on a table faster by storing extra
> information about each record when it's inserted or updated. A constraint is
> an automatic "check" you can set up that ensures any data you put into the
> table meets certain criteria. We're not going to talk about indexes or
> constraints in any detail in this tutorial, but you can read more about them
> in the PostgreSQL documentation.

###Data types

Every column in a table has a *data type*. There are a number of core SQL data
types supported by nearly every RDBMS, and individual vendors may also supply
data types specific to their own software. Some of the most common data types
in SQL are:

| type | description |
| ---- | ----------- |
| `varchar(n)` or `character varying(n)` | a string that is at most *n*
characters long |
| `integer` or `int` | integer numbers |
| `float` | floating-point numbers |
| `numeric` | fractional numbers with a fixed precision |
| `date` | stores a year, month and day |
| `timestamp` | stores a year, month, day, hour, minute, and second |
| `boolean` | either `true` or `false` |

[Here's a full-list of data types supported by
PostgreSQL](http://www.postgresql.org/docs/9.4/static/datatype.html). It's
important to recognize what data types you're working with, since it changes
the way you write queries against the data, and how some features (like
sorting) will behave.

###Writing a query with `SELECT`

Enough with the preliminaries! Let's actually get some data out of the
database. The way you get data out of a SQL table is to write a `SELECT`
statement. The `SELECT` statement allows you to specify (among other things):

* which rows you want
* for the rows selected, which columns you want
* the number of rows to return
* how to sort the rows

The basic syntax for `SELECT` is this:

    SELECT fields
    FROM table
    WHERE criterion
    ORDER BY order_fields
    LIMIT number;

... where:

* `fields` is a comma-separated list of fields that you want to retrieve
* `table` is the name of the table you want to query;
* `criterion` is a SQL expression that determines with rows will be included
  (more on SQL expressions in a bit);
* `order_fields` is a comma-separated list of fields to use as the basis for
  sorting the results (e.g., if you want to sort alphabetically by the `name`
  field, put `name` here); you can optionally include the `DESC` keyword here
  to sort in reverse order.
* `number` is the maximum number of records to return.

The `WHERE`, `ORDER BY` and `LIMIT` lines are all optional: the only thing
you need for a `SELECT` statement is a list of fields and a table. SQL is
also not white-space sensitive; I wrote each clause on a separate line above,
but you're free to include new lines and extra whitespace where you will. You
could also potentially write the whole statement on a single line, if you
wanted to. (Just remember to end the statement with a semicolon.)

> NOTE: This is only a small subset of the `SELECT` statement's capabilities,
> presented for pedagogical purposes only! The actual syntax is [much more
> complicated](http://www.postgresql.org/docs/9.0/static/sql-select.html).

So, for example, let's select the `name` and `population` columns from the
`city` table, displaying only the rows where the value for `population` is
greater than seven million. Type the following query into your `psql` session
and hit return.

    SELECT name, population
    FROM city
    WHERE population > 7000000;

You'll see results that look like this:

        name     | population 
    -------------+------------
     Moscow      |    8717000
     Istanbul    |    7615500
     Shanghai    |    7830000
     Karachi     |    9863000
     Mumbai      |    9925891
     New Delhi   |    7206704
     Hong Kong   |    7055071
     Jakarta     |    8259266
     Tokyo       |    7843000
     Seoul       |   10229262
     Mexico City |    9815795
     New York    |    7322564
     Sao Paulo   |    9811776
    (13 rows)

To order these cities alphabetically, we can add an `ORDER BY` clause:

    SELECT name, population
    FROM city
    WHERE population > 7000000
    ORDER BY name;

Results:

        name     | population 
    -------------+------------
     Hong Kong   |    7055071
     Istanbul    |    7615500
     Jakarta     |    8259266
     Karachi     |    9863000
     Mexico City |    9815795
     Moscow      |    8717000
     Mumbai      |    9925891
     New Delhi   |    7206704
     New York    |    7322564
     Sao Paulo   |    9811776
     Seoul       |   10229262
     Shanghai    |    7830000
     Tokyo       |    7843000
    (13 rows)

To order these cities by descending population:

    SELECT name, population
    FROM city
    WHERE population > 7000000
    ORDER by population DESC;

Results:

        name     | population 
    -------------+------------
     Seoul       |   10229262
     Mumbai      |    9925891
     Karachi     |    9863000
     Mexico City |    9815795
     Sao Paulo   |    9811776
     Moscow      |    8717000
     Jakarta     |    8259266
     Tokyo       |    7843000
     Shanghai    |    7830000
     Istanbul    |    7615500
     New York    |    7322564
     New Delhi   |    7206704
     Hong Kong   |    7055071
    (13 rows)

Finally, to limit our result set to only the top five cities, we can include
the `LIMIT` keyword. Let's change the fields to include the country as well:

    SELECT name, country, population
    FROM city
    WHERE population > 7000000
    ORDER by population DESC
    LIMIT 5;

Results:

        name     | country | population 
    -------------+---------+------------
     Seoul       | ROK     |   10229262
     Mumbai      | IND     |    9925891
     Karachi     | PK      |    9863000
     Mexico City | MEX     |    9815795
     Sao Paulo   | BR      |    9811776
    (5 rows)

###Exploring tables with `*` and `LIMIT`

Occasionally it's useful to just "take a peek" at the data that's in a table,
without having to specify which columns and rows you want in particular. For
these purposes, you can put a `*` in the field parameter (right after the
word `SELECT`), which will include *all* of the fields in the table in your
search result. Combined with the `LIMIT` clause, you can use this to take
a look at what's in the first few rows of the table `country`:

    SELECT *
    FROM country
    LIMIT 10;

Result:

        name    | code |     capital      |   province    |  area  | population 
    ------------+------+------------------+---------------+--------+------------
     Albania    | AL   | Tirane           | Albania       |  28750 |    3249136
     Greece     | GR   | Athens           | Attiki        | 131940 |   10538594
     Macedonia  | MK   | Skopje           | Macedonia     |  25333 |    2104035
     Serbia     | SRB  | Belgrade         | Serbia        |  77474 |    7379339
     Montenegro | MNE  | Podgorica        | Montenegro    |  14026 |     672180
     Kosovo     | KOS  | Pristina         | Kosovo        |  10887 |    1804838
     Andorra    | AND  | Andorra la Vella | Andorra       |    450 |      72766
     France     | F    | Paris            | Ile de France | 547030 |   58317450
     Spain      | E    | Madrid           | Madrid        | 504750 |   39181114
     Austria    | A    | Vienna           | Vienna-Wien   |  83850 |    8023244
    (10 rows)

A quick (but, in PostgreSQL, potentially [slow](https://wiki.postgresql.org/wiki/Slow_Counting)) way to count the total number of records in a table is to use
the `count()` aggregate function:

    SELECT count(*) FROM city;

Result:

     count 
    -------
      3111
    (1 row)

This tells us that there are 3111 rows in the `city` table. (More on
aggregation below.)

##SQL expressions in WHERE clauses

As we saw in one of the above examples, the `WHERE` clause requires an
expression that returns true or false. Rows in the table for which this
expression is true will be included in the result set; rows for which this
expression evaluates to false will be skipped.

The syntax for SQL expressions is, in general, very similar to the syntax for
writing expressions in (e.g.) Python (the analog for the `WHERE` clause in
Python would be the expression following `if` in a list comprehension). There
are a number of operators which take expressions on either side; these
expressions can be either literals (such as numbers or strings that you type
directly into the query) or column names. If the expression is a column name,
then its value is the contents of that column for the row currently being
evaluated.

The supported operators in SQL are, in some cases, slightly different from
their counterparts in Python. Here are some common SQL operators:

| operator | description |
| -------- | ----------- |
| `>`        | greater than |
| `<`        | less than |
| `>=`        | greater than or equal to |
| `<`        | less than or equal to |
| `=`        | equal to (note: `=` and not `==`!) |
| `<>` or `!=` | not equal to |

To check to see if a value is `NULL` or missing, use the special expression `IS
NULL` (or, for the converse, `IS NOT NULL`).

> You can also use basic mathematical expressions in SQL, to check if (e.g.)
> the sum of the value in two columns is greater than a particular value.
> [Here's a
> list](http://www.postgresql.org/docs/9.0/static/functions-math.html) of the
> supported mathematical operators in PostgreSQL. 
> 

Here's a quick example of using the `>` operator to find all rows in the `lake`
table with an `area` value of greater than 30000:

    SELECT name, area, depth FROM lake WHERE area > 30000;

Results:

          name       |  area  | depth 
    -----------------+--------+-------
     Dead Sea        |  41650 |   378
     Caspian Sea     | 386400 |   995
     Ozero Baikal    |  31492 |  1637
     Lake Victoria   |  68870 |    85
     Lake Tanganjika |  32893 |  1470
     Great Bear Lake |  31792 |   446
     Lake Huron      |  59600 |   229
     Lake Michigan   |  57800 |   281
     Lake Superior   |  82103 |   405
    (9 rows)

###More sophisticated WHERE clauses with `AND` and `OR`

You can construct more sophisticated expressions in your `WHERE` clauses using
the `AND` and `OR` operators. These work just like their Python counterparts:
on either side, write an expression. If both expressions return true, then
the entire expression with `AND` returns true. If either returns true, then
the entire expression with `OR` returns true.

As a quick example, let's find all of the cities in Finland that meet a
particular level of population. The cities in the `city` table are linked to
their country with a country code in the `country` field. We can determine
what that country code is by running a `SELECT` on the `country` table:

    SELECT name, code FROM country WHERE name = 'Finland';

Results:

      name   | code 
    ---------+------
     Finland | SF

Now we can query the `city` table for Finnish cities:

    SELECT name, country, population FROM city WHERE country = 'SF';

Results:

         name     | country | population 
    --------------+---------+------------
     Mariehamn    | SF      |       9500
     Tampere      | SF      |     170097
     Lahti        | SF      |      94234
     Haemeenlinna | SF      |      42000
     Kuopio       | SF      |      78571
     Lappeenrenta | SF      |      53922
     Kotka        | SF      |      58345
     Rovaniemi    | SF      |      31000
     Mikkeli      | SF      |      28000
     Jyvaeskylae  | SF      |      65511
     Joensuu      | SF      |      44000
     Oulu         | SF      |      97898
     Pori         | SF      |      77763
     Turku        | SF      |     161292
     Helsinki     | SF      |     487428
     Espoo        | SF      |     160480
     Vaasa        | SF      |      54275
    (17 rows)

Let's say we want to find all Finnish cities with a population of at least 100000 people. We can write that query like so:

    SELECT name, country, population
    FROM city
    WHERE country = 'SF' AND population > 100000;

Results:

       name   | country | population 
    ----------+---------+------------
     Tampere  | SF      |     170097
     Turku    | SF      |     161292
     Helsinki | SF      |     487428
     Espoo    | SF      |     160480
    (4 rows)

Another example: the `lake` table has a list of lakes, along with (among other
things) their area and depth. Let's say that we want to find a list of Earth's
most ~remarkable lakes~, based on those lakes' depth and area. To get a list of
lakes that are either (a) 500 meters deep or (b) have a surface area of more than 30000 square meters:

    SELECT name, area, depth
    FROM lake
    WHERE depth > 500 OR area > 30000;

Results:

           name       |  area  | depth 
    ------------------+--------+-------
     Dead Sea         |  41650 |   378
     Caspian Sea      | 386400 |   995
     Issyk-Kul        |   6236 |   668
     Lake Toba        |   1103 |   505
     Ozero Baikal     |  31492 |  1637
     Lake Victoria    |  68870 |    85
     Lake Tanganjika  |  32893 |  1470
     Lake Malawi      |  29600 |   704
     Great Bear Lake  |  31792 |   446
     Great Slave Lake |  28568 |   614
     Lake Huron       |  59600 |   229
     Lake Michigan    |  57800 |   281
     Lake Superior    |  82103 |   405
     Crater Lake      |   53.2 |   594
     Lake Tahoe       |    497 |   501
    (15 rows)

##Further reading

In part 2 of this tutorial, we'll discuss how to aggregate data and how to
join tables. In subsequent tutorials (if there's time!) we'll talk about how
to design your own database schemas. In the mean time, here are some good
introductory resources on SQL:

* The [PostgreSQL tutorial](http://www.postgresql.org/docs/9.4/static/tutorial.html) is a thoughtful, thorough introduction to PostgreSQL, `psql`, and relational database concepts in general.
* [SQL Teaching](https://www.sqlteaching.com/) has a series of online, interactive tutorials about making queries.
* If you're looking to buy a book, I always recommend O'Reilly's "Head First" series. Here's [Head First SQL](http://shop.oreilly.com/product/9780596526849.do).


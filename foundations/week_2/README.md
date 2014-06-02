# Week 2

## Monday June 2, 2014

### Notes

#### Downloading a file

First, we tried to figure out how to download a file using Python. Googling around, we came across [How do I download a file over HTTP using Python?](http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python) on StackOverflow. The *green checkmark* shows the answer that was selected as best, but scrolling down we saw something that helped us out a little more.

```python
import urllib
urllib.urlretrieve("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
```

Why'd we do this `import urllib` thing? We seem to do it often enough! We've done `import csv` before, too. `import` takes an external **module** (a bunch of code someone else has written that happens to have a name) and adds its abilities to our code. If you'd like a big long list of modules, try the [Python Module Index](https://docs.python.org/2/py-modindex.html).

We tried to see what the docstring was for urlretrieve (shift+tab) and got this

```python
urllib.urlretrieve(url, filename=None, reporthook=None, data=None)
```

It was also pretty easy to guess what the arugments were! Using that, we changed our url and our filename to be something more appropriate, like

```python
urllib.urlretrieve("http://jonathansoma.com/lede/dogs.csv", "dogs.csv")
```

and so now we had `dogs.csv` downloaded to our machine.

#### Going through the CSV

Our first instinct was to open it like we did last time, like this:

```python
dogs = open("dogs.csv","rb")
```

But then we Googled [how to open a csv using python](https://www.google.com/search?client=safari&rls=en&q=how+to+open+a+csv+using+python&ie=UTF-8&oe=UTF-8) and came up with something from [the Python documentation](https://docs.python.org/2/library/csv.html).

  >>> import csv
  >>> with open('eggs.csv', 'rb') as csvfile:
  ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  ...     for row in spamreader:
  ...         print ', '.join(row)
  Spam, Spam, Spam, Spam, Spam, Baked Beans
  Spam, Lovely Spam, Wonderful Spam

Lots of garbage was hanging out in there! The last two lines were the output of the example, and the `>>>` and `...` are just some "this is code" junk. So we're left with this...

```python
import csv
with open('eggs.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print ', '.join(row)
```

We needed to make it make sense with our code, so we changed `eggs.csv` to `dogs.csv` and `spamreader` to `dogcsv`. We used the docstring to figure out what `delimiter` and `quotechar` (more info - [delimiters](http://en.wikipedia.org/wiki/Delimiter-separated_values)), and figured our delimiter is `','` and we could get rid of `quotechar`.

```python
import csv
with open('dogs.csv', 'rb') as csvfile:
     dogcsv = csv.reader(csvfile, delimiter=',',)
     for row in dogcsv:
         print row
```

....more is coming!

### Links

I put together an IPython notebook about [looping through a CSV](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/foundations/week_2/Looping%20through%20a%20CSV.ipynb) that *might* help out with some of those `row[0]` questions.

[Command line basics](https://github.com/denten/dhnotes/wiki/cli-basics) from Dennis.

### Homework

You can find the **complete dogs.csv** at `http://jonathansoma.com/lede/dogs.csv`. Using a new IPython notebook, find out...

1. How many dogs are registered in New York City? *Hint: if you check out the IPython notebook above, it talks about how to convert the csv.reader variable into a list, which might give you an easy way to do it*
2. How many dogs are registered in Brooklyn? Staten Island? Queens? Manhattan? Bronx?
3. How many dogs are named Max in the [Lower East Side](http://www.city-data.com/neighborhood/Lower-East-Side-New-York-NY.html)?
4. How many dogs are named Max in [Bed Stuy](http://www.city-data.com/neighborhood/Bedford-Stuyvesant-Brooklyn-NY.html)?
5. How many dogs have the color [brindle](http://en.wikipedia.org/wiki/Brindle) as their first or second color?
6. Ask the user for their name (you're gonna have to Google how to get user input in python!). Then find out how many dogs in New York have that name.

Remember to add in comments about where you found answers and what you're trying to do during each step!

When you've done what you can (...everything, right?), save the IPython notebook by going to `File > Download as...` and click `IPython Notebook`. A `.ipynb` will be downloaded to your computer. E-mail that file as an attachment to `jonathan.soma@gmail.com`.
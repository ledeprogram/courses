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

```
>>> import csv
>>> with open('eggs.csv', 'rb') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print ', '.join(row)
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

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
     dogcsv = csv.reader(csvfile, delimiter=',')
     for row in dogcsv:
         print row
```

Great! Looking good. Now we want to see how many dogs are in the sample. We need to do a few things - you'll want to add your code in under my comments. I'll add in the actual code after Wednesday!

```python
import csv
with open('dogs.csv', 'rb') as csvfile:
    # Start off with 0 dogs
    
    dogcsv = csv.reader(csvfile, delimiter=',')
    for row in dogcsv:
        # Increase the counting by 1
        
        print row
    # Print the number of dogs we came across
    
```

Why all the indenting? Indenting shows that some blocks of code (the indented part) belongs to something above it. Like when you're making a nested list, like this...

- Canines:
  - Dog:
    - Afghan Hound
    - Pomeranian
    - Golden Retriever
  - Wolf
- Felines:
  - Lion
  - Tiger
  - Cat

Indenting is very important in Python! You'll probably get errors if you mess up the indenting. For example...

```python
if 2 > 3:
  print 'I can do math!'
  print '2 is greater than 3'
```

If you run that in IPython, you won't get any output. But if you do this...

```python
if 2 > 3:
  print 'I can do math!'
print '2 is greater than 3'
```

It'll output `2 is greater than 3`! But not because `2 > 3` is `True`, but because Python doesn't consider `print '2 is greater than 3'` to be inside of the `if 2 > 3` block. Oh yeah, and things that are indented together are generally called **block**.

#### Aside: Things being done different ways

It looks like we accidentally came across two ways of opening a CSV file:

```python
csvfile = open("dogs.csv","rb")
dogcsv = csv.reader(csvfile, delimiter=',')
```

```python
with open('dogs.csv', 'rb') as csvfile:
    dogcsv = csv.reader(csvfile, delimiter=',')
```

What's the difference? Well, the first one looks kind of standard. Just things in a row, assigning variables, la la la. The second one involves indenting, and this new `with ... as ...:` structure.

Just by looking at it, we can tell the second one is using a **block**, thanks to the indentation and the way the first line ends in `:`. Since it's indented, we should assume that something from the top part applies to the indented part.

But what is it? Well, we're doing something with a variable called `csvfile` that didn't exist before, and it's in the top `with` part, so let's make a wild guess that the `csvfile` variable was created **just for the indented block**. Every time you'd want to use `csvfile`, you'd need your code to be indented.

For example, think about the difference between these two:

```python
with open('dogs.csv', 'rb') as csvfile:
    print 'hello'
    dogcsv = csv.reader(csvfile, delimiter=',') 
```

```python
with open('dogs.csv', 'rb') as csvfile:
    print 'hello'
dogcsv = csv.reader(csvfile, delimiter=',') 
```

They'll both print `hello`, but the second one won't successfully create `dogcsv` from `csvfile`. Outside of that indented block, `csvfile` doesn't mean anything! It'd be like if we changed our list above from...

- Canines:
  - Dog:
    - Afghan Hound
    - Pomeranian
    - Golden Retriever
  - Wolf

...on over to...

- Canines:
  - Dog:
    - Afghan Hound
    - Pomeranian
  - Golden Retriever
  - Wolf

It's no good, because "Golden Retriver" belongs under "Dogs"! So, in summary: there are a million ways to do things (and they might all be confusingly similar), and indenting is important.

#### Getting columns from the row

This was the part where I became spectacularly inept at explaining how loops work. You might want to try out my IPython notebook about [looping through a CSV](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/foundations/week_2/Looping%20through%20a%20CSV.ipynb) to learn more.

So we wanted to grab the dog names. 

```python
import csv
with open('dogs.csv', 'rb') as csvfile:
     dogcsv = csv.reader(csvfile, delimiter=',')
     for row in dogcsv:
         print row[0]
```

`row[0]` is getting **the 0th element of the row**. I think that's the best way to remember what [n] does - remember it's **not** the 0th row. What's the first element of the row? If you look at the csv, it's the dog's name. So the above code should print out the dog's name.

#### Common patterns

Looping through things

```python
for element in list_of_things:
  # Do something with that element
```

Counting the number of anything

```python
len(list_of_things)
```

You can also do this for list-ish things (like `csv.reader`)

```python
# Start off with 0
count = 0
for element in list_of_things:
    # Add one to increment count 
    count = count + 1
# Display count
print count
```

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

## Wednesday, June 4, 2014

**Preemptive notes:** Run this to get some sample dog homework responses on your IPython Notebook servers

```python
import urllib
urllib.urlretrieve("https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/week_2/dog-homework-responses.ipynb", "Sample Dog Homework Responses.ipynb")
```
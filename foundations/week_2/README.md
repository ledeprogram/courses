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

#### Homework!

For your homework, write up some lab notes in Markdown! I'd recommend taking your old notes and converting them to Markdown, just so we can end up keeping them all in the same place. Then, if you're feeling cool and fun, read through the code we imported into your IPython Notebook and make notes about what you've learned.

(PS You don't need to reproduce your whole IPython notebook in the lab notebook! Just your thought process, code snippets, and anything else your Future Self will find useful. You can shove a bunch of your code and comments in there and annotate it all, but the ol' cut-and-paste ain't gonna cut it.)

Read below for more!

#### Dog Homework Stuff

**Preemptive notes:** Run this to get some sample dog homework responses on your IPython Notebook servers. You can read this code to understand things other people tried, or just gasp at the fact that there are one million ways to do even the most sinmple thing.

```python
import urllib
urllib.urlretrieve("https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/week_2/dog-homework-responses.ipynb", "Sample Dog Homework Responses.ipynb")
```

Make a new IPython project, past the above into the first cell, run it, then go back to the root of your IPython server - there should now be a new project called `Sample Dog Homework Responses`.

I'll be publishing an annotated version of that code eventually, but it should be good enough for now.

### Lab notes

You see what I'm doing here? These are lab notes. *You* can write lab notes! You *will* write lab notes!

See those aggressive italics? That's **Markdown**. That's what you'll be writing your lab notes in.

#### Markdown

Markdown is a compromise between writing in a terrible, inaccessible file format *cough*Word*cough*, and writing in plain-jane no-frills text. By using asterisks, pound symbols and underscores you can transform your text into ~*_SOMETHING INCREDIBLE_*~!!!!!

(**Big not-so-secret note:** This is all written in Markdown! As I'm writing it, it [looks just like this](https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/week_2/README.md) - might be useful to check it out to see how I format a thing or two.)

To learn Markdown syntax, while you can check out Daring Fireball's [tiny-fonted guide](http://daringfireball.net/projects/markdown/syntax), I find the [Mastering Markdown GitHub Guide](https://guides.github.com/features/mastering-markdown/) or [this cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) way more accessible.

Honestly, though, at first you'll probably want to make sure you're typing it out right as you go along. It'll be like that [side-by-side thing Dennis used during class](http://dillinger.io), but it'll be one that can save files to your own computer. Mac users should try out [Mou](http://mouapp.com) and Windows users can check out [MarkdownPad](http://markdownpad.com). Once you're a complete kingpin you can just write it straight in your plain text editor.

You save Markdown files just the same as you'd save any other file - just use the extension **.md** if it asks you for one, just like Word files are **.docx**. The only difference is if you're editing them plain (try opening them in TextWrangler or NotePad++), you can't see all the formatting. You'll need to pop them into Mou or Dillinger or the like to be able to see what it looks like displayed.

(**Prophecy of Next Week:** We're going to upload your notes to GitHub, where it will hide the code you've written and only display beautiful, beautiful text.)

#### What are lab notes?

Lab notes cover everything you've done during a project, kind of like what I've done above. They should probably include the following:

- Your thought process
- Things that worked
- Things you tried that didn't work
- Things you thought or felt or threw keyboards about
- Especially helpful sites
- A chonological walkthrough of what you were up to
- Snippets of code
- I'm honestly just trying to make this list really long so you know that I really do mean everything.

If you keep good lab notes as you're going along, you'll be able to step back in time to see what your mindset was. Us people who already know how to program are mostly *complete garbage* at teaching you to program, because *we already understand everything*. The best possible teacher you have is *yourself*, especially the version of yourself that takes notes about everything as you go along.

Important phrases you should be typing are **I was trying to X, but then Y happened**, **I was wondering how to X, so I found this page/code**, **we learned X but I was wondering about how to do Y**. And, you know, everything and anything else. Think of it like the most secret personal diary of struggles that you've ever had, except it's about *programming* and we're going to try to con you into making it public.

You can keep your lab notes in a single big long file if you want, but week-by-week might be best. Otherwise it'll be a big long stream! No pressure, though. Do what works.

#### What are we doing with them?

**First**, lab notes are awesome for Future You. You can go back when you're strugging and read them and find out when you did something earlier on that worked for you. Code snippets from the past are *invaluable*.

**Second**, lab notes are awesome for other people. We're going to (eventually) be putting them up on [GitHub](https://github.com), which is (more or less) a big ol' super-social code-sharing site. You can make them private if you really want, but think of the WORLD!

**Third**, when you explain something, you learn it better - it's a variation on [Rubber Duck Debugging](http://en.wikipedia.org/wiki/Rubber_duck_debugging).

#### Markdown notes vs. notes in IPython

Yes, yes, you can type Markdown in IPython cells. When we want to share it or keep it or move it around, though, you'll want it to be portable. You'll see more next week!
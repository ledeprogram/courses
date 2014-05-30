# Week 1: Wednesday, May 28

First we did **introductions!** I'm of course Soma, and most easily found on Twitter at [@dangerscarf](https://twitter.com/dangerscarf) if you have questions about any of this. Longer inquiries can head on over to [jonathan.soma@gmail.com](jonathan.soma@gmail.com).

## IRC: Internet Relay Chat

A chat room for secretly whispering during class. To log in you can download [Colloquy](http://colloquy.info) or Macs or [mIRC](http://www.mirc.com) for Windows machines. The room to join is **#ledeprogram** on **chat.freenode.net**.

## The Tiniest Overview of Programming languages

**Programming languages** are the words and symbols that make computers Do Stuff. In the end they can all more or less do the exact same sorts of things, but some have more parenthesis or support for language processing or [aren't based on English](http://en.wikipedia.org/wiki/Ezhil_(programming_language)) or all sorts of things.

**[JavaScript](http://skillcrush.com/2012/04/05/javascript/)** runs in your browser and is responsible for annoying pop-ups and neat interactive maps. It's being used on the server-side these days, too. ([some notes on frontend vs backend](http://skillcrush.com/2012/04/17/frontend-vs-backend-3/))

**Python**, **Perl**, and **Ruby** are all *scripting languages*, which means they're good for writing quick small programs (pedants, please spare me). Don't get me wrong, they're also perfectly good for writing larger programs, it's just that they're exceptionally good at the small stuff. **Perl** has traditionally been the domain of sysadmins who take care of servers, **Ruby** is for hipsters&dagger; and web site backends, and **Python** is for number-crunching, language-processing, and academia. Repeat these stereotypes to people if you'd like to get yelled at.

**Java** and **[C++](http://skillcrush.com/2012/05/30/c-c-c-and-objective-c/)** are *compiled languages*, which run on [servers](http://skillcrush.com/2012/04/25/web-server-3/) and are much faster than scripting languages. They're a pain to write, though, and require a lot more curly braces than Python.

### Other non-programming languages

[HTML](http://skillcrush.com/2012/04/02/html/) and [CSS](http://skillcrush.com/2012/04/03/css/) are actually not programming languges! HTML is a *markup language*, which describes that certain parts of content are on the web (here is a title, here is a paragraph, etc), and CSS is a *presentation language*, which can make things change colors and get borders and be larger or smaller and fun stuff like that.

**SQL**, a.k.a. *Structured Query Language* is a language used to talk to databases. You'll learn it in Data &amp; Databases!

## Reading Python

We saw a lot of examples in class, checking out code that was [unreadable &amp; uncommented](unreadable-uncommented.py), [unreadable &amp; commented](unreadable-commented.py), [readable &amp; uncommented](readable-uncommented.py), and finally [readable &amp; commented](readable-commented.py).

People are really into the [Zen of Python](http://legacy.python.org/dev/peps/pep-0020/) as a series of edicts about how to write Python, but it might just be [too zen to be of any use](http://stackoverflow.com/questions/4506563/what-is-the-pythonic-way-of-programming#comment4932944_4506587). Just keep your code readable and add a lot of comments - that way you'll know what you were doing when you read your code weeks later!

## Writing Python

#### Rule 1: NO FEAR

Programming is all about Googling error messages, reading code that doesn't make sense, and crossing your fingers that you didn't forget a parenthesis. **Every once in a while you type things, too.** No matter what, though, the first step to being able to rock it is to not be *too* intimidated. Just think of it as a foreign language that doesn't have to be pronounced! 

#### Learning Python outside of class

You all asked me about this a ton! [Learn Python the Hard Way](http://learnpythonthehardway.org) is the number one best (cheapskates can scroll until you see the *free to read online* link), but you can also check out the much-maligned-by-me [Codecademy course](http://www.codecademy.com/tracks/python).

My personally recommended way to learn is *do whatever works*.

#### What we talked about in class

First we did [Hello world](http://en.wikipedia.org/wiki/Hello_world_program), because *it's the law*.

Then we talked about Python [data types](https://docs.python.org/2/library/datatypes.html), which are much nicer than what that page seems to imply. **str** and **int** were the ones we started off with (strings and integers, respectively).

**Error messages** are your new best friend. Or at least they'll never leave you alone, and if you don't learn to love them you'll probably go insane. They also teach you how to Google and solve problems! The most popular one seems to be syntax errors, which usually means something was typed incorrectly.

**Variables** are handy bags to store your informaiton in. After saying `name = "Soma"` we can just use `name` all over the place instead of `"Soma"`. As a result, something like `name.upper()` will give us `"SOMA"`!

We learned about using &lt;shift&gt;+&lt;tab&gt; to bring up  [docstrings](http://docs.python-guide.org/en/latest/writing/documentation/), so we can try to figure out what the heck `glob` means. We also learned about using `.`+&lt;tab&gt; to get a list of methods we can use on an object. If nothing's coming up, run your code! If you're using it on `name`, for example, maybe IPython doesn't know what `name` is yet.

We also brushed up against methods and functions. Functions were roughly defined as `len` in `len(name)` and methods as the `upper` part of `name.upper()`. We learned you can pass arguments or parameters to them, like when we sent `"a"` to a method with `"Soma".count("a")`.

You can find most of that code right on over in [Hello world.ipynb](Hello world.ipynb).

**Lists** came up near the end, where we had `[5, 2, 7]` and tried to figure out how to count all those numbers up. We also talked about how to think about keeping running totals and writing **pseudocode**, which is sort of what the comments below are.

```python
# Open the file
total = 0
# Go through all the worksheets
    # Count the number of lines of code
    count = worksheet.lines_of_code
    total = total + count
# Print the total number of lines of code
print total
```

Finding out what a list is, and sorting it

```python
worksheets = [5, 2, 7,5,6,7,8,8]
type(worksheets)
worksheets.sort()
print worksheets
```

How do you get the final element of a list? Math!

```python
worksheets = [5, 2, 7,5,6,7,8,8,2,3,4,5]
worksheets[len(worksheets) - 1]
```

## Things to Do For Fun this Weekend

**Subscribe to the [NICAR](http://www.ire.org/nicar/) email list!** It's like being in the friendlist computer-y newsroom on earth. [Signup instructions are over here](http://www.ire.org/resource-center/listservs/subscribe-nicar-l/). You might want to [set up a filter](http://mashable.com/2012/06/22/gmail-filters/) to mark it as read when it comes in, though, otherwise you'll think you got real popular.

**Read a lot of angry online people being angry online** about whether other people are programming in [The Right Way](https://news.ycombinator.com/item?id=7795216), and if using Google makes you a horrible inhuman beast.
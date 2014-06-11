# Week 3

## Monday June 9, 2014

Covered: Working with [GitHub](https://github.com), [functions](http://learnpythonthehardway.org/book/ex18.html)

### Notes: GitHub

GitHub is a social coding platform, made up of *repositories* that store code (and anything else). You can collaboratively work on projects, submit changes to other peoples' projects, and open up bug reports. You can check out [my Tabletop.js project](https://github.com/jsoma/tabletop) for a good example!

*git* itself is a *version control system*, a way of keeping track of changes and versions instead of just leaving all of your code on your computer. That way when you accidentally delete something or break your code you can step back into an older version! 

These versions are all based on *commits*, which are series of changes. If I add a in couple new files and change some code, then I'll make a commit to say "this is a new version." Or maybe I just change one line and decide to commit!

GitHub doesn't know about your commits until you push, though. Otherwise they just live on your computer!

Useful git commands after you've created a new repository, (stolen from [Dennis](https://github.com/denten/dhnotes/wiki/github-workflow))

`git init` will tell git to start watching the current directory
`git add foo.txt` will add a new file into your respository. You can also do `git add .` to add all new files in.
`git commit -m "my first commit notes"` will create your first commit for you. You'll want to use a descriptive message, and make sure you've got both your beginning and end quotes.
`git remote add origin git@github.com:username/reponame` teaches your local repository that there's another repository on github it will talk to in the future. You'll only need to do this one once. 
`git push -u origin master` sends your changes on over to GitHub. Refresh your repository page and you'll see them right there!

My usual workflow once a repository has been created is to add all new files, create a new commit, and push it all up.

```
git add .
git commit -a -m "Here is a new commit"
git push
```

After you run `git push -u origin master` the first time you'll be able to use plain `git push` afterward, and git will know you mean to push it up to GitHub.

### Notes: Functions

When I wake up in the morning, I don't go downstairs and take out an egg and turn on the stove and crack the egg in a pan and wait while it cooks and get out a plate and get out a fork and take the egg out of the pan and turn off the stove and put the egg on my plate and put the egg in my mouth and chew it and swallow and repeat until the egg is gone. I go downstairs and I **eat breakfast**! 

"Eating breakfast" is just shorthand for that really long description above, and programming has its own version of that: **functions**.

`len` is a function, you use it like this...

```python
len("Your name")
```

Will give you `9` back. But behind the scenes `len` is doing all sorts of stuff! What kind of stuff? Well, I don't know, I just know it's somehow getting the length of whatever I pass it as an argument.

#### The Dinner Party

Imagine if I'm having a load of people over for dinner, and I need to greet them all. If I had four folks coming over, I might write some code a little bit like this:

```python
name = raw_input("What is your name? ")
print "Hello, " + name
name = raw_input("What is your name? ")
print "Hello, " + name
name = raw_input("What is your name? ")
print "Hello, " + name
name = raw_input("What is your name? ")
print "Hello, " + name
```

But good lord, that looks horrible! What if I want to change it to say "Howdy" instead of "Hello"? That's four spots I'd have to change it in!

There's a programming concept called [Don't Repeat Yourself](http://en.wikipedia.org/wiki/Don't_repeat_yourself), which argues that when you find yourself repeating the same code again and again there's probably an improvement you could make somewhere (the LOLish opposite is [W.E.T.](http://en.wikipedia.org/wiki/Don't_repeat_yourself#DRY_vs_WET_solutions), aka "we enjoy typing" or "write everything twice"). For dinner party example, we can break it into a function like this:

```python
def greeting():
    name = raw_input("What is your name? ")
    print "Hello, " + name

greeting()
greeting()
greeting()
greeting()
```

Notice how both `def greeting():` up top and `greeting()` below don't have any arguments. If you know who's coming to dinner, you might do something more like this

```python
def hello(name):
  print "Hello, " + name

hello("Adam")
hello("Samatha")
hello("Thomas")
```

The `def` part is where you're telling Python, "Hey, I'm making a function here!". The number of arguments in the function definition should match the number of arguments when you're calling the function, otherwise you'll get an error that looks something like

```
TypeError: your_function() takes exactly 1 argument (2 given)
```

#### Return Values

Let's say we wanted to reinvent the wheel and do some addition. Might look like this:

```python
def add(a, b):
  a + b

print add(2, 3)
```

Seems good, right? Nope! Instead of getting `5` to show up when we run our program, instead we get 

```
None
```

That's because our function isn't set up to give anything back when it finishes - it's adding up `a` and `b`, sure, but it's keeping the result to itself! The way you send information back is with the `return` statement.

```python
def add(a, b):
  a + b

print add(2, 3)
```

So now our code will return `5`.

A good question in class was why can't you just do...

```python
def add(a, b):
  print a + b

add(2, 3)
```

Because it would definitely print `5` for you! The thing is, though, the `add` function is supposed to add the numbers, not print the answer. What happens if I try to do...

```python
print add(2,3) + add(3,4)
```

You'd like it to print `12`, but instead you get an error! Because the new version of `add` doesn't have a return value, that code is actually saying `print None + None`. With a return statement, though, everything works fine.

```python
def add(a, b):
  a + b

print add(2, 3) + add(3, 4)
```
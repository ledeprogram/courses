---
title: Foundations of Computing 
date: 5/28/14 - 7/14/14
time: M & W 10am - 1pm 
affiliation: Columbia University, Lede Program
instructors: Jonathan Soma, Dennis Tenen
location: 601b Pulitzer Hall*

---

\* We will be meeting in room 601b for the first week or so and then according to the [room schedule](https://drive.google.com/file/d/0B4OAOue0b3VMNXJ1Z1loaGg4bWc/edit?usp=sharing).  

> An introduction to the ways in which the computer and data technologies can be partners in creative practices. We will emphasize writing code over point-and-click interfaces, presenting the computer as a programmable object. Through a series of projects, students will move from exploratory sessions, to writing small programs, to sharing code with others in class. They will learn by making, and in the process master a "scripting language" like Python or Ruby. Projects will examine and extend existing technologies in the digital humanities, computational journalism, architecture, and design; and will likely deal in text and images, in human relationships as exhibited through social networks, in map-making, and in reporting.

## Week 1: Intro to Python 

**Focus**: Get comfortable running Python at the command line and understand that seeking out help is 90% of coding

### Wednesday 5/28

Course philosophy  
Course tools: iPython notebook, bash, Piazza, IRC, GitHub  
  
Introduction to pseudocode  
Python hello world:  

- print, # comments   
- int, str, list, dictionary, tuple  
- variables  
- basic operators  
- basic control structures   
- loops and logic  
- iterables

**TODO**: Lab notebooks. File cleanup. Posting to Piazza.  

## Week 2: Terminal Basics 

**Focus**: Learn to read and write basic (clean, commented, beautiful) Python.  

**Week Inspiration:** [Dogs of NYC](http://project.wnyc.org/dogs-of-nyc/)  

### Monday 6/2

- Algorithmic thinking with [Dogs of NYC data](https://www.google.com/fusiontables/data?docid=1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ#rows:id=1)

- Writing readable code 
- Dictionaries (csv.reader vs. csv.DictReader)
- for...in
- Functions
- Programmer's mindset
- Getting help: living with syntax errors, docstrings, SE, IRC 
- [Terminal bash basics](https://github.com/denten/dhnotes/wiki/cli-basics): (`pwd`, `ls`, `cd`, `cat`, `man`, `cp`, `mv`, `touch`, `nano`, flags, pipes, `cd ~`, `cd /`)  
- Exploring your file system (files and folders). Binary, text, hex.

### Wednesday 6/4

- more on the Programmer's mindset
    - divide and conquer
    - be lazy
    - no black boxes
    - python specific stuff
- text and data workflows
- language interpreters
- taking control of IDE
- Lab notebooks
- code and data
- Markdown
- Pandoc
- Version control
- Github workflow
- finish going through the Dogs code

**Resources:** [Sustainable Authorship in Plain Text](http://programminghistorian.org/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown)

## Week 3: Functions and GitHub

-**Week Inspiration:** [Quakebot](http://www.slate.com/blogs/future_tense/2014/03/17/quakebot_los_angeles_times_robot_journalist_writes_article_on_la_earthquake.html)

### Monday: 6/9

- Installing GitHub, pushing and pulling
- Writing your own functions

### Wednesday 6/11

- Physical deconstruction (or construction!) of computing concepts
- More on functions, implementing baby Quakebot

Homework: [Earthquakes](https://github.com/ledeprogram/courses/blob/master/foundations/week_3/eq_homework.py)

## Week 4: Working with the Census and an introduction to APIs

**Focus:** Use another library, a simple key-based API, understand Census data

**Week Inspiration:** [Almost every story ever uses ACS data](http://articles.latimes.com/keyword/american-community-survey). [Quakebot](http://www.slate.com/blogs/future_tense/2014/03/17/quakebot_los_angeles_times_robot_journalist_writes_article_on_la_earthquake.html)

### Monday 6/16

- APIs
- The [census package](https://github.com/sunlightlabs/census) from Sunlight Labs
- Census terminology
    - FIPS codes
    - Blocks, tracts
    - MSAs
    - [etc](https://www.census.gov/geo/reference/)

### Wednesday 6/18

- .gitignore for API keys
- Working with Twitter API 

## Week 5: Networking

### Monday 6/23

- superpowers: code, terminal, server, network
- communication theory: sender, message, transmission, noise, channel, reception, receiver  
- Inventing the internet
- ping, traceroute
- connection, packet switching, datagram
- layers and protocols: [physical](http://www.linfo.org/physical_layer.html) (wi-fi, bluetooth), [data](http://www.linfo.org/data_link_layer.html) (bits into packets), [network](http://www.linfo.org/network_layer.html) (ip), [transport](http://www.linfo.org/transport_layer.html) (tcp, udp), [session](http://www.linfo.org/session_layer.html), [presentation](http://www.linfo.org/presentation_layer.html) (ascii, midi, mpeg), [application](http://www.linfo.org/application_layer.html) (http, bittorrent)
- mac, dns, ip address
- ports, firewall
- Cloud computing w/ aws
- Moving files: `ssh`, `scp`, `rsync`, `wget`  

### Wednesday 6/25

- pretty good privacy (PGP)
- public and private keys
- Send an encrypted email message
- tor, vpn, ssh tunnels
- bitcoin

**Resources**: [Cyberspace Atlas](http://personalpages.manchester.ac.uk/staff/m.dodge/cybergeography/atlas/atlas.html); [How PGP Works](http://web.archive.org/web/20140501185547/http://www.pgpi.org/doc/pgpintro/); [Mailvelope](http://www.mailvelope.com/), [Keybase](https://keybase.io/); <https://emailselfdefense.fsf.org/>; [Chapter 1](https://courseworks.columbia.edu/access/content/group/JOURJ4001_001_2014_2/tcp-ip-illustrated-second.pdf) from TCP/IP Illustrated by W.Richard Stevens, Second Edition.

## Week 6: Data Visualization 

**Focus:** Make visuals of your data

**Week Inpiration:** [How FiveThirtyEight Got the Nigerian Kidnappings Analysis Wrong](http://web.archive.org/web/20140516152339/https://source.opennews.org/en-US/articles/gdelt-decontextualized-data/)  

**Resources:** [Statistics Done Wrong](http://www.statisticsdonewrong.com/), [Demystifying Networks](http://web.archive.org/web/20140501191102/http://www.scottbot.net/HIAL/?p=6279), [Introduction to social network methods](http://www.faculty.ucr.edu/~hanneman/nettext/)

### Monday 6/30

- Bad stats
- Tufte
- Working with data
- Data visualization
- Matplotlib
- EDA

### Wednesday 7/2

- Matplotlib
- Bokeh
- Google TakeOut

## Week 7: Mapping

**Focus:** Making non-interactive and interactive maps (matplotlib and TileMill, respectively)

### Monday 7/7

- Shapefiles
- Joining data (Join with week 4 via FIPS?)
- Color schemes
    - diverging, sequential, qualitative
    - color blindness
    - RGB vs HSB
- Geocoding points

### Wednesday 7/9

- matplotlib
- [TileMill](https://www.mapbox.com/tilemill/)

## Week 8: Physical Computing

### Monday 7/14

- Physical computing
- Sensor tech
- Drone control

**Lab:** [Phidget](http://www.phidgets.com) music machine.

***Resources***: [Take the Linux Filesystem Tour](http://web.archive.org/web/20140501190339/http://tuxradar.com/content/take-linux-filesystem-tour/)

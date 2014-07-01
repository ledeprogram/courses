---
title: Data and Databases
date: 5/28/14 - 7/14/14
time: T & Th
affiliation: Columbia University, Lede Program
instructors: Adam Parrish, Matthew Jones, Dan Vegeto (TA)
Room: Pulitzer 607B
State of Being: Ec(-2)static
---


description: Consideration of both the scientific and social implications of counting, of turning the world into bits. Through the process of gaining fluency in the use of Python, students will spend some time thinking through representations of core "data types" like time, location, text, image, sound and relationships (or networks), and the computational "affordances" associated with each. Students will study several common metaphors for organizing and storing data – from structureless key-value stores, to document collections like MongoDB, to a single table or spreadsheet, to the "multiple tables" of a relational database. We will also discuss ideas behind publishing or sharing data, moving from HTML documents and Web 1.0 to data services and APIs in Web 2.0, to semantics in Web 3.0. These efforts will be project-driven, with students using and building modern data services with a scripting language. Their projects will underscore the reality that data are plentiful and circulate and interact in a kind of informational ecosystem. As researchers, our students will be called on both to access and to publish data products.

#readings
Readings must be completed before the beginning of class for each session. They are likely to change as our collective interests become clearer. The readings comprise, on the one hand, promient examples of data journalism, and, on the other, more reflective methodological reflections, often in more academic idioms.

#grading
- 35% attendance and participation (incl. reading discussions)
- 35% final project
- 30% homework assignments (5% each)


#sessions

###session 01: tuesday, may 27th 2014

- setting up an ec2 server

- how to use ipython

###session 02: thursday, may 29th 2014

- lists and list operations. [Notes here](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/01%20Lists.ipynb).

Reading: 
- Financial Times EU funding
- http://datajournalismhandbook.org/1.0/en/case_studies_1.html
- http://www.thebureauinvestigates.com/2012/05/29/eu-structural-funds-get-the-data/
- http://eufunds.ftdata.co.uk/

- Halevy, A., P. Norvig, and F. Pereira. “The Unreasonable Effectiveness of Data.” Intelligent Systems, IEEE 24, no. 2 (April 2009): 8–12. doi:10.1109/MIS.2009.36.

- Lazer, David M., Ryan Kennedy, Gary King, and Alessandro Vespignani. “The Parable of Google Flu: Traps in Big Data Analysis.” Science 343, no. 6176 (2014): 1203–5. doi:10.1126/science.1248506.

homework assignment due 6-3: [Lists and list operations](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/Data%20and%20Databases%20Homework%20Assignment%201.ipynb).


###session 03: tuesday, june 3rd 2014

- dictionaries, getting results from JSON APIs. [Notes here](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/02%20Dictionaries%20and%20Web%20APIs.ipynb).

reading: 
- Wickham, Hadley, Deborah Swayne, and David Poole. “Bay Area Blues: The Effect of the Housing Crisis.” *Beautiful Data: The Stories Behind Elegant Data Solutions,* 2009, 303–22.
    - as you read this: what are all of the different sources of structured data that they draw upon? What formats?

- Felten, Edward W. “Declaration of Professor Edward W. Felten in ACLU et Al. v. James R. Clapper Et. Al.,” August 26, 2013.

- http://datajournalismhandbook.org/1.0/en/case_studies_12.html


###session 04: thursday, june 5th 2014

- strings and string operations; regular expressions. [Notes here](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/03%20Strings%20and%20regular%20expressions.ipynb).

reading:
+ Bus Subsidies in Argentina, La Nacion: http://datajournalismhandbook.org/1.0/en/case_studies_14.html

+ http://blogs.lanacion.com.ar/projects/data/vozdata/

+ Berg, Mark, and Geoffrey C. Bowker. “The Multiple Bodies of the Medical Record,” 1996. https://www.ics.uci.edu/~gbowker/records.html.


homework assignment due 6-10: [Dictionaries, web APIs, strings, regular expressions](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/Data%20and%20Databases%20Homework%20Assignment%202.ipynb).


###session 05: tuesday, june 10th 2014

Making structure: number munging
- basic linear algebra
- tables, arrays 
- Pandas & NumPy

readings: 
- Edwards, Paul. *A Vast Machine: Computer Models, Climate Data, and the Politics of Global Warming.* Cambridge: MIT Press, 2010, ch. 10: “Making Data Global”


###session 06: thursday, june 12th 2014
Making structure: text mining

- text munging: textblob, nltk
		- tokenizing, stemming
 	- tdm
	- bag of words and its alternatives
 	- algorithms (clustering, LSA)
 	- sentiment analysis

reading: 
- Ramsay, Stephen. *Reading Machines toward an Algorithmic Criticism.* Urbana : University of Illinois Press, 2011, ch. 3

- “Sapping Attention: Stopwords to the Wise.” Accessed May 25, 2014. http://sappingattention.blogspot.com/2011/04/stopwords-to-wise.html.

homework assignment: *TBD*

###session 07: monday, june 16th 2014

Documenting data journalism

Readings:
"Presenting data to the public," http://datajournalismhandbook.org/1.0/en/delivering_data_0.html

- see http://www.theguardian.com/news/datablog/2011/dec/09/data-journalism-reading-riots
    and the connected series

- http://www.theguardian.com/uk/series/reading-the-riots    
    and the data journalist's academic reflections

- Vis, Farida. “A Critical Reflection on Big Data: Considering APIs, Researchers and Tools as Data Makers.” *First Monday* 18, no. 10 (2013). http://firstmonday.org/ojs/index.php/fm/article/view/4878.

Friedman, Batya, and Helen Nissenbaum. “Bias in Computer Systems.” ACM Transactions on Information Systems (TOIS) 14, no. 3 (1996): 330–47.

###session 08: tuesday, june 17th 2014

(overflow/catch-up day for previous sessions)

###session 09: tuesday june 24th 2014

HTTP, HTML (Beautiful Soup), XML. [Notes here](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/09%20XML%2C%20HTML%2C%20Beautiful%20Soup.ipynb).

- [Notes as delivered](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/Notes%202014-06-23.ipynb) (revised June 26th).

reading:
- Liu, Alan. “Transcendental Data: Toward a Cultural History and Aesthetics of the New Encoded Discourse.” Critical Inquiry 31, no. 1 (September 2004): 49–84. doi:10.1086/427302.


###session 10: thursday june 26th 2014

- more Beautiful Soup, reviewing Python basics.
- [Notes as delivered](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/Notes%202014-06-23.ipynb) (revised June 26th).
- [Scraping menupages example in full](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/scraping%20menupages.ipynb)

reading:
- Fortune, Stephen. “A Brief History of Databases.” Accessed May 3, 2014. http://vvvnt.com/media/history-of-databases.

Homework assignment, due July 1st: [Scraping with Beautiful Soup](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/Data%20and%20Databases%20Homework%20Assignment%205.ipynb).


###session 11: tuesday july 1st 2014

mongodb, an introduction. [Notes here](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/databases/10%20MongoDB.ipynb).


###session 12: thursday july 3rd 2014

introduction to web APIs w/tornado

reading:
- Bucher, Taina. "[Objects of intense feeling: The case of the Twitter API.](http://computationalculture.net/article/objects-of-intense-feeling-the-case-of-the-twitter-api)"
- Thorp, Jer. "[Art and the API.](http://blog.blprnt.com/blog/blprnt/art-and-the-api)"

assignment: make a simple web API.


###session 13: tuesday july 8th 2014

slush/overflow/lab/selected topics day


###session 14: thursday july 10th 2014

final project presentations


###additional resources
##python
learn python the hard way: http://learnpythonthehardway.org/book/

how to think like a computer scientist (python edition): http://openbookproject.net/thinkcs/python/english2e/

##data wrangling

https://dataiap.github.io/dataiap/

https://github.com/mitdbg/asciiclass

##data journalism examples and awardees

http://datajournalismhandbook.org/1.0/en/index.html

http://www.globaleditorsnetwork.org/programmes/data-journalism-awards/

##additional readings cut from syllabus

David Easley and Jon Kleinberg., *Networks, Crowds, and Markets: Reasoning about a Highly Connected World.*, http://www.cs.cornell.edu/home/kleinber/networks-book/, ch. 2

“Connected China”, http://connectedchina.reuters.com/

http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0025995

TED talk: https://www.ted.com/talks/james_b_glattfelder_who_controls_the_world


# Data and Databases, Summer 2015

Columbia University, Lede Program

Mondays and Wednesdays, July 15th through August 31st, 10am

Instructors: [Allison Parrish](http://www.decontextualize.com/) and [Matthew
Jones](http://www.columbia.edu/~mj340/)

##Description

Consideration of both the scientific and social implications of counting, of
turning the world into bits. Through the process of gaining fluency in the use
of Python, students will spend some time thinking through representations of
core "data types" like time, location, text, image, sound and relationships (or
networks), and the computational "affordances" associated with each. Students
will study several common metaphors for organizing and storing data – from
structureless key-value stores, to document collections like MongoDB, to a
single table or spreadsheet, to the "multiple tables" of a relational database.
We will also discuss ideas behind publishing or sharing data, moving from HTML
documents and Web 1.0 to data services and APIs in Web 2.0, to semantics in Web
3.0. These efforts will be project-driven, with students using and building
modern data services with a scripting language. Their projects will underscore
the reality that data are plentiful and circulate and interact in a kind of
informational ecosystem. As researchers, our students will be called on both to
access and to publish data products.

The notes for last year's version of this class are
[here](https://github.com/ledeprogram/courses/tree/master/databases).


##Readings

Readings must be completed before the beginning of class for each session. They
are likely to change as our collective interests become clearer. The readings
comprise, on the one hand, promient examples of data journalism, and, on the
other, more reflective methodological reflections, often in more academic
idioms.


##Homework assignments

There will be six homework assignments in the class, each assigned on a
Wednesday and due on the following Monday. The homework assignments are
designed to test and expand your knowledge of the technical concepts introduced
in class. Each homework assignment will be worth 5% of your grade.


##Final project

The final project is free-form and student-directed, but it should demonstrate
substantial mastery of both the technical and conceptual content of the course.
(If you have a question about whether or not a project idea is appropriate,
please let us know.) The project has the following requirements:

* You must turn in *documentation* of your project, preferably in the form of
  an online blog post (or similar).  In this documentation, you should
  describe your project and its goals, show your methodology, and report
  your findings (if any). Answer the following questions: What data did you
  use? Where did it come from? How did you process the data and what insights
  were thereby produced?
* You must present your project in-class on August 31st. This presentation
  (which will last somewhere from 5 to 10 minutes) should summarize the same
  points as your documentation. Be prepared to answer questions!
* You must turn in the *source code* for your project.

The goal of the final project is for students to be on the hook to pursue their
own interests and find their own way to synthesize the course material.
Students should make something that "fits in" to their (current or
aspirational) professional practice.

Students are free to work on their final projects collaboratively. In
collaborative projects, take care to ensure that *every* student's mastery of
the course content is properly demonstrated.


##Grading

- 35% Attendance and participation (incl. reading discussions)
- 35% Final Project
- 30% Homework assignments (5% each)


##Schedule

###Week 1: Wednesday, July 15th

* Course introduction
* Python: Beyond the Basics. [Notes](01_Python_Beyond_the_Basics.ipynb).

Homework

* [Assignment #1](Homework_1.ipynb), due July 20th


###Week 2: July 20th and 22nd

* Reading discussion
* Unicode. [Notes](02_Unicode.ipynb).
* Regular expressions. [Notes](03_Strings_and_Regular_Expressions.ipynb).

Reading (for discussion July 20th)

* Halevy, A., P. Norvig, and F. Pereira. “The Unreasonable Effectiveness of Data.” Intelligent Systems, IEEE 24, no. 2 (April 2009): 8–12. doi:10.1109/MIS.2009.36. [PDF](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/35179.pdf)
* Lazer, David M., Ryan Kennedy, Gary King, and Alessandro Vespignani. “The Parable of Google Flu: Traps in Big Data Analysis.” Science 343, no. 6176 (2014): 1203–5. doi:10.1126/science.1248506. [PDF](http://gking.harvard.edu/files/gking/files/0314policyforumff.pdf)
* [Literature is not Data: Against Digital Humanities](https://lareviewofbooks.org/essay/literature-is-not-data-against-digital-humanities) by Stephen Marche

Homework

* [Assignment #2](Homework_2.ipynb), due July 27th


###Week 3: July 27th and 29th

* Reading discussion
* Scraping HTML with Beautiful Soup. [Notes](04_Markup.ipynb)
* Introduction to SQL: [Notes](SQL_notes.md)
* Making SQL queries in Python: [Notes](05_SQL_in_Python.ipynb)

Reading (for discussion July 27th)

* Fortune, Stephen. [A Brief History of Databases](http://vvvnt.com/media/history-of-databases).
* Friedman, Batya, and Helen Nissenbaum. “Bias in Computer Systems.” ACM Transactions on Information Systems (TOIS) 14, no. 3 (1996): 330–47. [PDF](http://static.decontextualize.com/pdf/biasincomputers.pdf).
+ [Bus Subsidies in Argentina, La Nacion](http://datajournalismhandbook.org/1.0/en/case_studies_14.html) 
+ [VozData: collaborating to free data from PDFs](http://blogs.lanacion.com.ar/projects/data/vozdata/)

Homework

* [Assignment #3](Homework_3.ipynb), due August 3rd


###Week 4: August 3rd and 5th

* Making structure: number munging
    * pandas (and a bit of numpy)
    * csv, excel importing
    * tables, basic matrix and vector operations
    * basic statistical summarization
    * boolean indexing
    * map, apply, groupby
    * simple graphing

Readings

* Wickham, Hadley, Deborah Swayne, and David Poole. “Bay Area Blues:
The Effect of the Housing Crisis.” *Beautiful Data: The Stories Behind
Elegant Data Solutions,* 2009, 303–22.  (As you read this: what are all of the different sources of
structured data that they draw upon? What formats?)

* Edwards, Paul. *A Vast Machine: Computer Models, Climate Data, and
the Politics of Global Warming.* Cambridge: MIT Press, 2010, ch. 10:
“Making Data Global”

Homework 

* [Assignment #4](Homework_4.ipyng), due August 10th

###Week 5: August 10th and 12th

* Making structure: text mining
    * text munging:
        - vectorizing tokenizing, stemming
        - tdm
    * bag of words and its alternatives
        - algorithms (clustering, topic modeling)
        - sentiment analysis
* extracting text: pdf and ocr

Reading (discuss August 10th)

* Ramsay, Stephen. *Reading Machines toward an Algorithmic Criticism.*
Urbana : University of Illinois Press, 2011, ch. 3
* “Sapping Attention: Stopwords to the Wise.” Accessed May 25, 2014.
http://sappingattention.blogspot.com/2011/04/stopwords-to-wise.html.

Reading (discuss August 12th)

* see http://www.theguardian.com/news/datablog/2011/dec/09/data-journalism-reading-riots and the connected series
* http://www.theguardian.com/uk/series/reading-the-riots and the data journalist's academic reflections
* Vis, Farida. “A Critical Reflection on Big Data: Considering APIs,
Researchers and Tools as Data Makers.” *First Monday* 18, no. 10 (2013).
http://firstmonday.org/ojs/index.php/fm/article/view/4878.

Homework

* Assignment #5 (TBD), due August 17th

##Week 6: August 17th and 19th

* Final project proposals
* Working with networks (and back to maps if time permits)
    * introductory social network analysis
    * networkx, gephi

Reading

* Look at: “Connected China”, http://connectedchina.reuters.com/
* S. Graham, I. Milligan, & S. Weingart, [The Historian's
Macroscope](http://www.themacroscope.org/),  Section on Networks.

Homework

* Assignment #6 (TBD), due August 24th


##Week 7: August 24th and 26th

* Building web APIs with Flask (and/or other selected topics)
* Final project workshops

Reading

- Bucher, Taina. "[Objects of intense feeling: The case of the Twitter API.](http://computationalculture.net/article/objects-of-intense-feeling-the-case-of-the-twitter-api)"
- Thorp, Jer. "[Art and the API.](http://blog.blprnt.com/blog/blprnt/art-and-the-api)"

##Week 8: August 31st

* Final project presentations


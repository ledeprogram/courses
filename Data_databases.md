---
title: Data and Databases
date: 5/28/14 - 7/14/14
time: T & Th
affiliation: Columbia University, Lede Program
instructors: Adam Parrish, Matthew Jones
contact: TBA
location: TBA
---

#Data and Databases

**SUPER DRAFTY--overly detailed in early weeks and overly schematic in late weeks**

**tried to put python intros within motivation**

**motivations and exemplars needed!**


##Data structures and their enemies
### 1. Illusions of data accessibility

The motivation:

- Good, bad, and intermediate forms of "open data"

- Ethical imperative
	- making data available to both humans and machines
	- brutual honesty about making of data

- examples
> "Do No Harm: Hospital Care in Las Vegas," http://www.lasvegassun.com/hospital-care/
>	http://www.lasvegassun.com/news/2010/jun/27/fascination-and-frustration-reporting-las-vegas-ho/

The theory:

- Structured vs. unstructured data

- varieds example: MTA data? some pdf data; crappy http tables

The practice:

- *Python*
	- data types: lists
		- practice traversing
		- counting from zero
		- list comprehensions [big ask for first day]
			- MTA data?
	- importing csv [PANDAs?]
	- importing rss [?]
	-  control structures
		- for..in; while?

### 2. Structured data

- NYT json data? wordnik?
	- getting API keys, etc.

- Metadata and data
	- geolocation data in photo examples
	- mp3 example

- *Python*
	- data types: dicts
		- practice traversing
		- key, value

- JSON as simple structured data
	- *python*

- Using APIs
	*python* URL tools

END OF WEEK ONE:
	some systematic api program to draw from source, put in good dict, calculation something meaningful


**assume familiary with unix file system by week two?**


### 3. Structured data: strings and regular expressions

- *python* strings and string methods

- regular expressions/grep/*python*


### 4. Proprietary, open, and inbetween

- poltics of drm, etc.? (Gillespie)
- proprietary data stores of public records

- *Python*
	- conditionals and binary operators
		- explicit (if) & as indices
		- filtering lists
	- exception handling
	- html(BeautifulSoup)

- XML, the horror, the beauty
	- standard XML parsing libraries



??? NOT SURE IF A SEPARATE DAY/WHAT TECH CONTENT?


##'Raw data' is an oxymoron

###  Making structure: number munging

- Paul Edwards on climate data

- critical reflection on "data and method"
	- metadata about sources and processing
	- data provenance
	- classic statistical questions
	- sensors and personal equations

- numerical data munging
	- shaping of data
	- missing values, etc.
	- interpolation

- Tables, vectors, and arrays
	- basic linear algebra and vector operations
	- *python* pandas/NumPy basics

*END OF WEEK TWO: able to move to and from different formats*


###  Making structure: text mining
- example: wikileaks telegraphs, enron emails, declassified state dept telegrams, twitter

- *python* strings and string methods

- text mining basics
	- tdm
	- bag of words and its alternatives
	- text munging [https://de.dariah.eu/tatom/preprocessing.html]
		- tokenizing, stemming
 	- simple algos
 	    - clustering, &c


###  Making structure: binary blobs

- motivation: scanned document dumps?

- Binary formats (lossy/lossless)
	- pdf
	- images
	- video

- Binary munging
	- pdftotext
	- OCR
	- image classification?

***end of week three: ???****



###  Documenting data journalism

>see http://www.theguardian.com/news/datablog/2011/dec/09/data-journalism-reading-riots
##Critical publicity of data journalism

>and the connected series

>http://www.theguardian.com/uk/series/reading-the-riots

>and the data journalist's academic reflections

>Vis, Farida. “A Critical Reflection on Big Data: Considering APIs, Researchers and Tools as Data Makers.” First Monday 18, no. 10 (2013). http://firstmonday.org/ojs/index.php/fm/article/view/4878.

- writing self-reflexive posts of methods and limits of data

- critical exercise on a number of examples good and bad of documentation






##Database Metaphors and Systems


### . Databases: Relational
- relational metaphor

Fortune, Stephen. “A Brief History of Databases.” Accessed May 3, 2014. http://vvvnt.com/media/history-of-databases.

- ACID and its (un)importance
- basic SQL
	- *python* interface
	- sqlite3 shell [/}]


### . Databases: NoSQL and document stores

- JSON
- Key-value
- Document stores (SOLR)
- MongoDB
	- *python* interface
- distribution and its significance
	- practical APT theorem: can't have everything


## Building Opening: HTTP/Networking Basics


### Building openness: API

- Clinton FOIA materials? NSA materials
- archives as political legitimation
- building counter-archives (national security archive)

- Creating Flask? page with API
	- drawing upon (earlier) SQL and mongo databases
- documenting methods/data
- CRITICAL reflection of many posts of exemplary projects


### 13. Algorithmic documentation?

- automatic archives (Stanford)
- automatic writing (ProPublica)




##The Critique of Pure Data
### . Ideologies of data

Halevy, A., P. Norvig, and F. Pereira. “The Unreasonable Effectiveness of Data.” Intelligent Systems, IEEE 24, no. 2 (April 2009): 8–12. doi:10.1109/MIS.2009.36.

danah boyd and Kate Crawford “Six Provocations for Big Data.”
https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID1926431_code1210838.pdf?abstractid=1926431&mirid=2.

- Google flu trends

Lazer, David M., Ryan Kennedy, Gary King, and Alessandro Vespignani. “The Parable of Google Flu: Traps in Big Data Analysis.” Science 343, no. 6176 (2014): 1203–5. doi:10.1126/science.1248506.


##on-line classes and tutorials worth considering
Eugene Wu:
https://dataiap.github.io/dataiap/
https://github.com/mitdbg/asciiclass

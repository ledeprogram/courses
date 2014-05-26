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
	
##Data structures and their enemies
### 1. Illusions of data accessibility

The motivation:

- Good, bad, and intermediate forms of "open data"

- Ethical imperative
	- making data available to both humans and machines
	- brutual honesty about making of data

- examples

+ Bus Subsidies in Argentina, La Nacion: http://datajournalismhandbook.org/1.0/en/case_studies_14.html

+ Citibike data: http://www.citibikenyc.com/system-data

+ "Do No Harm: Hospital Care in Las Vegas," http://www.lasvegassun.com/hospital-care/
	+ http://www.lasvegassun.com/news/2010/jun/27/fascination-and-frustration-reporting-las-vegas-ho/

The theory:

- Structured vs. unstructured data

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

- Wickham, Hadley, Deborah Swayne, and David Poole. “Bay Area Blues: The Effect of the Housing Crisis.” Beautiful Data: The Stories Behind Elegant Data Solutions, 2009, 303–22.
	- what are all of the different sources of structured data that they draw upon? What formats?

- NYT json/xml data
	- getting API keys
	- http://developer.nytimes.com/docs/congress_api	

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
	some systematic api program to draw from source, put in good dict, calculate something meaningful


**assume familiary with unix file system by week two?**


### 3. Structured data: strings and regular expressions


- example with structured diagnostic code or the like?

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


##'Raw data' is an oxymoron: making structure

###Making structure: number munging [mlj]

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


###  Making structure: text mining [mlj]
- example: wikileaks telegraphs, enron emails, declassified state dept telegrams, twitter

- text mining basics [textblob]
	
	- text munging: textblob
		- tokenizing, stemming
 	- tdm
	- bag of words and its alternatives
 	- simple algos
 	    - classification (naive bayes)
 	    - sentiment analysis


###  Making structure: binary blobs

- motivation: scanned document dumps

- Financial Times EU funding: 'openness through pdf'

http://datajournalismhandbook.org/1.0/en/case_studies_1.html
http://www.thebureauinvestigates.com/2012/05/29/eu-structural-funds-get-the-data/
http://eufunds.ftdata.co.uk/

- Dykes, Jason, and Jo Wood. “The Geographic Beauty of a Photographic Archive.” In The Map Reader, 288–96. John Wiley & Sons, Ltd, 2011. http://dx.doi.org/10.1002/9780470979587.ch38.
- http://www.geograph.org.uk/


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

- writing self-reflexive posts of methods and limits of data

- documenting process of data

- critical exercise on a number of examples good and bad of documentation


####readings
"Presenting data to the public," http://datajournalismhandbook.org/1.0/en/delivering_data_0.html

>see http://www.theguardian.com/news/datablog/2011/dec/09/data-journalism-reading-riots

>and the connected series

>http://www.theguardian.com/uk/series/reading-the-riots

>and the data journalist's academic reflections

>Vis, Farida. “A Critical Reflection on Big Data: Considering APIs, Researchers and Tools as Data Makers.” First Monday 18, no. 10 (2013). http://firstmonday.org/ojs/index.php/fm/article/view/4878.

####statistical scolding
- correlation vs. causation
- overfitting

##Database Metaphors and Systems

### . Databases: Relational
- relational metaphor

Fortune, Stephen. “A Brief History of Databases.” Accessed May 3, 2014. http://vvvnt.com/media/history-of-databases.

- ACID and its (un)importance
- basic SQL
	- *python* interface
	- sqlite3 shell [/}]

->using SQL for queries: example: FT EU database. [put on central sql server and let query]


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



##The Critique of Pure Data
###Ideologies of data

Halevy, A., P. Norvig, and F. Pereira. “The Unreasonable Effectiveness of Data.” Intelligent Systems, IEEE 24, no. 2 (April 2009): 8–12. doi:10.1109/MIS.2009.36.

danah boyd and Kate Crawford “Six Provocations for Big Data.”
https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID1926431_code1210838.pdf?abstractid=1926431&mirid=2.

- Google flu trends

Lazer, David M., Ryan Kennedy, Gary King, and Alessandro Vespignani. “The Parable of Google Flu: Traps in Big Data Analysis.” Science 343, no. 6176 (2014): 1203–5. doi:10.1126/science.1248506.


##Forgetting data, excluding data
- “Minimization Procedures Used by the National Security Agency in Connection with Acquisitions of Foreign Intelligence Information Pursuant to Section 702 of the Foreign Intelligence Surveillance Act of 1978, as Amended,” July 28, 2009.






##on-line classes and tutorials worth considering
Eugene Wu:
https://dataiap.github.io/dataiap/
https://github.com/mitdbg/asciiclass

### Data sets

- NBA Census: https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/NBA-Census-10.14.2013.csv
- Iris data: https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/iris.csv
- Authorship data: https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/book-data.csv
- Mystery books: [1](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery1.txt) [2](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery2.txt) [3](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery3.txt) [4](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery4.txt) [5](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery5.txt) 

---
title: Algorithms
date: 7/14/14-9/3/14
time: M & W 10am - 1pm 
affiliation: Columbia University, Lede Program
instructors: Jonathan Soma, Chris Wiggins
location: 607c Pulitzer Hall*

---

\* [room schedule](https://drive.google.com/file/d/0B4OAOue0b3VMNXJ1Z1loaGg4bWc/edit?usp=sharing).  

> [Multiliteracies in algorithms](http://compositionforum.com/issue/14.2/rev-selber.php): functional literacy, critical literacy, and rhetorical literacy.
Within critical literacy, a strong emphasis will be knowing what is possible. For algorithms, this
usually means *computational complexity* -- the study of how the time needed to perform an algorithm
grows as the problem size (e.g., the number of data) grows. For algorithms dealing with data, we will study how
this leads to a balance between *fast* and *accurate*. Within functional literacy, we will be building on
Python's tools for learning from data, including [scikit-learn](http://scikit-learn.org/stable/). Rhetorical literacy will be the anchor
for the class, as our primary interest is in producing technology-enabled journalism.

---

## Week 1: Intro to Algorithms

- What is an algorithm?
    + Algorithms in computer science (searching, sorting, clustering)
    + Algorithms in real life
- Algorithmic thinking
    + Step after step
    + Reductions/Black boxes
- Multiliteracies
    + Functional literacy
    + Rhetorical literacy
    + Critical literacy
- Summary of projects
    + Documentation
    + Agile vs Waterfall
- Analysis of algorithm
    + Computationally (Functionally)
        - Correctness, Termination, Time, Space
        - Generality
    + Critically (Nick Diakopoulos)
        - Prioritization
        - Classification
        - Association
        - Filtering
- Examples of algorithms in journalism
    + QuakeBot
    + Narrative Science/Automated Insights
    + Projects from last class

#### Day One Links

- [ISO 3103](http://en.wikipedia.org/wiki/ISO_3103) ([2](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=8250))
- [Royal Society of Chemistry](http://www.rsc.org/pdf/pressoffice/2003/tea.pdf)
- [Orwell](http://www.booksatoz.com/witsend/tea/orwell.htm)
- [Automated Insights](http://nymag.com/daily/intelligencer/2014/07/why-robot-journalism-is-great-for-journalists.html) ([2](http://qz.com/228218/the-aps-newest-business-reporter-is-an-algorithm/))
- [Algorithmic Accountability Reporting](http://towcenter.org/wp-content/uploads/2014/02/78524_Tow-Center-Report-WEB-1.pdf) by Nick Diakopoulos

### Wednesday 7/16 

- Introduction to first in-class project: building a democrat detector

Course tools: [scikit-learn](http://scikit-learn.org/stable/), [pandas](http://pandas.pydata.org/), [ntlk](http://www.nltk.org/), [capitolwords.org's api](http://capitolwords.org/api/1/) (you will need to [register for a key](http://sunlightfoundation.com/api/accounts/register/))

-**Week Inspiration:** [Diakopolous Report](http://towcenter.org/wp-content/uploads/2014/02/78524_Tow-Center-Report-WEB-1.pdf) 
  
## Week 2: Supervised learning

**Focus**: modeling: predictive and interpretable

- tools:
    - scikit-learn
    - nltk
    - pandas
- data journalism and reproducibility
    - [upshot on github](https://github.com/TheUpshot)
        - e.g., [rangel charity](https://github.com/TheUpshot/RangelCharity)
        - e.g., [world cup](https://github.com/TheUpshot/world-cup-study)
        - reminder: same [bostock](https://github.com/mbostock) as in d3
        - also producing tools, e.g., [statement](https://github.com/TheUpshot/statement/blob/master/README.md) for getting congressional press statements
- why open source? [many eyes](http://en.wikipedia.org/wiki/Linus's_Law#By_Eric_Raymond)
- [overfitting](http://scikit-learn.org/stable/auto_examples/plot_underfitting_overfitting.html)

-**Week Inspiration:** [Nifty project on authorship detection](http://nifty.stanford.edu/2013/craig-authorship-detection/)

### Monday 7/21

#### overview/concepts:

- algorithms that learn from data to model the world
( i.e., machine learning)
- the role of optimization in those algos 
- representation (e.g., documents) 
- examples: reading aloud the [authorship nifty assignment](http://nifty.stanford.edu/2013/craig-authorship-detection/)
- another example: bag of words

#### math:
- introduce naive Bayes 
- introduce probability and Bayes rule 
- go through naive Bayes 
- show how it's a graphical model (pictures, organizing stories in your head, a chance to talk about complexity)

#### extensions:

- say but don't show how you could do this with priors and for multiclass
- talk about other classification algorithms
- how do decide what algorithm or priors are "best"? 
- digression on meaning of modeling and desiderata of models 

#### Fun data to play with

- [govtrack](https://www.govtrack.us/developers)
- [US github](https://github.com/unitedstates/congress/wiki/Bills)

-**Week Inspiration:** [what is Bayes theorem](http://www.scientificamerican.com/article/what-is-bayess-theorem-an/)

### Wednesday 7/23

- k-nearest neighbors (predicting from examples)

## Week 3: Probability and statistics

### Monday: 7/28

- back to 'Naive Bayes' and Bayes rule
- 'being Bayesian'
- critical literacy
    + why this classifier? what else is possible?
    + computational complexity: what is realistic?
    + what assumptions are made?
- rhetorical literacy: try something else!
    + random forests
    + decision trees, e.g., in [ProPublica](http://www.propublica.org/)'s [message machine](http://www.propublica.org/nerds/item/how-propublicas-message-machine-reverse-engineers-political-microtargeting)
    + SVMs
    + explore [scikit-learn](http://scikit-learn.org/stable/)'s [classification algorithms](http://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

**Possibly useful:** [Bayes Rule](http://www.scientificamerican.com/article/what-is-bayess-theorem-an/)

### Wednesday 7/30

- supervised learning/classification with probability modeling

## Week 4: Unsupervised learning

**Focus:** Exploratory data analysis, iterative algorithms (and therefore fast-vs-accurate)

### Monday 8/4 
- [bayes, naively](https://docs.google.com/spreadsheets/d/1Df09QfiAz217b9Z78UqPFan6cuIuK3UdApVPuEaFKhQ/edit#gid=0)
- re-orient: supervised+unsupervised
- k-means & '[GMM](http://scikit-learn.org/stable/modules/mixture.html)'
- [example k-means](http://scikit-learn.org/0.11/_downloads/document_clustering.py)
- project: find the tea party
    - cluster docs using bag of words + kmeans
    - functional literacy: fast-vs-accurate tradeoff
    - critical literacy: why 2 clusters?
    - rhetorical: what did you learn?
    - critical literacy: what about 3 clusters?
    - critical literacy: what distance are you using on words?
    - rhetorical: is there a tea party cluster?
    - rhetorical: try something else in scikit-learn [clustering algorithms](http://scikit-learn.org/stable/modules/clustering.html#clustering)

### Wednesday 8/6 
- generative clustering (clustering as inference)

## Week 5: Nifty projects: 

### Monday 8/11

- [Google one-grams](http://nifty.stanford.edu/2014/hug-google-books-dataset/)

### Wednesday 8/13

- [Twitter sentiment mapping](http://nifty.stanford.edu/2013/denero-muralidharan-trends/)
 
(note: lots of room for critical literacy here)

## Week 6: Algorithmic story generation

### Monday 8/18

### Wednesday 8/20

## Week 7: Networks and graphs

### Monday 8/25

- Networks
      - centralities
        - functional literacy
        - critical literacy: does choice of centrality matter?
        - critical literacy: how do you reduce human interactions into a graph?
      - graph drawing/graph visualization
        - critical literacy: does graph drawing mean anything? what are the axes?

**Possibly useful** [networkx](https://networkx.github.io/)

### Wednesday 8/27

- Graphs


## Week 8: Final project demo

### Monday 9/1

- No class! (Labor day)

### Wednesday 9/3

- Demos

---

## additional resources

### scikit-learn
- [the site](http://scikit-learn.org/stable/)
- [their tutorial on infernece](http://scikit-learn.org/stable/tutorial/statistical_inference/index.html)
- [their tutorial on scikit-learn](http://scikit-learn.org/stable/tutorial/basic/tutorial.html)
- [1-page algorithm *cheat sheet*](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
- [(longer) user guide](http://scikit-learn.org/stable/user_guide.html)
- [many examples](http://scikit-learn.org/0.11/auto_examples/index.html)

### a book
- [a book](http://www.packtpub.com/mastering-machine-learning-with-scikit-learn/book)
- [a code set associated with this book](https://github.com/luispedro/BuildingMachineLearningSystemsWithPython)


### some fun data, none of which has API

- [presidential speeches](http://www.presidentialrhetoric.com/historicspeeches/index.html) 
- [50 'important' speeches](http://www.americanrhetoric.com/21stcenturyspeeches.htm) 
- [all inauguration speeches]( http://www.bartleby.com/124/index.html )

<!--
##python
##data wrangling
##data journalism examples and awardees
##additional readings cut from syllabus
-->

### Readings

- [Reading Machines](http://www.press.uillinois.edu/books/catalog/75tms2pw9780252036415.html), Stephen Ramsay, 2011

### Python

- [warning on upgrades](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)

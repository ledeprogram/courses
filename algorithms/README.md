
- title: algorithms
- date: 7/14/14-9/3/14
- time: M & W 10am - 1pm 
- affiliation: Columbia University, Lede Program
- instructors: Jonathan Soma, Chris Wiggins
- location: 607c Pulitzer Hall \*

---

 
> [Multiliteracies in algorithms](http://compositionforum.com/issue/14.2/rev-selber.php): functional literacy, critical literacy, and rhetorical literacy.
Within critical literacy, a strong emphasis will be knowing what is possible. For algorithms, this
usually means *computational complexity* -- the study of how the time needed to perform an algorithm
grows as the problem size (e.g., the number of data) grows. For algorithms dealing with data, we will study how
this leads to a balance between *fast* and *accurate*. Within functional literacy, we will be building on
Python's tools for learning from data, including [scikit-learn](http://scikit-learn.org/stable/). Rhetorical literacy will be the anchor
for the class, as our primary interest is in producing technology-enabled journalism.

---

>  "every piece of digital technology embeds within it a model of the world, and acts as an argument for that model." --mark hansen


---

new room schedule:

- M Aug 25: 607B (j-school)
- T Aug 26; 607B (j-school)
- W Aug 27: 607B (j-school)
- R Aug 28: 609 Hamilton
 
- M Sept 1: Labor Day
- T Sept 2: 607B (j-school)  *this class runs 1-6pm, to showcase your final projects*
- W Sept 3: 607B (j-school)

---

# Schedule and notes:


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

**Focus**: modeling: [predictive and interpretable](http://www.stat.uchicago.edu/~lekheng/courses/191f09/breiman.pdf)

- tools:
    - [scikit-learn](http://scikit-learn.org/stable/)
    - [nltk](http://www.nltk.org/)
    - [pandas](http://pandas.pydata.org/)
- data journalism and reproducibility
    - [upshot on github](https://github.com/TheUpshot)
        - e.g., [rangel charity](https://github.com/TheUpshot/RangelCharity)
        - e.g., [world cup](https://github.com/TheUpshot/world-cup-study)
        - reminder: same [bostock](https://github.com/mbostock) as in d3
        - also producing tools, e.g., [statement](https://github.com/TheUpshot/statement/blob/master/README.md) for getting congressional press statements
- why open source? 
    + [many eyes](http://en.wikipedia.org/wiki/Linus's_Law#By_Eric_Raymond)
    + BUT this doesn't mean no bugs. cf., [heartbleed](http://mashable.com/2014/04/14/heartbleed-open-source/)
- [overfitting](http://scikit-learn.org/stable/auto_examples/plot_underfitting_overfitting.html) (cf., Einstein's ["Everything should be made as simple as possible, but not simpler."](  http://quoteinvestigator.com/2011/05/13/einstein-simple/#more-2363)
- discussion of [nifty](http://nifty.stanford.edu) projects
    - [sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis): it's a thing
    - [example](http://www.crimsonhexagon.com/) of a sentiment analysis as a service company
    - [hedometer](http://www.hedonometer.org/index.html): example of a sentiment analysis research project
- more on naive bayes
    - [example](https://github.com/jhofman/ddm/blob/master/2012/lecture_03/enron_naive_bayes.sh) of naive bayes in [bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell)) script on [enron](http://en.wikipedia.org/wiki/Enron) email [dataset](http://nlp.cs.aueb.gr/software_and_datasets/Enron-Spam/index.html)
    - [example](http://awk.info/?doc/tools/nbc.html) of naive bayes in [awk](http://en.wikipedia.org/wiki/AWK)
    - this is not how spam works, though [some people think it is](http://www.paulgraham.com/spam.html)
- importance of probability
    - [prosecutor's fallacy](http://en.wikipedia.org/wiki/Prosecutor's_fallacy)
    - [bayes in oj simpson trial](http://opinionator.blogs.nytimes.com/2010/04/25/chances-are/)
    - [box on iterative understanding](http://www.tandfonline.com/doi/pdf/10.1080/01621459.1976.10480949)

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
    + what is "good" modeling -- see [Leo](http://www.stat.uchicago.edu/~lekheng/courses/191f09/breiman.pdf) (an allusion to CP Snow's [the two cultures]( http://en.wikipedia.org/wiki/The_Two_Cultures)
- rhetorical literacy: try something else!
    + random forests
    + decision trees, 
        - e.g., in [ProPublica](http://www.propublica.org/)'s [message machine](http://www.propublica.org/nerds/item/how-propublicas-message-machine-reverse-engineers-political-microtargeting)
        - [iris image](http://www.ibm.com/developerworks/library/ba-predictive-analytics2/fig06.gif) as simple decision tree
    + SVMs
    + explore [scikit-learn](http://scikit-learn.org/stable/)'s [classification algorithms](http://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- introduction to unsupervised learning
    + normalization via [standard score](http://en.wikipedia.org/wiki/Standard_score)
    + preprocessing at [command line](http://shop.oreilly.com/product/0636920032823.do)
- more on data journalism
    + [NYT LIRR example](http://www.nytimes.com/2012/09/13/nyregion/more-lirr-retirees-arrested-on-fraud-charges.html), 2012
    + [Lucia de berk](http://www.badscience.net/2010/04/lucia-de-berk-a-martyr-to-stupidity/)
    + [forensic bioinformatics](http://www.nytimes.com/2011/07/08/health/research/08genes.html)
- supervised learning
    + [kmeans](https://www.youtube.com/watch?v=gSt4_kcZPxE) movie
- useful resources to learn more
    + [free book](http://web.stanford.edu/~hastie/local.ftp/Springer/OLD/ESLII_print4.pdf) "triplets" aka ESL
    + [map](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) of algorithms, including k-means, GMM; kNN, NB, decision trees


**Possibly useful:** [Bayes Rule](http://www.scientificamerican.com/article/what-is-bayess-theorem-an/)

### Wednesday 7/30

- supervised learning/classification with probability modeling

## Week 4: Unsupervised learning

**Focus:** Exploratory data analysis, iterative algorithms (and therefore fast-vs-accurate)

### Monday 8/4 

opening questions:

+ how can journalists be disciplined while facing deadlines?
    - hard with deadlines; cf., "[The Goat Must Be Fed](http://www.goatmustbefed.com/): Why digital tools are missing in most newsrooms", by the Duke Reporters' Lab, May 2014 
    - hard even for professional developers; cf., [commit logs from last night](http://commitlogsfromlastnight.com/ )
    - growing awareness is already leading to novel field, and novel curricula. cf., the [software carpentry]( http://software-carpentry.org/ ) movement.
    - note that you ignore good software carpentry at your peril. cf., ["
  How to lose $172,222 a second for 45 minutes"]( http://pythonsweetness.tumblr.com/post/64740079543/how-to-lose-172-222-a-second-for-45-minutes )
+ should the relationship between journalist and story end when story is published?  (cf., "[The leaked New York Times innovation report](http://www.niemanlab.org/2014/05/the-leaked-new-york-times-innovation-report-is-one-of-the-key-documents-of-this-media-age/) is one of the key documents of this media age", Joshua Benton, Neiman Journalism Lab )
    - see also this [summary/table of contents](https://gist.github.com/chrishwiggins/3e47cbcd46a697694ba9)
    - [example](https://twitter.com/NickKristof) of journalist engaging audience
    - [example](
http://www.nytimes.com/interactive/2014/health/paying-till-it-hurts.html
) of journalist turning relations
with readers into new stories


new matters:

- [bayes, naively](https://docs.google.com/spreadsheets/d/1Df09QfiAz217b9Z78UqPFan6cuIuK3UdApVPuEaFKhQ/edit#gid=0)
- (supervised) regression and (over-)fitting
    + [explanation](http://scikit-learn.org/stable/auto_examples/plot_underfitting_overfitting.html)
    + [code](http://scikit-learn.org/stable/_downloads/plot_underfitting_overfitting.py)

- document clustering in kmeans
    + [code]( http://scikit-learn.org/0.11/_downloads/document_clustering.py)
    + note: uses [TFIDF](http://en.wikipedia.org/wiki/Tf%E2%80%93idf)
    + related example in kmeans: [digits](
http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#example-cluster-plot-kmeans-digits-py
)

- 'GMM' (Gaussian/Normal/Bell curve mixture modeling)
    + [explanation](http://scikit-learn.org/stable/modules/mixture.html)
    + [image](http://cl.ly/image/22172E3d3o3o)
of 
[pseudocode](
http://en.wikipedia.org/wiki/Pseudocode)
from 
[ESL](
http://web.stanford.edu/~hastie/local.ftp/Springer/OLD/ESLII_print4.pdf)
    + demo 
        - [explanation](http://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html#example-mixture-plot-gmm-pdf-py)
        - [code](http://scikit-learn.org/stable/_downloads/plot_gmm_pdf.py)
    + [actual code for GMM](https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/mixture/gmm.py)
- dimensionality reduction via
[PCA](http://web.media.mit.edu/~tristan/phd/dissertation/figures/PCA.jpg)
- try something else in scikit-learn from among their [clustering algorithms](http://scikit-learn.org/stable/modules/clustering.html#clustering)! Try changing number of clusters! Go play!

thoughts on UNIX and algorithms in your life:

- [too many aliases]( http://mathbabe.org/2013/04/15/interview-with-chris-wiggins-dont-send-me-another-shortcut-alias/), mathbabe post
- example: code to introduce people to each other
    + [original code](  https://github.com/chrishwiggins/orly/blob/master/ii
)
    + [pull request](  https://github.com/chrishwiggins/orly/commit/954025d9e31a4625023cc77c16f25a592e229bff
)
    + [improvied code](  https://github.com/chrishwiggins/orly/blob/master/iii
)
- [example](https://gist.githubusercontent.com/chrishwiggins/3d76528e99434a4ddd4e/raw/f9a7c377e14c1a620ec34db04f6507ed61f44744/a.rb) 
of pipes for word counting
- [killall](http://en.wikipedia.org/wiki/Killall) is useful
- some example [aliases](
http://en.wikipedia.org/wiki/Alias_(command))
    + [gugc](
https://github.com/chrishwiggins/mise/blob/1a5a3e557bd38fbb11c7771ffe3725104c4815d8/sh/aliases-public.sh#L63)
 for better git discipline
    + [repo](
https://github.com/chrishwiggins/mise/blob/1a5a3e557bd38fbb11c7771ffe3725104c4815d8/sh/aliases-public.sh#L89)
 for better repository discipline
    + [mypy](
https://github.com/chrishwiggins/mise/blob/1a5a3e557bd38fbb11c7771ffe3725104c4815d8/sh/aliases-public.sh#L193
) for dealing with multiple python installs

-**Week Inspiration:** [Krugman busts out probability](http://krugman.blogs.nytimes.com/2014/08/02/anti-intellectualism-that-dares-not-speak-its-name/) 

### Wednesday 8/6 

- Python test
- KMeans coding - [in-class version](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/algorithms/05%20Kmeans!%20from%20class.ipynb), [my version](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/algorithms/05%20NBA%20K-Means%20(my%20notes).ipynb)
- [Homework](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/Homework%20-%2005%20KMeans.ipynb)

## Week 5: Nifty projects: 

### Monday 8/11

- [Google one-grams](http://nifty.stanford.edu/2014/hug-google-books-dataset/)
    + [solutions and test scripts](https://github.com/ledeprogram/courses/tree/master/algorithms/nifty-onegram)
    + now go nuts! be free!
- Related: Zipf's law: why?
    - [in word counts](http://norvig.com/mayzner.html) (from [Peter Norvig](http://en.wikipedia.org/wiki/Peter_Norvig))
    - [in neuroscience](http://esciencecommons.blogspot.com/2014/08/physicists-eye-neural-fly-data-find.html) 
    - [in general](http://arxiv.org/pdf/cond-mat/0412004.pdf)

### Wednesday 8/13

- [Twitter sentiment mapping](http://nifty.stanford.edu/2013/denero-muralidharan-trends/)
 
(note: lots of room for critical literacy here)

## Week 6: Algorithmic story generation

### Monday 8/18

- Input, Output, Precision, Determinism, Finiteness, Correctness, Generality
- Prioritization, Classification, Association, Filtering

**Quakebot:** [on Source](https://source.opennews.org/en-US/articles/how-break-news-while-you-sleep/), [on Slate](http://www.slate.com/blogs/future_tense/2014/03/17/quakebot_los_angeles_times_robot_journalist_writes_article_on_la_earthquake.html)

#### Storytelling

What is a story? What's *in* a story?

- Generative vs. descriptive
- [Plotto](http://www.brainpickings.org/index.php/2012/01/06/plotto/), the Master Book of All Plots ([2](http://www.npr.org/2012/02/19/146941343/plotto-an-algebra-book-for-fiction-writing)) - preconditions, postconditions
- [Aarne-Thompson Classification System](http://en.wikipedia.org/wiki/Aarne–Thompson_classification_system)
- **Vladimir Propp**: [Plot Elements](http://changingminds.org/disciplines/storytelling/plots/propp/propp.htm), [Dramatis Personae](http://changingminds.org/disciplines/storytelling/characters/propp_personae.htm)
- **Claude Lévi-Strauss**: [Structuralism](http://www.webpages.uidaho.edu/~sflores/KlagesLevi-Strauss.html), [The Structural Study of Myth](http://www.soc.ucsb.edu/faculty/mohr/classes/soc4/summer_08/pages/Resources/Readings/Levi-Strauss.pdf)
- <a href="http://en.wikipedia.org/wiki/Conflict_(narrative)">Conflict</a>

[Cinderella tales](http://www.pitt.edu/~dash/type0510a.html), examples: [1](http://www.pitt.edu/~dash/type0510a.html#jacobs), [2](http://www.pitt.edu/~dash/type0510a.html#saddleslut), [3](http://www.pitt.edu/~dash/type0510a.html#grimm)

NYT: [Mike Brown's autopsy](http://www.nytimes.com/2014/08/18/us/michael-brown-autopsy-shows-he-was-shot-at-least-6-times.html), [PWC fined](http://dealbook.nytimes.com/2014/08/17/pwc-faces-penalty-and-sidelining-of-regulatory-consulting-unit/), [Germany + the American Old West](http://www.nytimes.com/2014/08/18/world/europe/germanys-fascination-with-american-old-west-native-american-scalps-human-remains.html), [Palin and Oil](http://www.nytimes.com/2014/08/18/us/politics/sarah-palins-attack-on-sean-parnells-oil-plan-creates-odd-wedge-for-alaskan-voters.html), [Iraq retakes dam](http://www.nytimes.com/2014/08/19/world/middleeast/iraq-mosul-dam.html)

#### [Narrative Science](http://www.narrativescience.com) (and [Automated Insights](http://blog.automatedinsights.com/post/71645583008/our-year-in-review))

- [Narrative Science on Forbes](http://www.forbes.com/sites/narrativescience/), examples: [1](http://www.forbes.com/sites/narrativescience/2014/08/12/earnings-expected-to-increase-for-agilent-technologies/), [2](http://www.forbes.com/sites/narrativescience/2014/08/12/perrigo-profit-expected-to-slip/), [3](http://www.forbes.com/sites/narrativescience/2014/08/12/profit-expected-to-dip-for-autodesk-2/), [4](http://www.forbes.com/sites/narrativescience/2014/08/15/earnings-increase-expected-for-tjx-companies/)
- [The Future of Journalism?](http://www.cjr.org/behind_the_news/the_future_of_journalism.php?page=all) (CJR)
- [Can an Algorithm Write a Better News Story Than a Human Reporter?](http://www.wired.com/2012/04/can-an-algorithm-write-a-better-news-story-than-a-human-reporter/)
- [Notes on Narrative Science and Automated Insights](http://blog.ouseful.info/2013/05/22/notes-on-narrative-science-and-automated-insight/)

What's your angle? Trands, correlations, inflection points

#### Propublica's [Opportunity Gap](http://projects.propublica.org/schools/)

Writeup: [How To Edit 52,000 Stories at Once](http://www.propublica.org/nerds/item/how-to-edit-52000-stories-at-once)

- **Stuyvesant High**: [ProPublica](http://projects.propublica.org/schools/schools/362058002877), [Big Apple Ed](http://www.bigappleed.com/schools/107-stuyvesant-high-school), [Open House Packet](http://stuy.enschool.org/pdf/Complete_Open_House_Packet.pdf), [IB Times](http://www.ibtimes.com/stuyvesant-high-asian-american-domination-elite-schools-triggers-resentment-soul-searching-1563568), [NY Post](http://nypost.com/2014/07/19/why-nycs-push-to-change-school-admissions-will-punish-poor-asians/)
- **Brooklyn Tech**: [ProPublica](http://projects.propublica.org/schools/schools/362058001928), [Big Apple Ed](http://www.bigappleed.com/schools/676-brooklyn-technical-high-school), [Technology Analysis](http://schools.nyc.gov/nr/rdonlyres/f520ac97-18fc-4876-ae9c-2a2592e428a8/0/brooklyntech_v3.pdf)
- **William Cullen Bryant**: [ProPublica](http://projects.propublica.org/schools/schools/362058002887), [Big Apple Ed](http://www.bigappleed.com/schools/1376-william-cullen-bryant-high-school), [Wikipedia](http://en.wikipedia.org/wiki/William_Cullen_Bryant_High_School)
- **Harvey Milk**: [ProPublica](http://projects.propublica.org/schools/schools/362058005522), [Big Apple Ed](http://www.bigappleed.com/schools/124-harvey-milk-high-school)

### Wednesday 8/20

### For reference

- [Twitter Developer site](https://dev.twitter.com)
- [Forecast.io API Registration](https://developer.forecast.io/register)
- [Cron jobs](http://en.wikipedia.org/wiki/Cron)

#### Our notes

- [How to build a Twitter bot](twitter.md)
- [How to run tasks regularly using cron](cron.md)
- [Using the Forecast.io API](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/algorithms/09-Forecast-twitter.ipynb)

## Week 7: Networks and graphs

### Monday 8/25

- Networks
    - introduction and examples in data journalism
        + from NYT: [oscar net](http://www.nytimes.com/interactive/2013/02/20/movies/among-the-oscar-contenders-a-host-of-connections.html?_r=0)
        + from bostock: 
            - [uberdata](http://bost.ocks.org/mike/uberdata/)
            - [matrix plots](http://mbostock.github.io/protovis/ex/matrix.html)
            - [chord plots](http://bl.ocks.org/mbostock/4062006)
        + lots of work from [gilad lotan](http://giladlotan.com/), e.g., recent [media analysis around gaza](https://medium.com/i-data/israel-gaza-war-data-a54969aeb23e)
        - critical literacy: how do you reduce human interactions into a graph?
    - centralities (find 'important' nodes)
        - functional literacy
        - critical literacy: does choice of centrality matter?
    - graph drawing/graph visualization
        - critical literacy: does graph drawing mean anything? what are the axes?
    - graph partitioning/community detection
    - [example notebook](http://nbviewer.ipython.org/github/ledeprogram/courses/blob/master/algorithms/10-networkx-fun.ipynb)

- **Possibly useful**
    - [networkx](https://networkx.github.io/)
    - [2003 review article](http://arxiv.org/abs/cond-mat/0303516)
    - [cathy's 2012 blog post](http://mathbabe.org/2012/11/01/columbia-data-science-course-week-9-morningside-analytics-network-analysis-data-journalism/) based on a lecture from [john kelly](http://apidictionist.com/) of [morningside analytics](https://www.morningside-analytics.com/)
    -  [Social Network Analysis as a method in the Data Journalistic toolkit](http://www.academia.edu/6280420/Social_Network_Analysis_as_a_method_in_the_Data_Journalistic_toolkit) by Adriana Homolova - Academia.edu
    - [Social Network Analysis for Journalists Using the Twitter API](http://datadrivenjournalism.net/resources/social_network_analysis_for_journalists_using_the_twitter_api)


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

### Data sets

- NBA Census: https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/NBA-Census-10.14.2013.csv
- Iris data: https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/iris.csv
- Authorship data: https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/book-data.csv
- Mystery books: [1](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery1.txt) [2](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery2.txt) [3](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery3.txt) [4](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery4.txt) [5](https://raw.githubusercontent.com/ledeprogram/courses/master/algorithms/data/books/mystery5.txt) 

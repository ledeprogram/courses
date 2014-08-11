# examples taken from http://joshh.ug/SRPC/assignments/assignment4.html
# datafiles taken from http://joshh.ug/SRPC/assignments/datafiles3.zip
# (but without all_words.tsv ; big and not needed below)
# with a few typo's fixed, as indicated below

# <mise-en-place>
# needed imports from 2 solution modules

# 1.
# def read_entire_wfile(wfile):            Returns the counts and years for all words
# def read_wfile(word, year_range, wfile): Returns the counts and years for the word
# def read_total_counts(tfile):            Returns the total number of words
import one_gram_reader
from one_gram_reader import *

# 2.
# def total_occurrences(word_data, word):             Returns total occurrences of word
# def count_letters(word_data):                       Returns a list of length 26 corresponding to letter freqs
# def bar_plot_of_letter_frequencies(word_data)       Plots frequencies of letters
### Task 1: Plotting letter frequencies
# def plot_aggregate_counts(word_data, words):        Plots distribution of word frequencies, and annotates words
### Task 2: Plotting aggregate word counts
# def get_occurences_in_year(word_data, word, year):  Gets number of occurrences of word during year specified
# def get_average_word_length(word_data, year):       Gets the average length of all words from year specified
# def plot_average_word_length(word_data, year_range):Make a plot of average word length of year range specified
### Task 3: Plotting average word lengths vs. time
# def normalize_counts(years, counts, total):         Returns the normalized count
# def plot_words(words, year_range, wfile, tfile):    Plots the relative popularity of words over range specified


import one_gram_plotter
from one_gram_plotter import *

# </mise-en-place>

# example1 (testing read_entire_wfile)
word_data = read_entire_wfile("very_short.tsv")
print(word_data)
print("----------------------------")
print(word_data["request"])

### Task 1: Plotting letter frequencies

# example2, 
## import one_gram_reader
word_data = one_gram_reader.read_entire_wfile("very_short.tsv")
print(total_occurrences(word_data, "wandered"))    
print(total_occurrences(word_data, "quetzalcoatl"))

# example3
## import one_gram_reader
word_data = one_gram_reader.read_entire_wfile("very_short.tsv")
print(word_data)
print(count_letters(word_data))

# example4
## import one_gram_reader
word_data = one_gram_reader.read_entire_wfile("very_short.tsv")
bar_plot_of_letter_frequencies(word_data)

### Task 2: Plotting aggregate word counts

# example5
## import one_gram_reader
# had to rename datafile to words_that_start_with_q.tsv
word_data = one_gram_reader.read_entire_wfile("words_that_start_with_q.tsv")
plot_aggregate_counts(word_data, ["quest", "questions"])

### Task 3: Plotting average word lengths vs. time

# example6
# import one_gram_reader
# had to fix spelling of occurrence
word_data = one_gram_reader.read_entire_wfile("very_short.tsv")
print(word_data)
print(get_occurrences_in_year(word_data, "wandered", 2007))

# example7
## import one_gram_reader
word_data = one_gram_reader.read_entire_wfile("very_short.tsv")
print(word_data)
print(get_average_word_length(word_data, 2006))

# example8
## import one_gram_reader
# had to fix inconsistency on words_that_start_with_q.tsv vs words_that_start_with_letter_q.csv
word_data = one_gram_reader.read_entire_wfile("words_that_start_with_q.tsv")
plot_average_word_length(word_data, [1860, 1880])

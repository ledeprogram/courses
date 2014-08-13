# examples taken from http://joshh.ug/SRPC/assignments/assignment3.html
# datafiles taken from http://joshh.ug/SRPC/assignments/datafiles3.zip
# for this one (but not #4) we need all_words.tsv
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

# example1 
years, counts = read_wfile("request", [2005, 2007], "very_short.tsv")
print(years)
print(counts)

# example2
total_counts = read_total_counts("total_counts.csv")
print(total_counts[1507])
print(total_counts[1525])

# example3
## import one_gram_reader
years, counts = one_gram_reader.read_wfile("request", [2000, 2010], "very_short.tsv")
total = one_gram_reader.read_total_counts("total_counts.csv")    
print(years)
first_observed_year = years[0]
print(first_observed_year)
print(counts[0])
print(total[first_observed_year])
normalized_counts = normalize_counts(years, counts, total)
print(normalized_counts[0])                                #equal to 646179 / 14425183957

# example4
## SLOW:
## plot_words(["horse", "fish", "dog"], [1800, 2000], "all_words.tsv", "total_counts.csv")

# example5
plot_words(["horse", "fish", "pain", "joy"], [1800, 2000], "all_words.tsv", "total_counts.csv")


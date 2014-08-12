import csv 
import matplotlib.pyplot as plt 
from one_gram_reader import * 
import numpy as np 
 
#Counts the total number of times that word appears in word_data 
def total_occurrences(word_data, word): 
    if not word in word_data: 
        return 0 
         
    tuple_list = word_data[word] 
    sum = 0 
    for t in tuple_list: 
        sum = sum + t[1] 
         
    return sum 
 
#Counts the total number of occurrences of each letter in word_data 
def count_letters(word_data): 
    letter_counter = {} 
 
    #Count occurrences of each letter using a dictionary 
    for word, tuple_list in word_data.iteritems(): 
        for letter in word.lower(): 
            letter_counter[letter] = letter_counter.get(letter, 0) + total_occurrences(word_data, word) 
 
    counts = [] 
 
    #It's not safe to simply return letter_counter.values() because the letters 
    #might not be in alphabetical order. An alternate approach would have been 
    #to use the special data structure ordered_dictionary 
    for letter in "abcdefghijklmnopqrstuvwxyz": 
        counts.append(letter_counter.get(letter, 0)) 
         
    total = float(sum(counts)) 
     
    for i in range(len(counts)): 
        counts[i] = counts[i] / total 
         
    return counts  
 
def bar_plot_of_letter_frequencies(word_data): 
    counts = count_letters(word_data) 
 
    xval = np.arange(len(counts)) 
    plt.figure(1) 
    plt.clf()     
    plt.bar(xval, counts) 
    # label the axes
    plt.xlabel('Letter') 
    plt.ylabel('Total count') 
 
    #The 0.33 here is intended to center the letters a bit better.      
    plt.gca().set_xticks(xval + 0.33) 
 
    #Things look nicer with capital letters. 
    plt.gca().set_xticklabels("ABCDEFGHIJKLMNOPQRSTUVWXYZ")     
 
    #reset axes so that they are tight around the 26 letters of the alphabet 
    ax = plt.axis() 
    ax = (ax[0], 26, ax[2], ax[3]) 
    plt.axis(ax) 
    plt.draw() 
    plt.show()     
 
 
 
#Returns the normalized count 
#(normalize by total_count=total[years[i in range len(counts)]])
def normalize_counts(years, counts, total):      
    normalized_counts = [] 
 
    N = len(counts) 
    for i in range(N): 
        year = years[i] 
        try: 
            total_count = total[year] 
            normalized_count = counts[i] / float(total_count) 
            normalized_counts.append(normalized_count) 
        except: 
            normalized_counts.append(0) 
    return normalized_counts 
     
#Plots the relative popularity of words over range specified 
def plot_words(words, year_range, words_filename, totals_filename):     
    plt.figure(1) 
    plt.clf() 
    total = read_total_counts(totals_filename) 
    for word in words: 
        years, counts = read_wfile(word, year_range, words_filename) 
        normalized_counts = normalize_counts(years, counts, total)         
        plt.plot(years, normalized_counts) 
         
    plt.legend(words) 
    plt.xlabel('Year') 
    plt.ylabel('Relative frequency') 
    plt.grid() 
    plt.draw() 
    plt.show() 
 
def plot_relative_popularity(word1, word2, year_range, words_filename, totals_filename): 
    plt.figure(2) 
    plt.clf() 
    total = read_total_counts(totals_filename) 
    years1, counts1 = read_wfile(word1, year_range, words_filename) 
    years2, counts2 = read_wfile(word2, year_range, words_filename) 
 
    normalized1 = normalize_counts(years1, counts1, total)         
    normalized2 = normalize_counts(years2, counts2, total)             
     
    ratio = np.array(counts1, dtype = float) / np.array(counts2, dtype = float) 
    maxloc = np.argmax(ratio) 
    minloc = np.argmin(ratio) 
     
    w1peak = years1[np.argmax(ratio)] 
    w2peak = years2[np.argmin(ratio)] 
         
    plt.subplot(2, 1, 1) 
    plt.plot(years1, normalized1) 
    plt.plot(years2, normalized2) 
    plt.legend([word1, word2]) 
    plt.xlabel('Year') 
    plt.ylabel('Relative frequency') 
     
    plt.subplot(2,1,2) 
    plt.plot(years1, ratio) 
    plt.xlabel('Year') 
    plt.ylabel('Frequency ratio') 
    plt.legend([word1 + "/" + word2]) 
     
    plt.annotate(str(w1peak), xy=(w1peak, ratio[maxloc])) 
    plt.annotate(str(w2peak), xy=(w2peak, ratio[minloc]))     
    plt.grid()     
    plt.show() 
    plt.draw() 
 
 
 
def plot_total_counts(): 
    plt.figure(2) 
    plt.clf() 
    total = read_total_counts(total_csv_file) 
    plt.semilogy(total.keys(), total.values()) 
    z = plt.axis() 
 
    print(z) 
    plt.draw() 
    plt.show() 
 
#Plots the aggregate count of all words, with annotations for words in list 
def plot_aggregate_counts(word_data, words): 
    aggregate_counts = {} 
    for word in word_data.keys(): 
        aggregate_counts[word] = total_occurrences(word_data, word) 
         
    plt.figure(4) 
    plt.clf() 
  
 
    #use reverse sorted counts as y values 
    sorted_counts = aggregate_counts.values() 
    sorted_counts.sort(reverse=True) 
    #use rank as x values 
    xval = np.arange(len(sorted_counts)) 
 
    #plot both as a line and as markers 
    plt.loglog(xval, sorted_counts)     
    plt.loglog(xval, sorted_counts, 'o')     
 
    #annotate word with *s 
    for word in words: 
        total = total_occurrences(word_data, word) 
        try: 
            x_coord = sorted_counts.index(total)         
            print(x_coord) 
            plt.plot(x_coord, total, 'r*', ms = 12) 
            #factor of 1.1 is to make things look nicer 
            plt.annotate(word, xy = (x_coord * 1.1, total)) 
        except: 
            pass 
    plt.gca().autoscale_view(tight=True, scalex=True, scaley=True)     
             
    plt.xlabel('Rank of word') 
    plt.ylabel('Total number of occurrences') 
    plt.draw() 
    plt.show() 
 
def get_occurrences_in_year(word_data, word, query_year): 
    tuple_list = word_data[word] 
    for year, count in tuple_list: 
        if (year == query_year): 
            return count 
 
    return 0 
     
 
 
def get_average_word_length(word_data, year): 
    #assuming maximum word length is 30 or less. Seems ugly, there is probably 
    #a cleaner way to do this, but hey, this works well enough. 
    words_of_length_i = [0] * 30 
     
    for word in word_data.keys():      
        occurrences = get_occurrences_in_year(word_data, word, year) 
        words_of_length_i[len(word)] = words_of_length_i[len(word)] + occurrences 
 
    weighted_sum = 0 
 
    for i in range(30): 
        weighted_sum = weighted_sum + i * words_of_length_i[i] 
         
    total_words = sum(words_of_length_i) 
    if total_words == 0: 
        return 0 
    else: 
        return float(weighted_sum) / total_words 
         
             
#Plots the aggregate count of all words, with annotations for words in list 
def plot_average_word_length(word_data, year_range): 
    years = range(year_range[0], year_range[1] + 1) 
    awl = [] 
    for year in years: 
        awl.append(get_average_word_length(word_data, year)) 
         
    plt.figure(5) 
    plt.clf() 
    plt.plot(years, awl) 
    plt.xlabel('Year') 
    plt.ylabel('Average word length') 
 
 
    plt.draw() 
    plt.show() 

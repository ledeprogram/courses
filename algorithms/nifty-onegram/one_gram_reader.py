import csv
import pickle

def read_entire_wfile(filename):
    input_file = open(filename, "rb")

    csv_reader = csv.reader(input_file, delimiter="\t")

    word_counts = {}

    for row in csv_reader:
        word = row[0]
        if not word in word_counts:
            word_counts[word] = []
        year = int(row[1])
        count = int(row[2])
        word_counts[word].append((year, count))

    input_file.close()
    return word_counts

##Returns the counts and years for the word
def read_wfile(word, year_range, filename):              
    input_file = open(filename, "rb")
    csv_reader = csv.reader(input_file, delimiter="\t")
    
    years = []
    counts = []
    
    for row in csv_reader:
        year = int(row[1])

        if (row[0] == word):
            if (year <= year_range[1]) and (year >= year_range[0]):
                years.append(int(row[1]))
                counts.append(int(row[2]))
                                        
    input_file.close()
    return years, counts    

#Returns the total number of words
def read_total_counts(filename):     
    input_file = open(filename, "rb")
    csv_reader = csv.reader(input_file, delimiter=",")
    
   # csv_reader.next()
    total_during_year = {}
    for row in csv_reader:
        try:
            year = int(row[0])
            count = int(row[1])
            total_during_year[year] = count
        except:
            pass
            
    input_file.close()    
    return total_during_year

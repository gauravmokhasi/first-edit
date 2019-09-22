"""
@author = gauravmokhasi
This program lets writers know if they are repeating words -- something that they hate doing.
"""
import re

def read_file():
    """
    asks user to enter the name of the text file to analyze.
    then it opens that file
    """
    in_file = input("Enter name of text file without extension: ")+".txt"
    return open(in_file, 'r')

def split_wise(text):
    """
    takes an input string and splits it based on common english delimiters.
    returns a list of words in the string
    """
    # splitting on: , <whitespace> - ! ? : ; /
    return filter(None, re.split("[,\s\-!?:;/]+", text))
    
def build_dict(list_words, dict_words):
    """
    populates a dictionary based on the list of words.
    key = word. value = # of occurrences of word
    """
    for word in list_words:
        word = word.lower() # to ignore case
        if not word in dict_words:
            dict_words[word] = 1
        else:
            dict_words[word] += 1

def clean_up(dict_words, dict_words_copy):
    """
    cleans up the dictionary based on some rules.
    """
    remove_single_words(dict_words, dict_words_copy)
    remove_common_words(dict_words_copy)

def remove_single_words(dict_words, dict_words_copy):
    """
    removes words that occur only once.
    """
    for word in dict_words:
        if dict_words[word] == 1:
            del dict_words_copy[word]

def remove_common_words(dict_words_copy):
    """
    removes common english words that are not meaningful for analysis.
    user should specify these words in the ignore_words.csv file
    """
    ignore_words_file = open("ignore_words.csv", 'r')
    list_ignore_words = ignore_words_file.read().split(',')
    for word in list_ignore_words:
        if word in dict_words_copy:
            del dict_words_copy[word]
    ignore_words_file.close()

def create_analysis_file(sorted_word_count):
    analysis_file = open("analysis_file.txt", 'w+')
    analysis_file.write("Non-common words that appear more than once in your document.\n")
    # add "word: count" to file
    for item in sorted_word_count:
        analysis_file.write(str(item[0]) + ": " + str(item[1]) + "\n")
    analysis_file.write("(Think the list still has a lot of common words? ")
    analysis_file.write("Add the words you want to ignore to ignore_words.csv)")
    return analysis_file

# read input file that you want to analyze
document = read_file()

# get file contents and close
text = document.read()
document.close()

# get list of words in the file contents
list_words = split_wise(text)

# dictionary to hold how many times each word appears
dict_words = {}
build_dict(list_words, dict_words)

# make a copy of the dictionary - used to give user cleaner output
dict_words_copy = dict_words.copy()
clean_up(dict_words, dict_words_copy)

# reverse sort dict so that you see most frequently used words first
sorted_word_count = sorted(dict_words_copy.items(), key=lambda x: x[1], reverse = True)

# create analysis_file and close
analysis_file = create_analysis_file(sorted_word_count)
analysis_file.close()

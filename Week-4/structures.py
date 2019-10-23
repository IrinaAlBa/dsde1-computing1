'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containing the first and the last element
# of "the_list". 
def first_and_last(the_list):
    """This function returns a list containing the first and last elements of the_list"""
    new_list = [the_list[0],the_list[-1]]
    return new_list


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is less than "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    """This function reverses the second and third parameter and outputs them in a new list"""
    if (end < beginning) or (end >= len(the_list)) or (beginning < 0):
        raise ValueError("improper list indexes")
    new_list = the_list[beginning:end+1]
    return new_list.reverse()

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    """This function inserts two times the same value into the list."""
    n_times = 2
    value = the_list[index]
    while n_times > 0:
        the_list.insert(index, value)
        n_times -= 1
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    word = input()
    rev_word = word[::-1]
    if word == rev_word:
        return word
    else:
        print("This is not a palindrome")

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence = input()
    rev_sentence = sentence[::-1]
    if sentence == rev_sentence:
        return sentence
    else:
        print("This is not a palindrome")

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    sentence1[0].isupper()
    #have to put in an endswith function somewhere here, but not sure how.
    #also, have to strip whitespace on the ends of both sentences, then .ljust(1, " ") to the second one.
    return


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    key = input()
    key in dictionary.keys()
    return

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    value = input()
    value in dictionary.values()
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    new_dictionary = dictionary1.copy()
    new_dictionary.update(dictionary2)
    return new_dictionary

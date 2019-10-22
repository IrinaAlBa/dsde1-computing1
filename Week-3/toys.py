'''
toys.py
Simple toy functions to get comfortable working 
with functions.
'''

# write a function that adds 1
# to the input and prints the result
def inc(a):
   number = a + 1
   print(number)


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    number = a + 1
    return number


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    number = a + b
    return number


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    number = sum(a,b)
    number1 = inc_return(number)
    return number1


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    return  a % 2 == 0


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    # hint: you can add strings together 
    # in order to concatenate them
    final_phrase = ""
    for i in range(repeat):
        final_phrase += phrase
    return final_phrase
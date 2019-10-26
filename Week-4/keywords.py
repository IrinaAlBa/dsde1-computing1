'''
keywords.py
Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name = 0, place = 0):
    if user_name == 0 and place == 0:
        print("Hello and welcome")
    if user_name !=0 and place == 0:
        print("Hello " + str(user_name) + " and welcome")
    if user_name != 0 and place != 0:
        print("Hello " + str(user_name) + " and welcome to " + str(place))

# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword argument is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

# check if for median one has to sort the list

def list_average(a_list, avg_type = 0):
    n = len(a_list)
    get_sum = sum(a_list)
    mean = get_sum / n
    a_list.sort()
    if n % 2 == 0: 
        median1 = a_list[n//2] 
        median2 = a_list[n//2 - 1] 
        median = (median1 + median2)/2
    else:
        median = a_list[n//2]
    from collections import Counter
    data = Counter(a_list)
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if avg_type == 0 or avg_type == "mean":
        return mean
    if avg_type == "mode":
        if len(mode) == n: 
            get_mode = "No mode found"
        else: 
            get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
    if avg_type == "median":
        return median
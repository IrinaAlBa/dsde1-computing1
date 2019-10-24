'''
keywords.py
<<<<<<< HEAD
=======

>>>>>>> upstream/master
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
<<<<<<< HEAD
def welcome_message(user_name = 0, place = 0):
    if user_name == 0 and place == 0:
        print("Hello and welcome")
    if user_name !=0 and place == 0:
        print("Hello " + str(user_name) + " and welcome")
    if user_name != 0 and place == 0:
        print("Hello " + str(user_name) + " and welcome to " + str(place))


def list_average(a_list, avg_type):
    a_list = []

    if avg_type == "mean":
        return
=======
>>>>>>> upstream/master


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
<<<<<<< HEAD
# the second optional keyword argument is called avg_type
=======
# the second optional keyword arguemt is called avg_type
>>>>>>> upstream/master
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
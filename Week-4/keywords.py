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
def welcome_message(user_name = "", place = ""):
    """This function gives a welcome message. If no username or place is provided,
    then the function simply prints 'Hello and welcome'. If a username is provided
    then 'Hello <user_name> and welcome' will be printed. If both keyword arguments
    are provided, then 'Hello <user_name> and welcome to <place> will be printed."""
    user = str(user_name)
    if user:
        user = f', {user},'
    location = str(place)
    if location:
        location = f' to {location}'
    return f"Hello{user} and welcome{location}"

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

def list_average(a_list, avg_type = "mean"):
    """This function returns the mean of a list if nothing, or 'mean' is called.
    if 'mode' is called, it returns the mode of the function, and if 'median',
    it returns the median."""
    n = len(a_list)

    if not avg_type in ["mean", "median", "mode"]:
        raise ValueError("Unknown avg type")

    if avg_type == "mean":
        return 0 if n == 0 else sum(a_list)/n
    
    a_list.sort()
    index = n // 2
    if avg_type == "median":
        if n == 0:
            return None
        if n % 2:
            return a_list[index]
        else:
            return (a_list[n//2]+a_list[n//2 -1])/2.0
    
    if n == 0:
        return []
        
    mode = max(a_list, key=a_list.count)
    max_count = a_list.count(mode)
    out = []
    for x in set(a_list):
        if a_list.count(x) == max_count:
            out.append(x)
    return out
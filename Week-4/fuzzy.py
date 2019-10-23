'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    """ This function does some maths on three numbers"""
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    """This function returns True or False."""
    return bool(question)

    # first function takes three numbers
    # second function takes a True or False
def main():
    """The first function takes three numbers.
    The second function takes a True or False."""
    answer = maths(3, 9, 2.3)
    print(answer)
    new_answer = choices(True)
    print(new_answer)

if __name__ == '__main__':
    main()
    
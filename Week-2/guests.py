name = ''
while not name:
    print('Enter your name: ')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Make sure to have enough room for everyone!')
print('Have a lovely time :)')
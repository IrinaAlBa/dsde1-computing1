import random
guess = input("Take a wild guess: ")
guess = int(guess)
number = random.randint(1,10)
if guess == number:
    print("You are right!")
else:
    print("You are wrong.")
    num_tries = 1
    while num_tries < 3:
        print('You have ' + str(3-num_tries) + ' tries left. Try again.')
        num_tries = num_tries + 1
        print('Take a wild guess: ')
        guess = input()
        guess = int(guess)
        number = random.randint(1,10)
        if guess == number:
            print("You are right!")
        else:
            continue
     if num_tries == 3:
        print('You lose.')
    break
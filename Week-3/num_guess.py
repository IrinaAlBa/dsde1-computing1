import random
guess = input("Take a wild guess: ")
guess = int(guess)
number = random.randint(1,10)
answer = guess == number
print(answer)
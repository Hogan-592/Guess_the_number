#This project uses random library that's built in python and ueser to guess that random number
import random

#Define a function which we can call upon
def guess(x):
    #randint is a method defined in random library which takes two parameters for a range
    random_number = random.randint(1, x)
    guess = 0 #set this number to be zero so it won't equal to the random number as it startas with 1
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low')
        elif guess > random_number:
            print('Sorry, guess again. Too high')

    #The following line only executes when the while loop is broke
    print(f'Yay, congrats. You have guessed the number {random_number}')

#Call the function
guess(10)

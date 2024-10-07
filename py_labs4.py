#!/bin/python3

user_reply = input("Need to ship a package? enter yes or no")

if user_reply == "yes":
    print("We can help!")
elif user_reply == "no":
    print("That's a shame!")
else:
    print("Enter yes or no only!")

import random

my_num = random.randint(1,10)

is_guess_correct = False

while is_guess_correct != True:
    guess = input("guess between 1-10")
    if int(guess) == my_num:
        print("You guessed {}. It's right, you win!".format(guess))
    else:
        print("You guessed {}. Pathetic.".format(guess))

for x in range(0, 11):
    print(x)



#!/bin/python3 

print("Hello again, World!")

my_string = "This is a string!"

print(my_string, "is of type", type(my_string))

two_string = "And this is too!" 

g_string = my_string + two_string 

print(g_string)

name = input("What's your name? ")

print(name)

def take_fave_input(noun):
    input(f"what is your favourite {noun}? ")

nouns = ["colour", "animal"]

for noun in nouns:
    take_fave_input(noun)

print("{}, you did it slightly wrong! ".format(name))

print(nouns[0], nouns[1])

nouns[1] = "science"

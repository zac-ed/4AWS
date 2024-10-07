#!/bin/python3

fruits = ("apple", "orange", "pineapple")

print(fruits, type(fruits), fruits[0], fruits[1], fruits[2])

fruit_dict = {
  "Zac" : "apple",
  "Ranjith" : "orange",
  "Kunal" : "pineapple"
}

print(fruit_dict, type(fruit_dict))

print(fruit_dict["Zac"], fruit_dict["Kunal"])

mix_types = [45, 290578, 1.02, True, "My cat is on the bloody side, again!", "45"]

for item in mix_types:
    print("{} is of the data type {}".format(item, type(item)))



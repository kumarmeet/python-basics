# indentation is very important in python

# under the function get_choices both statment is intended with same
import random

def greeting():
  return "Hello World"

# dictionaries (used to data values in key value pairs)
dict = {"name": "Meet", "age": 32}

print(dict["age"])

#user input
def input_number():
  value1 = input("Input value 1 ")
  value2 = input("Input value 2 ")

  return {value1, value2}

# print(input_number())

#lists is used for group items into single variable
#lists contain any type of data into list
food = ["pizza", "momos", "dal", "rice"]

print(random.choice(food))

age = 21
print("Jim age is" + age)

#f string
print(f"Jim age is {age}")







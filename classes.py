# self in an argument of method will 
# point to current obj instance and 
# it must be specified when defining a method

# defining a constructor __init__

# inheritance put the class name in derived class -> class Dog(Animal)

class Animal:
  def walking(self):
    print("Walking")

class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def barking(self):
    print("Woof....")
  
  def dogData(self):
    print(f"Hello, {self.name} and age is {self.age}")


shaggy = Dog("Shaggy", 4)

shaggy.barking()
shaggy.walking()

shaggy.dogData()
    
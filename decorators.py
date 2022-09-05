#whenever we call the hello function
# the decorators is going to be called

# Decorators is a function that takes a function
# as a parameter wraps the function in an inner function
# that performs the jobs has to do and returns that inner function
# #

# it is useful when you want to change a behavior of a function without modifying a function
# and need to run same code on multiple functions


def logtime(func):
  def wrapper():
    #do something before
    print("before")
    val = func()
    print("after")
    #do something after
    return val
  return wrapper

@logtime
def hello():
  print("Hello........")
  
hello()




# if return a nested function from a 
# function that nested function has access those variables
# event if that function is not active anymore 

def counter():
  count = 0
  
  def increment():
    nonlocal count #this allows to access the variable which is declare in outer function 
    count = count + 1
    return count
  
  return increment

increment = counter()

print(increment())
print(increment())
print(increment())


# normal function
def greeting(name):
  return f"Hello {name}"

# nested function
# make a nested function when that function work only that specific function only
def sum(num1, num2):
  result = num1 + num2
  
  def data():
      print(result)
      
  data()

sum(10, 20)

# if want to access a variable defined in the outer function from the inner function
# need declare the as nonlocal keyword
def count():
  count = 0
  
  def increment():
    nonlocal count #this allows to access the variable which is declare in outer function 
    count = count + 1
    print(count)
  
  increment()

count()
    
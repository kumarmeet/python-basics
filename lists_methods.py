from functools import reduce


nums = [1,2,3,4,5,6,7,8,9,10]

result = map(lambda num: num * 2, nums)

print(list(result))

users = [{"id":"12345"}, {"id": "56789"}]

def check_id(obj):
  if obj["id"] == "12345":
    return True
  
result = map(check_id, users)

print(list(result))


data = [1,5,9,3,4,52,7,8,65,4,10,32,51,69]

def filter_data(n):
  if n > 40:
    return n
  
result = filter(filter_data, data)

print(list(result))


expenses = [("Dinner", 80), ("Car Repair", 120)]

print(expenses[0][1]) #pull out 0th index value and then takes 1 index value in tuple

sum = 0

for expense in expenses:
  sum += expense[1] # have to check this line execution

print(sum)

summation = reduce(lambda a, b: a[1] + b[1], expenses)

print(summation)

nums = [1,2,3,4,5]

sum = 0

for idx, n in enumerate(nums):
  sum += n
  
print(sum)

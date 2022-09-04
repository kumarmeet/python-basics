# python has for and while loop

i = 0

while i <= 4:
  print(i)
  i = i + 1
  
nums = [1,2,3,4,5,6,7,8,9,10]

for num in nums:
  print(num)

for num in range(4):
  print("Hello")
  
#indexing

for idx, num in enumerate(nums):
  print(idx, num)
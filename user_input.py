# number guessing game

from random import choice

nums = [1,2,3,4,5,6,7,8,9,10]

while(True):
  user_value = input("Enter number: ")
  your_number = choice(nums)
  
  if(user_value == your_number):
    print("You Win")
    break
  else:
    print(f"You Lose, original number is {your_number}")
    
    key = input(f"Do you want to continue, press y or Y and no ANY KEY: ")
    if key == "y" or key == "Y":
      continue
    else:
      break
    
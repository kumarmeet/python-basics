# indentation is very important in python

# under the function get_choices both statment is intended with same
import random

def check_win(choices):
  print(f"You chose {choices['player']} and computer chose {choices['computer']}")

  if choices["player"] == choices["computer"]:
    return "Tie"
  elif choices["player"] == "rock" and choices["computer"] == "scissors":
    return "Player wins"
  elif choices["player"] == "scissors" and choices["computer"] == "paper":
    return "Player wins"
  elif choices["player"] == "paper" and choices["computer"] == "rock":
    return "Player wins"
  else:
    return "Computer wins"

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: )")
  options = ["paper", "rock", "scissors"];
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}

  return check_win(choices)

result = get_choices()

print(result)
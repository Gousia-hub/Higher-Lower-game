from art import logo
from art import vs
#art 
from replit import clear
#random
#format
#compare



from game_data import data
import random
def choice():
  return random.choice(data)

def format_acc(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"


#check
def check_ans(guess,follo_A,follo_B):
  if follo_A > follo_B:
    return guess == "a"
  else:
    return guess == "b"
    
def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = choice()
  account_b = choice() 
  
  while game_should_continue:
    
  

    while account_a == account_b:
      account_b = choice()

    A = format_acc(account_a)
    print(f"Comapre A: {A}")
    print(vs)
    B = format_acc(account_b)
    print(f"Comapre B: {B}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    follo_A = account_a["follower_count"]
    follo_B = account_b["follower_count"]
    is_crt = check_ans(guess,follo_A,follo_B)
      
    clear()
    print(logo)  

    
    if is_crt:
      score += 1
      print(f"ur ryt! current score: {score}")
      account_a = account_b
      account_b = random.choice(data)
      
    else:
      print("sry! wrng")
      print(f"ur final score is {score}")
      game_should_continue = False
game()
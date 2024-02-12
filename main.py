from game_data import data
import random


contenstants = []

def add_new():
  choice = random.choice(data)
  contenstants.append(choice)

def game():
  is_playing = True
  exclude_list = []
  score = 0
  add_new()
  add_new()
  
  while is_playing:
    first_contender = contenstants[0]
    second_contender = contenstants[1]
    print(f"Compare A: {first_contender['name']}, a {first_contender['description']}, from {first_contender['country']}")
    print(f"Against B: {second_contender['name']}, a {second_contender['description']}, from {second_contender['country']}")
    
    if first_contender['name'] == second_contender['name']:
      exclude_list.append(second_contender)
      contenstants.pop()
      add_new()
      
    user_choice = input("Who has more followers? Choose A or B: ").lower()
    
    if user_choice == 'a':
      if first_contender['follower_count'] > second_contender['follower_count']:
        exclude_list.append(second_contender)
        contenstants.pop()
        add_new()
        score += 1
      elif first_contender['follower_count'] < second_contender['follower_count']:
        is_playing = False
        print("You lose")
        print(f"Your score is: {score}")
        
    elif user_choice == 'b':
      if first_contender['follower_count'] < second_contender['follower_count']:
        contenstants[0] = contenstants[1]
        contenstants.pop()
        add_new()
        score += 1
      elif first_contender['follower_count'] > second_contender['follower_count']:
        is_playing = False
        print("you lose")
        print(f"Your score is: {score}")
        
    exclude_list.append(second_contender)
    exclude_list.append(first_contender)
    
    if first_contender or second_contender in exclude_list:
      contenstants.pop()
      add_new()
      

game()

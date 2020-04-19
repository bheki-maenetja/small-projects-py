from random import choice

def main():
  input("WELCOME TO ROCK, PAPER, LIZARD, SCISSORS, SPOCK >>> ")
  final_user_score, final_comp_score = play_game()
  input(f"GAME OVER >>> ")
  input(f"Final Scores: Player {final_user_score} - {final_comp_score} Computer >>> ")
  input(f"Thank you for playing!!! >>> ")

def play_game():
  user_score = 0
  comp_score = 0

  choice_table = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors'],
  }

  while True:
    user_choice = get_user_choice()
    if user_choice == 'q': break

    input(f"Player Choice: {user_choice.upper()} >>> ")
    comp_choice = choice(['rock', 'paper', 'scissors', 'lizard', 'spock']).lower()
    input(f"Computer Choice: {comp_choice.upper()} >>> ")

    if comp_choice == user_choice:
      input("It's a tie!!! >>> ")
    elif comp_choice in choice_table[user_choice]:
      input("You won!!! >>> ")
      user_score += 1
    else:
      input("You lost >>> ")
      comp_score += 1
    
    input(f"Scores: Player {user_score} - {comp_score} Computer >>> ")

  return (user_score, comp_score)

def get_user_choice():
  print(f"\nCHOICES\n{7*'-'}\n* Rock\n* Paper\n* Scissors\n* Lizard\n* Spock\n")
  while True:
    try:
      choice = input("Enter your choice or press 'q' to quit: ").strip().lower()
      if choice not in ['rock', 'paper', 'scissors', 'lizard', 'spock', 'q']: raise ValueError
    except ValueError:
      print("Please enter a valid choice")
    else:
      break
  
  return choice

main()
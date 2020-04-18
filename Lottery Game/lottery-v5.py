from random import sample

def main():
  input("WELCOME TO THE LOTTERY!!! >>> ")

  total_winnings = 0
  
  num_rounds = get_integer(1, 10, "How many rounds do you want to play?\nEnter a number between 1 and 10")
  # print(num_rounds)
  play_lotto()

def play_lotto():
  # ticket = None
  # draw = None
  # winnings = 0
  # num_matches = 0

  game_settings = [
    (10, '10-ball'),
    (20, '20-ball'),
    (50, '50-ball'),
    (100, '100-ball'),
    (1000, '1000-ball')
  ]

  print(f"\nGAME MODE\n{9*'-'}\n" + "\n".join([f"{game_settings.index(i) + 1}) {i[1]}" for i in game_settings]) + "\n")
  setting_index = get_integer(1, 5, "To set the game mode enter it's corresponding number")
  game_setting = game_settings[setting_index - 1]
  
  input(f"You have chosen {game_setting[1]} >>> ")
  ticket = get_ticket(game_setting[0])
  draw = sample(range(1, game_setting[0] + 1), 6)
  print(f"Your ticket: {ticket}\nThe draw: {draw}")

def get_ticket(num_range):
  input("Time to enter your lotto numbers >>> ")
  ticket = []

  while len(ticket) != 6:
    if len(ticket) > 0: print(f"Your lotto numbers: {ticket}")
    lotto_num = get_integer(1, num_range, f"Enter a number between 1 and {num_range}")
    if lotto_num in ticket: 
      print("You already entered this number!!!")
    else:
      ticket.append(lotto_num)
  
  return ticket

# Utitlity Functions
def get_integer(min_value, max_value, input_prompt):
  while True:
    try:
      number = int(input(f"{input_prompt}: "))
      if number not in range(min_value, max_value + 1): raise ValueError
    except ValueError:
      print(f"Please enter a number between {min_value} and {max_value}!")
    else:
      break
  
  return number

main()
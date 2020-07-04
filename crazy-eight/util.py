# User Input
def get_integer(min_value, max_value, input_prompt):
  while True:
    try:
      number = int(input(f"{input_prompt}: "))
      if number not in range(min_value, max_value + 1): raise ValueError
    except ValueError:
      print(f"Please enter a number between {min_value} and {max_value}!!!")
    else:
      break
  
  return number

def get_string(min_length, max_length, input_prompt, accept_values=None):
  while True:
    try:
      string = input(f"{input_prompt}: ").lower()
      if accept_values != None:
        if string not in accept_values: raise ValueError
      if len(string) > max_length or len(string) < min_length: raise ValueError
    except ValueError:
      pass
    else:
      break
  
  return string

# Display Functions
def print_game_board(num_player_cards, num_comp_cards, current_card):
  print("STATE OF PLAY\n-------------")
  print(f"Player {num_player_cards} - {num_comp_cards} Computer\n")
  print(f"Current Card: {current_card}")
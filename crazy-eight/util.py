from random import shuffle

# Card Handling
def assign_cards(card_deck):
  player_cards, comp_cards = [], []
  for deck in (player_cards, comp_cards):
    for i in range(8):
      new_card = card_deck.pop()
      deck.append(new_card)
  
  while True:
    new_card = card_deck.pop()
    if not new_card.is_power:
      pile = [new_card]
      break
    else:
      card_deck.append(new_card)
      shuffle(card_deck)

  stack = card_deck
  return player_cards, comp_cards, stack, pile

def test_cards(main_deck, player_cards, comp_cards, stack, pile): # checks to see if there are any cards in more than one place
  for card in main_deck:
    list_count = 0
    for item in (player_cards, comp_cards, stack, pile):
      if card in item:
        list_count += 1
    print(card, list_count)

# User Input
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

def get_string(min_length, max_length, input_prompt, accept_values=None):
  while True:
    try:
      string = input(f"{input_prompt}: ").lower()
      if not accept_values:
        if string not in accept_values: raise ValueError
      if len(string) > max_length or len(string) < min_length: raise ValueError
    except ValueError:
      print(f"{input_prompt}: ")
    else:
      break
  
  return string

# Display Functions
def print_game_board(num_player_cards, num_comp_cards, current_card):
  print("STATE OF PLAY\n-------------")
  print(f"Player {num_player_cards} - {num_comp_cards} Computer\n")
  print(f"Current Card: {current_card}")
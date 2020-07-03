from random import shuffle, choice
import util

# CLASSES
class Card():

  card_names = {
    0: 'joker',
    1: 'ace',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'jack',
    12: 'queen',
    13: 'king'
  }

  def __init__(self, value, suite):
    self.value = value
    self.suite = suite
    self.is_power = True if value in [0, 2, 7, 8, 11] else False
    self.name = f"{self.card_names[value]} of {suite}" if value != 0 else f"{self.card_names[value]}"
  
  def __str__(self):
    return f"{self.name.title()}"

# FUNCTIONS

# Main Functions
def main(): # the main game function
  main_deck = get_card_deck()
  shuffled_deck = main_deck[:]
  shuffle(shuffled_deck)
  player_cards, comp_cards, stack, pile = util.assign_cards(shuffled_deck)
  # util.test_cards(main_deck, player_cards, comp_cards, stack, pile)

  current_card = pile[-1]
  current_suite = pile[-1].suite
  is_player_turn = True

  util.print_game_board(len(player_cards), len(comp_cards), current_card)

  while True:
    # Process Input (events)
    if len(player_cards) == 0 or len(comp_cards) == 0:
      break
    if is_player_turn:
      is_player_turn = not is_player_turn
      player_choice = util.get_string(1, 1, "Press p to take a card or c to view your your deck", ['c', 'p'])
      if player_choice == 'c':
        view_cards(player_cards)
      elif player_choice == 'p':
        print("You want to pick a card")
    # Update

  input("GAME OVER\nThank your for playing >>> ")

# Other Game Functions
def get_card_deck():
  card_deck = []

  for suite in ['hearts', 'diamonds', 'flowers', 'spades']:
    for i in range(1, 14):
      new_card = Card(i, suite)
      card_deck.append(new_card)
  
  for i in range(2):
    new_joker = Card(0, '')
    card_deck.append(new_joker)
  
  return card_deck

def view_cards(deck):
  print("\nYour cards:")
  for i, card in enumerate(deck):
    print(f"{i+1}) {card}")

# Function Calls
main()
  
    
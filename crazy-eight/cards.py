from random import shuffle, choice
from util import get_integer

# The Card Class
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
    if value == 2:
      self.power_value = 2
    elif value == 0:
      self.power_value = 6
  
  def __str__(self):
    return f"{self.name.title()}"

# CARD FUNCTION

# Creating the Deck and Assigning Cards
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

def check_stack(stack, pile):
  if len(stack) < 21:
    pile_cards = pile[:-1]
    shuffle(pile_cards)
    stack += pile_cards
    last_card = pile[-1]
    pile.clear()
    pile.append(last_card)

# Debugging
def test_cards(main_deck, player_cards, comp_cards, stack, pile): # checks to see if there are any cards in more than one place
  for card in main_deck:
    list_count = 0
    for item in (player_cards, comp_cards, stack, pile):
      if card in item:
        list_count += 1
    print(card, list_count)

def print_status(pile, stack, comp_cards):
  input(f"There are now {len(pile)} cards in the pile, {len(stack)} cards in the stack and the computer has {len(comp_cards)} cards >>> ")

# Display
def view_cards(deck, heading):
  print(f"\n{heading}:")
  for i, card in enumerate(deck):
    print(f"{i+1}) {card}")
  print()

def print_game_board(num_player_cards, num_comp_cards, current_card):
  print("STATE OF PLAY\n-------------")
  print(f"Player {num_player_cards} - {num_comp_cards} Computer\n")
  print(f"Current Card: {current_card}")

# Choosing and Playing
def play_card(deck, current_card, current_suite, is_attacked=False):
  input_prompt = "Choose a card by entering it's corresponding number or press 0 to go back" if not is_attacked else "Choose a card by entering it's corresponding number or press 0 to take the cards"

  if current_card.value in [0, 2] and is_attacked:
    viable_cards = [card for card in deck if card.value == 0 or card.value == 2]
  elif current_card.value == 0 and not is_attacked:
    viable_cards = deck.copy()
  else:
    viable_cards = [card for card in deck if card.value == current_card.value or card.suite == current_suite or card.value == 0]
    
  if len(viable_cards) > 0:
    view_cards(viable_cards, 'Here are the cards that you can play')
    card_choice_index = get_integer(0, len(viable_cards), input_prompt) - 1
    if card_choice_index == -1 and is_attacked:
      return 1
    elif card_choice_index == -1:
      return None
    card_choice = viable_cards[card_choice_index]
    deck.remove(card_choice)
    return card_choice
  elif len(viable_cards) == 0 and is_attacked:
    input("Eish! Looks like you're going to have to take those cards >>> ")
    return 1
  else:
    input("Yikes! Looks like there aren't any cards that you can play >>> ")
    return None

def comp_play_card(deck, current_card, current_suite, is_attacked=False):
  if current_card.value in [0, 2] and is_attacked:
    viable_cards = [card for card in deck if card.value == 0 or card.value == 2]
  elif current_card.value == 0 and not is_attacked:
    viable_cards = deck.copy()
  else:
    viable_cards = [card for card in deck if card.value == current_card.value or card.suite == current_suite or card.value == 0]
  
  if len(viable_cards) > 0:
    card_choice = choice(viable_cards)
    deck.remove(card_choice)
    return card_choice
  elif len(viable_cards) == 0 and is_attacked:
    input("The computer will take those cards >>> ")
    return 1
  else:
    return None

# Power Cards
def change_suite():
  input("\nYou can now change the current suite >>> ")
  choices = ['hearts', 'diamonds', 'flowers', 'spades']

  for i, choice in enumerate(choices):
    print(f"{i+1}) {choice.title()}")
  print()
  
  suite_choice_index = get_integer(1, len(choices), "To choose a suite enter it's corresponding number") - 1
  suite_choice = choices[suite_choice_index]
  input(f"You have chosen {suite_choice.title()} >>> ")
  return suite_choice

def comp_change_suite():
  input("\nThe computer will change the current suite >>> ")
  choices = ['hearts', 'diamonds', 'flowers', 'spades']
  suite_choice = choice(choices)
  input(f"The computer has chosen {suite_choice} >>> ")
  return suite_choice

def take_cards(attack_value, deck, stack):
  for i in range(attack_value):
    new_card = stack.pop()
    deck.append(new_card)

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
  
  def __str__(self):
    return f"{self.name.title()}"

# CARD FUNCTIONS

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

# Testing
def test_cards(main_deck, player_cards, comp_cards, stack, pile): # checks to see if there are any cards in more than one place
  for card in main_deck:
    list_count = 0
    for item in (player_cards, comp_cards, stack, pile):
      if card in item:
        list_count += 1
    print(card, list_count)

# Display
def view_cards(deck, heading):
  print(f"\n{heading}:")
  for i, card in enumerate(deck):
    print(f"{i+1}) {card}")
  print()

# Choosing and Playing
def play_card(deck, current_card):
  if current_card.value == 0:
    viable_cards = deck.copy()
  else:
    viable_cards = [card for card in deck if card.value == current_card.value or card.suite == current_card.suite or card.value == 0]
  if len(viable_cards) > 0:
    view_cards(viable_cards, 'Here are the cards that you can play')
    card_choice_index = get_integer(1, len(viable_cards), "Choose a card by entering it's corresponding number") - 1
    print(f"You want to play: {viable_cards[card_choice_index]}")
  else:
    input("Yikes! Looks like there aren't any cards that you can play >>> ")

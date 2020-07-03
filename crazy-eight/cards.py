from random import shuffle, choice

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

# Card Handling
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

def test_cards(main_deck, player_cards, comp_cards, stack, pile): # checks to see if there are any cards in more than one place
  for card in main_deck:
    list_count = 0
    for item in (player_cards, comp_cards, stack, pile):
      if card in item:
        list_count += 1
    print(card, list_count)

def view_cards(deck):
  print("\nYour cards:")
  for i, card in enumerate(deck):
    print(f"{i+1}) {card}")
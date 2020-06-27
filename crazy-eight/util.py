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
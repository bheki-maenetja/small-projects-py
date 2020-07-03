from random import shuffle, choice

import cards
import util

# THE MAIN FUNCTION
def main(): # the main game function
  main_deck = cards.get_card_deck()
  shuffled_deck = main_deck[:]
  shuffle(shuffled_deck)
  player_cards, comp_cards, stack, pile = cards.assign_cards(shuffled_deck)
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
        cards.view_cards(player_cards)
      elif player_choice == 'p':
        print("You want to pick a card")
    # Update

  input("GAME OVER\nThank your for playing >>> ")

main()
  
    
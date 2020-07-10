from random import shuffle, choice

import cards
import util

# THE MAIN FUNCTION
def main(): # the main game function
  main_deck = cards.get_card_deck()
  shuffled_deck = main_deck[:]
  shuffle(shuffled_deck)
  player_cards, comp_cards, stack, pile = cards.assign_cards(shuffled_deck)
  # cards.test_cards(main_deck, player_cards, comp_cards, stack, pile)

  current_card = pile[-1]
  current_suite = pile[-1].suite
  is_player_turn = True
  player_choice = ''

  util.print_game_board(len(player_cards), len(comp_cards), current_card)

  while True:
    # Process Input (events)
    if len(player_cards) == 0 or len(comp_cards) == 0:
      break
    while is_player_turn:
      if player_choice == 'c':
        cards.view_cards(player_cards, 'Your cards')
        player_choice = util.get_string(1,1, 'Press b to go back or p to play a card', accept_values=['b', 'p'])
      elif player_choice == 'p':
        player_card = cards.play_card(player_cards, current_card)
        if player_card != None:
          pile.append(player_card)
          input(f"You have played the {player_card} >>> ")
          current_card = pile[-1]
          current_suite = current_card.suite
          is_player_turn = False
        else:
          player_choice = ''
      elif player_choice == 't':
        new_player_card = stack.pop()
        player_cards.append(new_player_card)
        input(f"You have taken the {new_player_card} >>> ")
        is_player_turn = False
      else:
        player_choice = util.get_string(1, 1, "Press t to take a card, c to view your your deck or p to play a card", ['c', 'p', 't'])
    else:
      input(f"There are now {len(pile)} cards in the pile, {len(stack)} cards in the stack and the computer has {len(comp_cards)} cards >>> ")
      input("Its the computer's turn now! >>> ")
      is_player_turn = True
      player_choice = ''
    # Update
    util.print_game_board(len(player_cards), len(comp_cards), current_card)

  input("GAME OVER\nThank your for playing >>> ")

main()
  
    
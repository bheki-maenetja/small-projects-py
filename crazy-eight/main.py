from random import shuffle, choice

import cards
import util

# THE MAIN FUNCTION
def main():
  main_deck = cards.get_card_deck()
  shuffled_deck = main_deck[:]
  shuffle(shuffled_deck)
  player_cards, comp_cards, stack, pile = cards.assign_cards(shuffled_deck)

  current_card = pile[-1]
  current_suite = pile[-1].suite
  is_player_turn = True
  player_choice = ''
  attack_value = 0

  cards.print_game_board(len(player_cards), len(comp_cards), current_card)

  while True:
    # Process Input (events)
    if len(player_cards) == 0 or len(comp_cards) == 0:
      break
    while is_player_turn:
      if player_choice == 'c':
        cards.view_cards(player_cards, 'Your cards')
        player_choice = util.get_string(1,1, 'Press b to go back or p to play a card', accept_values=['b', 'p'])
      elif player_choice == 'p':
        player_card = cards.play_card(player_cards, current_card, current_suite, attack_value > 0)
        if player_card != None and player_card != 1:
          input(f"You have played the {player_card} >>> ")
          pile.append(player_card)
          current_card = pile[-1]
          current_suite = current_card.suite
          is_player_turn = True if current_card.value == 7 or current_card.value == 11 else False
          if current_card.value == 8:
            current_suite = cards.change_suite()
          elif current_card.value in [0, 2]:
            attack_value += current_card.power_value
        elif player_card == 1:
          input(f"The player will take {attack_value} cards >>> ")
          attack_value = 0
          is_player_turn = False
        player_choice = ''
      elif player_choice == 't':
        new_player_card = stack.pop()
        player_cards.append(new_player_card)
        input(f"You have taken the {new_player_card} >>> ")
        is_player_turn = False
        player_choice = ''
      else:
        player_choice = util.get_string(1, 1, "Press t to take a card, c to view your your deck or p to play a card", ['c', 'p', 't']) if attack_value == 0 else 'p'
    else:
      cards.print_status(pile, stack, comp_cards)
      input("Its the computer's turn now! >>> ")
      comp_card = cards.comp_play_card(comp_cards, current_card, current_suite, attack_value > 0)

      if comp_card != None and comp_card != 1:
        pile.append(comp_card)
        input(f"The computer has played the {comp_card} >>> ")
        current_card = pile[-1]
        current_suite = current_card.suite
        is_player_turn = False if current_card.value == 7 or current_card.value == 11 else True
        if current_card.value == 8:
          current_suite = cards.comp_change_suite()
        elif current_card.value in [0, 2]:
          attack_value += current_card.power_value
      elif comp_card == 1:
        input(f"The computer will take {attack_value} cards >>> ")
        attack_value = 0
        is_player_turn = True
      else:
        new_comp_card = stack.pop()
        comp_cards.append(new_comp_card)
        input(f"The computer has taken the {new_comp_card} >>> ")
        is_player_turn = True

      cards.print_status(pile, stack, comp_cards)
    # Update
    cards.print_game_board(len(player_cards), len(comp_cards), current_card)

  input("GAME OVER\nThank your for playing >>> ")

main()

  
    
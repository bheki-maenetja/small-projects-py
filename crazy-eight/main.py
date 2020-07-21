from random import shuffle, choice

from cards import * 
import util

# THE MAIN FUNCTION
def main():
  main_deck = get_card_deck()
  shuffled_deck = main_deck[:]
  shuffle(shuffled_deck)
  player_cards, comp_cards, stack, pile = assign_cards(shuffled_deck)

  current_card = pile[-1]
  current_suite = pile[-1].suite
  is_player_turn = True
  player_choice = ''
  attack_value = 0
  
  print_game_board(len(player_cards), len(comp_cards), current_card)

  while not is_game_over(player_cards, comp_cards, current_card):
    # Process Input (events)
    while is_player_turn:
      if player_choice == 'c':
        view_cards(player_cards, 'Your cards')
        player_choice = util.get_string(1,1, 'Press b to go back or p to play a card', accept_values=['b', 'p'])
      elif player_choice == 'p':
        player_card = play_card(player_cards, current_card, current_suite, attack_value > 0)
        if player_card != None and player_card != 1:
          input(f"You have played the {player_card} >>> ")
          pile.append(player_card)
          current_card = pile[-1]
          current_suite = current_card.suite
          is_player_turn = True if current_card.value == 7 or current_card.value == 11 else False
          if current_card.value == 8:
            current_suite = change_suite()
          elif current_card.value in [0, 2]:
            attack_value += current_card.power_value
        elif player_card == 1:
          input(f"The player will take {attack_value} cards >>> ")
          take_cards(attack_value, player_cards, stack)
          check_stack(stack, pile)
          attack_value = 0
          is_player_turn = False
        player_choice = ''
      elif player_choice == 't':
        take_cards(1, player_cards, stack)
        check_stack(stack, pile)
        input(f"You have taken the {player_cards[-1]} >>> ")
        is_player_turn = False
        player_choice = ''
      else:
        player_choice = util.get_string(1, 1, "Press t to take a card, c to view your your deck or p to play a card", ['c', 'p', 't']) if attack_value == 0 else 'p'
    else:
      if not is_game_over(player_cards, comp_cards, current_card):
        print_status(pile, stack, comp_cards)
        input("Its the computer's turn now! >>> ")
        comp_card = comp_play_card(comp_cards, current_card, current_suite, attack_value > 0)

        if comp_card != None and comp_card != 1:
          pile.append(comp_card)
          input(f"The computer has played the {comp_card} >>> ")
          current_card = pile[-1]
          current_suite = current_card.suite
          is_player_turn = False if current_card.value == 7 or current_card.value == 11 else True
          if current_card.value == 8:
            current_suite = comp_change_suite(comp_cards)
          elif current_card.value in [0, 2]:
            attack_value += current_card.power_value
        elif comp_card == 1:
          input(f"The computer will take {attack_value} cards >>> ")
          take_cards(attack_value, comp_cards, stack)
          check_stack(stack, pile)
          attack_value = 0
          is_player_turn = True
        else:
          take_cards(1, comp_cards, stack)
          check_stack(stack, pile)
          input(f"The computer has taken the {comp_cards[-1]} >>> ")
          is_player_turn = True

      print_status(pile, stack, comp_cards)
    # Update
    print_game_board(len(player_cards), len(comp_cards), current_card)

  input("GAME OVER\nThank your for playing >>> ")

main()

  
    
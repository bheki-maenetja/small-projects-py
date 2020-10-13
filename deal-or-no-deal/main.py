import v1.deal as version1
import v2.deal_v2 as version2
import v3.deal_v3 as version3
from util.util_functions import get_integer

def game_handler():
  input("Welcome to Deal or No Deal >>> ")
  print("1. Version 1 (Original)", "2. Version 2 (Bonus Features)", "3. Version 3 (NEW STUFF)", sep="\n")
  
  version_choice = get_integer("To choose a version enter it's corresponding number", max_value=3, min_value=1, break_value='q')
  if version_choice == 1:
    version1.playGame()
  elif version_choice == 2:
    version2.start_game()
  elif version_choice == 3:
    version3.play_game()

if __name__ == "__main__":
    game_handler()
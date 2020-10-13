import v1.deal as version1
import v2.deal_v2 as version2
import v3.deal_v3 as version3
from util.util_functions import get_integer

def game_handler():
  print("Choose the version of the game you want to play\n")
  print("1) Deal or No Deal (Original)", "2) Deal or No Deal 2 (Bonus Features)", "3) All New Deal or No Deal (NEW STUFF)", sep="\n")

  version_choice = get_integer("\nTo choose a version enter it's corresponding number", max_value=3, min_value=1, break_value='q')
  if version_choice == 1:
    version1.playGame()
  elif version_choice == 2:
    version2.start_game()
  elif version_choice == 3:
    version3.play_game()

if __name__ == "__main__":
    game_handler()
import v1.deal as version1
import v2.deal_v2 as version2

def game_handler():
  input("Welcome to Deal or No Deal >>> ")
  input("You have chosen version 2 >>> ")
  version2.start_game()

if __name__ == "__main__":
    game_handler()
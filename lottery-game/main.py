import v1.lottery as lotto1
# import v2.lottery_v2 as lotto2
# import v3.lottery_v3 as lotto3
# import v4.lottery_v4 as lotto4
import v5.lottery_v5 as lotto5

def game_handler():
  print("Choose the version of the game you want to play\n")
  print("1) Lottery (Original)", "2) Lottery 2", "3) Lottery 3 (More game levels)", "4) All New Lotto", "5) Lotto Legacy (The best one yet)", sep="\n")
  lotto1.export_function()

if __name__ == "__main__":
    game_handler()
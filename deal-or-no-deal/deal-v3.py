from random import sample

def start_game():
    input("Twenty boxes, a quarter of a million pounds. Welcome to Deal or No Deal!!! >>> ")
    money_table = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 50.0, 100.0, 250.0, 500.0, 750.0, 1000, 3000, 5000, 10000, 15000, 20000, 35000, 50000, 75000, 100000, 250000]
    money_board = {i:money_table[i-1] for i in sample(range(1, 23), 22)}

start_game()

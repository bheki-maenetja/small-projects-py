from random import sample

def play_lotto():
    input("WELCOME TO THE LOTTERY!!! >>> ")
    total_winnings = 0
    while True:
        try:
            num_rounds = int(input("How many rounds would you like to play? Choose between 1 and 10: "))
            if num_rounds not in range(1,11): raise ValueError
        except ValueError:
            print("Please enter a valid number!")
        else:
            break
    for i in range(0, num_rounds):
        input(f"ROUND {i+1} >>> ")
        total_winnings += get_winnings()
    input(f"Congratulations!!! You've won a total of ${total_winnings}!!!\nThank you for playing the lottery!!! >>> ")

def get_winnings():
    game_settings = {1: ['10-ball', 10], 2: ['20-ball', 20], 3: ['50-ball', 50], 4: ['100-ball', 100], 5: ['1000-ball', 1000]}
    for i in game_settings:
        print(f"{i}: {game_settings[i][0]}")
    while True:
        try:
            setting_choice = int(input("Select your game mode: "))
            if setting_choice not in range(1,6): raise ValueError
        except ValueError:
            print("Please enter a number between 1 and 5")
        else:
            break
    user_settings = tuple(game_settings[setting_choice])
    input(f"You have selected {user_settings[0]}!\nRight then, let's crack on with your game!!! >>> ")
    draw, ticket = ticket_and_draw(user_settings)
    print(f"The draw: {draw}\nThe ticket: {ticket}")
    cash_prize, winning_balls, num_hits = calculate_winnings(user_settings, draw, ticket)
    input(f"Congratulations! You've won ${cash_prize}!!! >>> ")
    input(f"You got {num_hits} correct number(s): {winning_balls} >>> ")
    return cash_prize

def ticket_and_draw(user_settings):
    draw = sample(range(1, user_settings[1]), 6)
    input("Time to enter your lotto numbers >>> ")
    ticket = []
    while len(ticket) != 6:
        try:
            lotto_ball = int(input(f"Enter a number between 1 and {user_settings[1]}: "))
            if lotto_ball not in range(1, user_settings[1] + 1) or lotto_ball in ticket: raise ValueError
            ticket.append(lotto_ball)
        except ValueError:
            print("Please enter a valid number")
    return draw, ticket

def calculate_winnings(user_settings, draw, ticket):
    prize_money = [0, 10, 20, 50, 100, 1000]
    winning_balls = [i for i in draw for j in ticket if i == j]
    num_hits = len(winning_balls)
    winnings = prize_money[num_hits] * user_settings[1]
    return winnings, winning_balls, num_hits

if __name__ == "__main__":
    play_lotto()
else:
    def export_function():
      play_lotto()

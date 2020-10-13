import random

def play_lotto():
    """
    Purpose: Main function of the program
    """
    input("Welcome to the Lottery!!! >>> ")
    total_winnings = 0
    print("1: 20-ball\n2: 50-ball\n3: 100-ball\n4: 200-ball\n5: 500-ball\n6: 1000-ball")
    setting_choice = input("Select the type of lotto game you want to play\nEnter the corresponding number: ")
    while True:
        if (not setting_choice.isnumeric()) or (int(setting_choice) not in range(1, 7)):
            setting_choice = input("Please enter a valid input: ")
        else:
            setting_choice = int(setting_choice)
            break
    num_rounds = input("How many rounds would you like to play?\nSelect between 1 and 10: ")
    while True:
        if (not num_rounds.isnumeric()) or (int(num_rounds) not in range(1, 11)):
            num_rounds = input("Invalid input, please enter any number from 1 to 10: ")
        else:
            num_rounds = int(num_rounds)
            break
    for i in range(num_rounds):
        input(f"Round {i+1}, here we go! >>> ")
        ticket_and_draw = get_ticket_and_draw(setting_choice)
        round_winnings, num_hits = calculate_winnings(ticket_and_draw)
        total_winnings += round_winnings
        input(f"Here was the draw: {ticket_and_draw['draw']}\nHere is your ticket: {ticket_and_draw['ticket']} >>> ")
        input(f"You got {num_hits} ball(s) correct!\nYou've won ${round_winnings} in this round. Well done! >>> ")
    input(f"You've won a total of ${total_winnings}! Well done! >>> ")
    input("Thank you for playing the Lottery!!! >>> ")

def get_ticket_and_draw(setting_choice):
    """
    Purpose: Creates a list of random numbers from a set range and takes in the users lotto numbers

    Parameters:
        setting_choice --> Specifies the range of numbers the user can select from and the range from which the draw is made

    Return Values:
        The function returns a dictionary containing the user's chosen number (ticket), the list of numbers selected randomly and the range from which these two sets of numbers could be selected
    """
    input("Right, it's time to enter your lotto numbers! >>> ")
    game_settings = dict([(1, 20), (2, 50), (3, 100), (4, 200), (5, 500), (6, 1000)])
    draw_range = game_settings[setting_choice]
    lotto_draw = []
    lotto_ticket = []
    while len(lotto_draw) != 7:
        ball = random.randrange(1, draw_range + 1)
        if ball not in lotto_draw: lotto_draw.append(ball)
    while len(lotto_ticket) != 7:
        lotto_num = input(f"Enter any number from 1 to {draw_range}: ")
        while True:
            if (not lotto_num.isnumeric()) or (int(lotto_num) not in range(1, draw_range + 1)) or (int(lotto_num) in lotto_ticket):
                lotto_num = input(f"Invalid input, please enter any number from 1 to {draw_range}: ")
            else:
                lotto_num = int(lotto_num)
                lotto_ticket.append(lotto_num)
                break
    input("All done! Let's see how you did! >>> ")
    return {"ticket": lotto_ticket, "draw": lotto_draw, "range": draw_range}

def calculate_winnings(ticket_and_draw):
    """
    Purpose: Calculate the prize money that the user is to receive in 1 round of lotto

    Parameters:
        ticket_and_draw --> A dictionary storing the lotto ticket, lotto draw and draw range

    Return Values:
        cash_prize --> The users winnings
        num_hits --> The number of correct mathches between the user's ticket and the lottery draw
    """
    money_table = [0, 10, 50, 100, 250, 500, 750, 1000]
    ticket, draw, draw_range = ticket_and_draw["ticket"], ticket_and_draw["draw"], ticket_and_draw["range"]
    num_hits = len([i for i in ticket for j in draw if i == j])
    cash_prize = money_table[num_hits] * draw_range
    return cash_prize, num_hits

if __name__ == "__main__":
    play_lotto()
else:
    def export_function():
      play_lotto()

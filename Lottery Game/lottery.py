import random

def create_lists(ticket, draw, draw_range):
    while len(ticket) < 6:
        my_ball = int(input("Please enter any number from 0 to " + str(draw_range) + ": "))
        ticket.append(my_ball)
        ball = random.randint(0, draw_range)
        if ball not in draw:
            draw.append(ball)
        else:
            ball = random.randint(0, draw_range)
            if ball not in draw:
                draw.append(ball)
            else:
                ball = random.randint(0, draw_range)
                if ball not in draw:
                    draw.append(ball)
                else:
                    ball = random.randint(0, draw_range)
                    if ball not in draw:
                        draw.append(ball)
                    else:
                        ball = random.randint(0, draw_range)
                        if ball not in draw:
                            draw.append(ball)
                        else:
                            print("what do we do now?")


def lotto_checker(ticket, draw, winnings):
    hit_list = []
    x = 0
    while x < 6:
        if ticket[x] in draw and hit_list.count(ticket[x]) == 0:
            hit_list.append(ticket[x])
            x += 1
        else:
            x += 1

    num_balls = len(hit_list)

    if num_balls/6 == 6/6:
        print("You just won the jackot baby! $1 000 000!")
        print("These were the drawn lotto numbers: " + str(draw))
        winnings.append(1000000)
    elif num_balls/6 == 5/6:
        print("Fan-frickin-tastic! You just won $500 000!")
        print("These were the drawn lotto numbers: " + str(draw))
        winnings.append(500000)
    elif num_balls/6 == 4/6:
        print("Amazing! You walk away with $125 000!")
        print("These were the drawn lotto numbers: " + str(draw))
        winnings.append(125000)
    elif num_balls/6 == 3/6:
        print("Great job! You're gonna get $15 625!")
        print("These were the drawn lotto numbers: " + str(draw))
        winnings.append(15625)
    elif num_balls/6 == 2/6:
        print("Good job! You won $3125.")
        print("These were the drawn lotto numbers: " + str(draw))
        winnings.append(3125)
    elif num_balls/6 == 1/6:
        print("Well done! You get $625")
        print("These were the drawn lotto numbers: " + str(draw))
        winnings.append(625)
    else:
        print("Boo hoo! You're a loser! Now go home!")
        print("These were the drawn lotto numbers: " + str(draw))

my_ticket = []
the_draw = []
wallet = []

def play_lottery(user_nums, powerballs, money):
    rounds = int(input("How many rounds would you like to play? "))
    user_range = int(input("Enter any number from 10 or above to set the range "))
    counter = 0
    total = 0
    x = 0
    if user_range < 10:
        user_range = 10
        print("Range too low. Range has been automatically set to 10.")
    while counter < rounds:
        create_lists(user_nums, powerballs, user_range)
        lotto_checker(user_nums, powerballs, money)
        user_nums.clear()
        powerballs.clear()
        counter += 1
    while x < len(money):
        total += money[x]
        x += 1
    print("Congratulations! You won a total of $" + str(total)+ "!")

play_lottery(my_ticket, the_draw, wallet)

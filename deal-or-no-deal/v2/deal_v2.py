from random import choice, randrange

def start_game():
    """
    Initialise's the game.
    """
    input("Twenty-two boxes, a quarter of a million pounds, just one question.\nWelcome to Deal or No Deal!!! >>> ")
    money_table = [0.01, 0.1, 0.5, 1.0, 5, 10, 50, 100, 250, 500, 750, 1000, 3000, 5000, 10000, 15000, 20000, 35000, 50000, 75000, 100000, 250000]
    game_board = [(i, money_table.pop(randrange(len(money_table)))) for i in range(1, 23)]
    display_board(game_board)
    while True:
        try:
            box_num = int(input("Enter the number of the box you want to choose: "))
            user_box = game_board[box_num - 1]
        except:
            print("Please enter a valid input")
        else:
            break
    input(f"You have chosen box {user_box[0]} >>> ")
    play_game(game_board, user_box)

def play_game(money_boxes, chosen_box):
    """
    Asks the user to eliminate boxes from their game until a deal is made or only 2 boxes remain.
    """
    input("Right then! Let's crack on with your game!!! >>> ")
    key_boxes = [17, 14, 11, 8, 5, 2]
    offer_button = choice([True, False])
    while len(money_boxes) > 0:
        if len(money_boxes) in key_boxes:
            input("Press enter to continue >>> ")
            display_board(money_boxes, chosen_box)
            cash_offer = make_offer(money_boxes)
            print(f"We are now at {len(money_boxes)}-box.")
            input(f"Your offer is £{cash_offer} >>> ")
            deal = check_decision(cash_offer)
            if deal == True:
                input(f"You've decided to deal at £{cash_offer} >>> ")
                complete_game(money_boxes, deal, cash_offer, chosen_box)
                return
            elif deal == False and len(money_boxes) == 2:
                complete_game(money_boxes, deal, cash_offer, chosen_box)
                return
            elif deal == False and len(money_boxes) == 17:
                input("No deal! Onwards we go! >>> ")
                input("But before you move on you should know that you've been given the offer button.\nThis will allow you to demand the banker to make you an offer at any point in the game, but you can only use this once.\nTo use the offer button press 'X' >>> ") if offer_button == True else None
            else:
                input("No deal! Onwards we go! >>> ")
            key_boxes.remove(len(money_boxes))
        else:
            box_choice = input("Choose the box that you want to eliminate: ")
            while True:
                if box_choice.lower() == "x" and len(money_boxes) < 17 and offer_button == True:
                    offer_button = False
                    input("You've triggered the offer button! >>> ")
                    cash_offer = make_offer(money_boxes)
                    input(f"Your offer is £{cash_offer} >>> ")
                    deal = check_decision(cash_offer)
                    if deal == True:
                        input(f"You've decided to deal at £{cash_offer} >>> ")
                        complete_game(money_boxes, deal, cash_offer, chosen_box)
                        return
                    else:
                        input("No deal! Onwards we go! >>> ")
                        break
                elif (not box_choice.isnumeric()) or (int(box_choice) == chosen_box[0]) or (int(box_choice) not in [i[0] for i in money_boxes]):
                    box_choice = input("Please enter a valid input: ")
                else:
                    box_choice = int(box_choice)
                    break
            if not str(box_choice).isnumeric(): continue
            box_choice = [i for i in money_boxes if i[0] == box_choice][0]
            print(f"You've lost £{box_choice[1]}")
            money_boxes.remove(box_choice)

def complete_game(money_boxes, deal_decision, money_offer, chosen_box):
    """
    Completes the user's game by opening all of the remaining boxes after a deal is made.
    """
    input("Right then, it's time to complete your game >>> ")
    key_boxes = [17, 14, 11, 8, 5]
    if len(money_boxes) in key_boxes: key_boxes.remove(len(money_boxes))
    while True:
        if deal_decision == True and len(money_boxes) == 2:
            input("Press enter to continue >>> ")
            display_board(money_boxes, chosen_box)
            cash_offer = make_offer(money_boxes)
            print("We are now at 2-box.")
            input(f"Your offer at this point would've been £{cash_offer} >>> ")
            input("Right then, let's see what you would've won! >>> ")
            print(f"If you went all the way you would have won £{chosen_box[1]}")
            winnings = money_offer
            break
        elif deal_decision == False and len(money_boxes) == 2:
            input("Right, it's crunch time! >>> ")
            swap = choice([True, False])
            swap_decision = input("The banker has offered you the swap\nPress 1 to swap your box else press 2: ") if swap == True else None
            while True:
                if swap_decision == "1":
                    box_choice = [i for i in money_boxes if i[0] != chosen_box[0]][0]
                    input(f"You've decided to swap!\nYour box is now Box {box_choice[0]} >>> ")
                    break
                elif swap_decision == "2":
                    input(f"You've decided not to swap!\nYour box is still {chosen_box[0]} >>> ")
                    break
                elif (swap_decision != None) and (swap_decision not in ["1", "2"]):
                    swap_decision = input("Please enter a valid input: ")
                else:
                    break
            input("Right then, let's see what you've won! >>> ")
            print(f"You have won £{box_choice[1]}, congratulations!") if swap_decision == "1" else print(f"You have won £{chosen_box[1]}, congratulations!")
            winnings = box_choice[1] if swap_decision == "1" else chosen_box[1]
            break
        elif deal_decision == True and len(money_boxes) in key_boxes:
            input("Press enter to continue >>> ")
            display_board(money_boxes, chosen_box)
            cash_offer = make_offer(money_boxes)
            print(f"We are now at {len(money_boxes)}-box.")
            input(f"Your offer at this point would've been £{cash_offer} >>> ")
            key_boxes.remove(len(money_boxes))
        else:
            box_choice = input("Choose the box that you would've eliminated: ")
            while True:
                if (not box_choice.isnumeric()) or (int(box_choice) == chosen_box[0]) or (int(box_choice) not in [i[0] for i in money_boxes]):
                    box_choice = input("Please enter a valid input: ")
                else:
                    box_choice = int(box_choice)
                    break
            box_choice = [i for i in money_boxes if i[0] == box_choice][0]
            print(f"You would've lost £{box_choice[1]}")
            money_boxes.remove(box_choice)
    input("Press enter to continue >>> ")
    box_23(winnings)
    return

def box_23(cash_prize):
    """
    Gives the user the option to purchase box 23 and increase or decrease their winnings.
    """
    box_choice = choice([2, 0.5, 10000, 0])
    input(f"So you've won £{cash_prize}\nBut how would you like to purchase Box 23? >>> ")
    input("With Box 23 you stand the chance to do one of the following >>> ")
    input("1) Double your winnings\n2) Half your winnings\n3) Get an extra £10000\n4) Lose all your money and leave with nothing\nPress enter to continue >>> ")
    decision = input("So Box 23, deal or no deal?\nPress 1 to deal else press 2: ")
    while True:
        if (not decision.isnumeric()) or (int(decision) not in [1, 2]):
            decision = input("Please enter a valid input: ")
        else:
            break
    input("You've purchased Box 23, let's see what's inside! >>> ") if decision == "1" else input("So you're not buying Box 23, suit yourself >>")
    if decision == "1" and (box_choice == 2 or box_choice == 0.5):
        input(f"Wow! You've doubled your money!\nNow you've just won £{2*cash_prize}, congratulations! >>> ") if box_choice == 2 else input(f"Oh no! You've halved your money\nNow you're only walking away with £{0.5*cash_prize}, congratulations? >>> ")
        input("Thank you for playing Deal or No Deal! >>> ")
        return
    elif decision == "1" and (box_choice == 10000 or box_choice == 0):
        input(f"Wow! You've won an extra £10 000!\nNow you're walking away with £{cash_prize + 10000}, congratulations! >>> ") if box_choice == 10000 else input("OH NOOO! You've lost all your money! You walk away with nothing! >>> ")
        input("Thank you for playing Deal or No Deal! >>> ")
        return
    else:
        input(f"Well, it's official, you've won £{cash_prize}, congratulations!\nThank you for playing Deal or No Deal! >>> ")

def check_decision(money_offer):
    """
    Checks whether or not the user wants to deal at the offered amount.
    """
    decision = input(f"£{money_offer}, deal or no deal?\nPress 1 to deal, else press 2: ")
    while True:
        if (not decision.isnumeric()) or (int(decision) not in [1, 2]):
            decision = input("Please enter a valid number: ")
        else:
            decision = int(decision)
            break
    return True if decision == 1 else False

def make_offer(money_boxes):
    """
    Returns a cash value to be offered to the user, that is calculated from the remaining cash prizes.
    """
    average = 0
    for i, j in money_boxes:
        average += j
    average /= len(money_boxes)
    game_round = ((len(money_boxes) - 17)/-3) + 1
    offer = average * game_round/10
    offer = int(round(offer, -2)) if offer >= 100 else round(offer, 2)
    return offer

def display_board(money_boxes, chosen_box=(0, 0)):
    """
    Displays the remaining boxes and cash prizes.
    """
    blue_money = [i[1] for i in money_boxes if i[1] < 1000]
    red_money = [i[1] for i in money_boxes if i[1] >= 1000]
    blue_money.sort()
    red_money.sort()
    remaining_boxes = [i[0] for i in money_boxes if i[0] != chosen_box[0]]
    print("\nMONEY BOXES\n")
    for i in range(0, (len(remaining_boxes) // 2) * 2, 2): print(f"Box {remaining_boxes[i]}\t\tBox {remaining_boxes[i + 1]}")
    print(f"Box {remaining_boxes[-1]}") if len(remaining_boxes) % 2 != 0 else print()
    print("\nCASH PRIZES\n")
    print("Blue Money:")
    for i in blue_money: print(f"£{i}", end=" ")
    print("\n\nRed Money:")
    for i in red_money: print(f"£{i}", end=" ")
    input("\n\nHere is the board as it stands. Press enter to continue >>> ")


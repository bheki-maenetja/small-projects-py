import random

def ticket_and_draw(diff_setting): #Get's user's numbers and creates draw
    ranges = [10, 100, 1000]
    draw_range = ranges[diff_setting]
    user_ticket = []
    lotto_draw = []
    while len(user_ticket) < 6:
    	user_num = int(input(f"Enter any number from 0 to {draw_range}: "))
    	while 0 <= user_num <= draw_range and user_num not in user_ticket:
    		user_ticket.append(user_num)
    		break
    	else:
    		print("Either you've already entered that number or it's out of range. Try again")
    while len(lotto_draw) < 6:
    	lotto_ball = random.randint(0, draw_range)
    	while lotto_ball not in lotto_draw:
    		lotto_draw.append(lotto_ball)
    return user_ticket, lotto_draw

def get_money(ticket, draw):
	hit_list = []
	money_table = {
	6: [1000000, "You just won the jackpot baby! $1 000 0000!"],
	5: [500000, "Fan-frickin-tastic! You just won $500 000!"],
	4: [125000, "Amazing! You walk away with $125 000!"],
	3: [15625, "Great job! You're gonna get $15 625!"],
	2: [3125, "Good job! You won $3125!"],
	1: [625, "You won $625!"],
	0: [0, "Boo hoo! You're a loser! Now go home!"],
	}
	for i in ticket:
		if i in draw:
			hit_list.append(i)
	money = money_table[len(hit_list)]
	print(f"These were the numbers drawn: {draw}")
	return money

def play_lotto():
	print("1: Easy (1 - 10)\n2: Medium (1 - 100) \n3: Hard (1 - 1000)")
	diff = int(input("Enter 1, 2 or 3 to set the difficulty level: "))
	num_rounds = int(input("How many rounds would you like to play: "))
	count = 0
	winnings = 0
	while count < num_rounds:
		player_ticket, player_draw = ticket_and_draw(diff - 1)
		cash = get_money(player_ticket, player_draw)
		winnings += cash[0]
		print(cash[1])
		count += 1
	print(f"Congratulations, you've won a grand total of ${winnings}. Well done!")

if __name__ == "__main__":
    play_lotto()
else:
    def export_function():
      play_lotto()

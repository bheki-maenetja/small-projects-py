import random

def makeOffer(moneyBoxes):
	blueMoney = []
	redMoney = []
	for i in range(1, 23):
		if i in moneyBoxes and moneyBoxes[i] <= 750:
			blueMoney.append(moneyBoxes[i])
		elif i in moneyBoxes:
			redMoney.append(moneyBoxes[i])
	if len(redMoney) != 0:
		start = 0
		for i in redMoney:
			start += i
		redAverage = start/len(redMoney)
		offer = round(0.6*redAverage*(1.11-len(blueMoney)/10), -2)
		return offer
	else:
		start = 0
		for i in blueMoney:
			start += i
		offer = round(0.4*start/len(blueMoney), 2)
		return offer

def displayBoard(moneyBoxes, chosenBox):
	input("Press enter to continue ")
	boxes = []
	blueMoney = []
	redMoney = []
	for i in range(1, 23):
		if i in moneyBoxes and moneyBoxes[i] <= 750:
			boxes.append(i)
			blueMoney.append(moneyBoxes[i])
		elif i in moneyBoxes:
			boxes.append(i)
			redMoney.append(moneyBoxes[i])
	boxes.remove(chosenBox)
	boxes.sort()
	blueMoney.sort()
	redMoney.sort()
	for item in [boxes, blueMoney, redMoney]:
		if item == boxes:
			boxWord = ""
			for i in range(0, len(boxes)):
				boxWord += "Box " + str(boxes[i]) + ", "
		elif item == blueMoney:
			blueWord = ""
			for i in range(0, len(blueMoney)):
				blueWord += "$" + str(blueMoney[i]) + ", "
		else:
			redWord = ""
			for i in range(0, len(redMoney)):
				redWord += "$" + str(redMoney[i]) + ", "
	print("This is the state of your game:\n")
	print(f"Here are the remaining boxes:\n{boxWord}\n")
	print(f"Here are the remaining cash prizes:\n\nBlue Money:\n{blueWord}\n\nRed Money:\n{redWord}\n")

def playGame():
	print("Twenty two boxes. A quarter of a million dollars. Just one question. Welcome to Deal or No Deal!!!")
	input("Press enter to continue ")
	moneyTable = [0.01, 0.1, 0.5, 1, 5, 10, 50, 100, 250, 500, 750, 1000, 3000, 5000, 10000, 15000, 20000, 35000, 50000, 75000, 100000, 250000]
	gameBoxes = dict.fromkeys(range(1, 23))									
	for i in gameBoxes:														
		if gameBoxes[i] == None:
			randIndex = random.randrange(0, len(moneyTable))
			gameBoxes[i] = moneyTable.pop(randIndex)
	userBox = int(input("Choose one of the boxes numbered from 1 to 22: "))
	validBox = False
	while validBox == False:
		while userBox not in range(1, 23):
			userBox = int(input("Can't choose that box, try again: "))
		else:
			validBox = True
	print(f"You have chosen box {userBox}.")
	displayBoard(gameBoxes, userBox)    
	key_rounds = [17, 14, 11, 8, 5, 2]
	while len(gameBoxes) >= 2:
		if len(gameBoxes) in key_rounds:
			displayBoard(gameBoxes, userBox)
			offer = makeOffer(gameBoxes)
			print(f"We have now reached {len(gameBoxes)}-box. Your offer is ${offer}")
			input("Press enter to continue ")
			decision = 1 if int(input(f"${offer}. Deal, or no deal? Press 1 if you want to deal, else press 2. ")) == 1 else 2
			if len(gameBoxes) >= 2 and decision == 1:
				print(f"You've decided to deal at ${offer}\nRight, let's complete your game!")
				completeGame(offer, gameBoxes, userBox)
				return
			elif len(gameBoxes) == 2 and decision == 2:
				print(f"No deal! It's crunch time now!")
				input("Press enter to continue ")
				completeGame(None, gameBoxes, userBox)
				return
			elif len(gameBoxes) > 2 and decision == 2:
				print("No deal! Let's play on.")
			key_rounds.remove(len(gameBoxes))
		else:
			choice = int(input("Choose your next box: "))
			validChoice = False
			while validChoice == False:
				while choice == userBox or choice not in gameBoxes:
					choice = int(input("You can't select that box, try again: "))
				else:
					validChoice = True
			print(f"You've lost ${gameBoxes.pop(choice)}\n")

def completeGame(dealMoney, moneyBoxes, chosenBox):
	key_rounds = [17, 14, 11, 8, 5]
	dealAt = len(moneyBoxes)
	while len(moneyBoxes) >= 2:
		if len(moneyBoxes) in key_rounds and len(moneyBoxes) != dealAt:
			displayBoard(moneyBoxes, chosenBox)
			offer = makeOffer(moneyBoxes)
			print(f"If you went to {len(moneyBoxes)}-box, your offer would have been ${offer}")
			key_rounds.remove(len(moneyBoxes))
		elif len(moneyBoxes) == 2 and dealMoney == None:
			swap = 1 if random.randrange(0, 2) == 1 else 0
			if swap == 1:
				swapDecision = int(input("The banker has offered your the swap. (1) Swap or (2) no swap? "))
				if swapDecision == 1:
					print("You've taken the swap! How brave!")
					for i in moneyBoxes:
						if i != chosenBox:
							newBox = i
					print(f"Your box is now Box {newBox}")
					input("Press enter to continue ")
				elif swapDecision == 2:
					print("You're sticking with your box. Best of your luck!")
				print("Right, time to open it up!")
				input("Press enter to continue ")
				print(f"You have won ${moneyBoxes[chosenBox]}! Congratulations!\nThank you for playing Deal or No Deal. Bye bye!!!")
				return
			elif swap == 0:
				print("Right, time to open up your box! Best of luck!")
				input("Press enter to continue ")
				print(f"You have won ${moneyBoxes[chosenBox]}! Congratulations!\nThank you for playing Deal or No Deal. Bye bye!!!")
				return
		elif len(moneyBoxes) == 2 and dealMoney != None and dealAt > 2:
			displayBoard(moneyBoxes, chosenBox)
			offer = makeOffer(moneyBoxes)
			print(f"If you went to {len(moneyBoxes)}-box, your offer would have been ${offer}")
			input("Press enter to continue ")
			print("Anyway, let's see what you would've won!")
			input("Press enter to continue ")
			print(f"If you went all the way, you would've opened your box to find ${moneyBoxes[chosenBox]}\nBut instead you dealt at ${dealMoney}\nThank you for playing Deal or No Deal. Bye bye!!!")
			return
		elif dealAt == 2:
			input("Press enter to continue ")
			print(f"So you've dealt at {dealMoney}\nAnyway let's see what you would've won!")
			input("Press enter to continue ")
			print(f"If you went all the way, you would've opened your box to find ${moneyBoxes[chosenBox]}\nBut instead you dealt at ${dealMoney}\nThank you for playing Deal or No Deal. Bye bye!!!")
			return
		else:
			choice = int(input("Choose what would've been your next box: "))
			validChoice = False
			while validChoice == False:
				while choice == chosenBox or choice not in moneyBoxes:
					choice = int(input("You couldn't have selected that box, try again: "))
				else:
					validChoice = True
			print(f"You would've lost ${moneyBoxes.pop(choice)}\n")

playGame()


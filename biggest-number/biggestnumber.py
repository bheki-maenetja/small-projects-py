numTotal = int(input("How many numbers would you like to enter: "))
bigNum = float(input("Enter your first number: "))
for i in range(0, numTotal - 1):
    newNum = float(input("Enter another number "))
    if newNum > bigNum:
        bigNum = newNum

print("The biggest number is " + str(bigNum))
    
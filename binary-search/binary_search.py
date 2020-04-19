from random import randint

my_list = sorted([randint(0, 100) for i in range(11)])

searchItem = int(input(f"Here is your list: {my_list}\nEnter any number in the list to find it's position: "))

found = False
searchFailed = False
first = 0
last = len(my_list) - 1
while (not found) and (not searchFailed):
    middle = (first + last) // 2
    if my_list[middle] == searchItem:
        found = True
    elif first >= last:
        searchFailed = True
    elif my_list[middle] > searchItem:
        last = middle - 1
    else:
        first = middle + 1

if found == True:
    print(f"Position: {middle}")
else:
    print("Item not present in array")

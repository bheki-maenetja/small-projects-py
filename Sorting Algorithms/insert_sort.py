from random import randint

my_list = [randint(0, 100) for i in range(10)]
input(f"Here is your list: {my_list}\nPress enter to have it sorted >>> ")

num_items = len(my_list)
for pointer in range(1, num_items):
    ItemToBeInserted = my_list[pointer]
    CurrrentItem = pointer - 1
    while (my_list[CurrrentItem] > ItemToBeInserted) and (CurrrentItem > -1):
        my_list[CurrrentItem + 1] = my_list[CurrrentItem]
        CurrrentItem -= 1
    my_list[CurrrentItem + 1] = ItemToBeInserted

print(my_list)

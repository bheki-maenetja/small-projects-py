from random import randint

my_list = [i for i in range(1, 102)]

list_subsets = (my_list[i:i+7] for i in range(0, len(my_list), 7))

for i, subset in enumerate(list_subsets):
    print(i, subset)


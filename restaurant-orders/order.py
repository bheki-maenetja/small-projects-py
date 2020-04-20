import json

main_menu = []

the_bill = 0

my_order = []

prices = []

def get_menus(list_menus):
    file_name = input("Where would you like to eat today? ").lower()
    file = open(file_name + ".txt", "r")
    for line in file:
        format_line = json.loads(line)
        list_menus.append(format_line)



def get_price(total_bill, list_menus, choice, orders, price_list):
    food_bill = 0
    for dic in list_menus:
        if dic['name'] == choice:
            item_menu = dic
    item_list = list(item_menu.keys())
    item_list.remove('name')
    for item in item_list:
        num = orders.count(item)
        price = item_menu[item] * num
        food_bill += price
    total_bill = total_bill + food_bill
    price_list.append(total_bill)
    print(price_list)

def calculate(price_list, constant):
    for price in price_list:
        constant += price




def show_menu(list_menus, menu_name):
    for dic in list_menus:
        if dic["name"] == menu_name:
            key_holder = list(dic.keys())
            key_holder.remove("name")
            print("Here is the " + menu_name + " menu:")
            for key in key_holder:
                print(key + ": " + str(dic[key]))

                             
def place_order(list_menus, the_orders, menu_name):
    counter = 0
    for dic in list_menus:
        if dic["name"] == menu_name:
            key_holder = list(dic.keys())
            key_holder.remove("name")
    num_items = len(key_holder)
    while counter < num_items:
        order = input("What " + menu_name + " item would you like to order? (Press 'Q' to 'quit' when you're done.)").lower()
        if order == "q":
            break
        how_many = int(input("How many of those items would you like? "))
        
        while the_orders.count(order) < how_many:
            the_orders.append(order)
        counter += 1


def lets_eat(list_menus, total_bill, orders, price_list):
    get_menus(list_menus)
    
    choice_1 = input("Would you like to order drinks, food or desserts? Press 'Q' to quit when you're done. ").lower()
    if choice_1 == "q":
        for i in price_list:
            total_bill += i
        print("We're sorry you didn't buy anything. Come back another time!")
        return
    show_menu(list_menus, choice_1)
    place_order(list_menus, orders, choice_1)
    get_price(total_bill, list_menus, choice_1, orders, price_list)
    calculate(price_list, total_bill)
    
    choice_2 = input("Would you like to order drinks, food or desserts? Press 'Q' to quit when you're done. ").lower()
    if choice_2 == "q":
        for i in price_list:
            total_bill += i
        print("Thanks for wining and dining here! That will be " + "$" + str(total_bill)+ ".")
        return
    show_menu(list_menus, choice_2)
    place_order(list_menus, orders, choice_2)
    get_price(total_bill, list_menus, choice_2, orders, price_list)
    calculate(price_list, total_bill)
    
    choice_3 = input("Would you like to order drinks, food or desserts? Press 'Q' to quit when you're done. ").lower()
    if choice_3 == "q":
        for i in price_list:
            total_bill += i
        print("Thanks for wining and dining here! That will be " + "$" + str(total_bill)+ ".")
        return
    show_menu(list_menus, choice_3)
    place_order(list_menus, orders, choice_3)
    get_price(total_bill, list_menus, choice_3, orders, price_list)
    calculate(price_list, total_bill)
    
    for i in price_list:
        total_bill += i
    print("Thanks for wining and dining here! That will be " + "$" + str(total_bill) + ".")



















lets_eat(main_menu, the_bill, my_order, prices)


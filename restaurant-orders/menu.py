import json

menu_list = []

def create_menu(list_of_menus):
    menu = {}
    menu_counter = 0
    name = input("What would you like to call this menu? ")
    num_items = int(input("How many menu items would you like to create? "))
    menu["name"] = name
    while menu_counter < num_items:
        item = input("Enter the name of your menu item: ")
        item_price = float(input("Enter the price of this item: "))
        menu[item] = item_price
        menu_counter += 1
    list_of_menus.append(menu)
    
    
def list_menu(list_of_menus):
    list_counter = 0
    num_menus = int(input("How many menus would you like to create? "))
    while list_counter < num_menus:
        create_menu(list_of_menus)
        list_counter += 1
    print(list_of_menus)
        
def save_menu(list_of_menus):
     name = input("Save this set of menus as: ").lower()
     format_list = json.dumps(list_of_menus)
     new_file = open(name + ".txt" , "w")
     new_file.write(format_list)
            
    
list_menu(menu_list)
save_menu(menu_list)
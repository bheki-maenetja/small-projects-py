import json

def create_menus(files):
    menu = {}
    menu_counter = 0
    name_menu = input("What would you like to call this menu? ").lower()
    num_items = int(input("How many menu items would you like to create? "))
    menu["name"] = name_menu
    while menu_counter < num_items:
        item = input("Enter the name of your menu item: ").lower()
        item_price = float(input("Enter the price of this item: "))
        menu[item] = item_price
        menu_counter += 1
    format_menu = json.dumps(menu)
    files.write(format_menu + "\n")
    
    
    
def file_menus():
    list_counter = 0
    file_name = input("Save this set of menus as: ").lower()
    file = open(file_name + ".txt", "w")
    num_menus = int(input("How many menus would you like to create? "))
    while list_counter < num_menus:
        create_menus(file)
        list_counter += 1
        
file_menus()
    
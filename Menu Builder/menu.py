width = int(input("Enter the width: "))

price_width = 10
item_width = width - (len("Item") + len("Price"))

num_items = int(input("How many items would you like to enter: "))
item_list = []
for i in range (0, num_items):
	item = input("Enter the name of your item: ")
	price = float(input("Enter the price of your item: "))
	price_fmt = "{:.2f}".format(price)
	indent = width - (len(item) + len(str(price_fmt)))
	line = f"{item}{indent*' '}{price_fmt}"
	item_list.append(line)

print("="*width)
print(f"Item{item_width*' '}Price")
print("-"*width)

for i in item_list:
	print(i)

print("="*width)



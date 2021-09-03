# the key parameter can be used to sort complex objects


class Product():
    def __init__(self, name, price, weight, discount):
        self.name = name
        self.price = price
        self.weight = weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price, self.weight))

    def discountPrice(self):
        return self.price - (self.price * self.discount)


prodList = [
    Product("Widget", 50, 10, 0.05),
    Product("Doohickey", 40, 8, 0.15),
    Product("Thingamabob", 35, 12, 0.0),
    Product("Gadget", 65, 7, 0.20)
]

# use the key parameter to select a field to sort on


def prodsort(product):
    return product.price


print(sorted(prodList, key=prodsort))

# use the key parameter to select a field to sort on
print(sorted(prodList, key=lambda p: p.price))

# the key parameter can also call a method on the object
print(sorted(prodList, key=lambda p: p.discountPrice()))

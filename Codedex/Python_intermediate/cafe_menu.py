class CoffeeMenu:
    menu = {}

    def __init__(self):
        self.menu = {
            "espresso": 2.50,
            "latte": 2.75,
            "cappuccino": 3.20,
            "americano": 2.70,
        }

    def get_price(self, item):
        if item not in self.menu:
            return None
        return self.menu.get(item)
    
    def add_item(self, item, price):
        self.menu[item] = price
        return self.menu[item]
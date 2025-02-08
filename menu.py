class Menu:
    def __init__(self):
        self.items = {"pizza": [], "burger": [], "drinks": []}

    def add_menu_item(self, category, item):
        self.items.get(category, []).append(item)

    def show_menu(self):
        for category, items in self.items.items():
            print(f"\n{category.capitalize()}:")
            for index, item in enumerate(items, 1):
                print(f"{index}. {item.name} - ${item.price}")
 
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Burger(Food):
    def __init__(self, name, price, meat, ingredients):
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients


class Pizza(Food):
    def __init__(self, name, price, is_cold=False):
        super().__init__(name, price)
        self.is_cold = is_cold


class Drinks(Food):
    def __init__(self, name, price, is_hot=False):
        super().__init__(name, price)
        self.is_hot = is_hot

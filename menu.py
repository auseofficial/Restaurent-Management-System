class Menu:
    def __init__(self):
        self.menu = {"pizza": [], "burger": [], "drinks": []}

    def add_menu_item(self, category, item):
        if category in self.menu:
            self.menu[category].append(item)
        else:
            print(f"Category {category} does not exist in the menu!")

    def show_menu(self):
        print("Menu:")
        for category, items in self.menu.items():
            print(f"\n{category.capitalize()}:")
            for item in items:
                print(f" - {item.name} (${item.price})")

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cooking_time = 15

class Burger(Food):
    def __init__(self, name, price, meat, ingredients):
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

class Pizza(Food):
    def __init__(self, name, price, isCold=False):
        super().__init__(name, price)
        self.isCold = isCold

class Drinks(Food):
    def __init__(self, name, price, isHot=False):
        super().__init__(name, price)
        self.isHot = isHot

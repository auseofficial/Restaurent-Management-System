from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

class Customer(User):
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money
        self.__order = None

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order
        print(f"{self.name} placed an order")

    def eat_food(self, order):
        print(f"{self.name} ordered and ate {order.items}")

    def pay_for_order(self, amount):
        print(f"{self.name} paid ${amount}")

    def give_tips(self, tips_amount):
        print(f"{self.name} gave a tip of ${tips_amount}")

    def write_review(self, stars):
        print(f"{self.name} gave a review with {stars} stars")

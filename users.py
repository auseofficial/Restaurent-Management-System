from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def write_review(self, stars):
        pass

class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

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
        print(f"{self.name} placed an order: {order.items} costing ${order.price}")

    def eat_food(self):
        if self.__order:
            print(f"{self.name} is eating {self.__order.items}")
        else:
            print(f"{self.name} has no order to eat.")

    def pay_for_order(self):
        if self.__order and self.money >= self.__order.price:
            self.money -= self.__order.price
            print(f"{self.name} paid ${self.__order.price}. Remaining balance: ${self.money}")
        else:
            print(f"{self.name} does not have enough money to pay for the order.")

    def give_tips(self, tips_amount):
        print(f"{self.name} gave a tip of ${tips_amount}.")

    def write_review(self, stars):
        print(f"{self.name} gave a review with {stars} stars.")

# Example Usage
order1 = Order(items="Pizza", price=15)
customer1 = Customer(name="Alice", money=50)

customer1.order = order1  
customer1.eat_food()      
customer1.pay_for_order() 
customer1.give_tips(5)    
customer1.write_review(5) 
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address, money):
        super().__init__(name, phone, email, address)
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


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_date = starting_date

    def receive_salary(self):
        print(f"{self.name} received their salary of ${self.salary}")


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, cooking_item):
        super().__init__(name, phone, email, address, salary, starting_date)
        self.cooking_item = cooking_item


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super().__init__(name, phone, email, address, salary, starting_date)
        self.department = department


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, serving_area):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_date = starting_date
        self.serving_area = serving_area

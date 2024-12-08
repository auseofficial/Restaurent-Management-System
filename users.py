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

    def pay_for_order(self, amount):
        if amount <= self.money:
            self.money -= amount
            print(f"{self.name} paid ${amount}")
        else:
            print(f"{self.name} does not have enough money to pay ${amount}")


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_date = starting_date

    def receive_salary(self):
        print(f"{self.name} received their salary of ${self.salary}")


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, specialty):
        super().__init__(name, phone, email, address, salary, starting_date)
        self.specialty = specialty


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, serving_area):
        super().__init__(name, phone, email, address, salary, starting_date)
        self.serving_area = serving_area

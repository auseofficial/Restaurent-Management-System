class Restaurant:
    def __init__(self, name, rent, menu):
        self.name = name
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0

    def receive_payment(self, amount):
        self.revenue += amount
        self.balance += amount

    def pay_expense(self, amount, description):
        if amount <= self.balance:
            self.expense += amount
            self.balance -= amount
            print(f"Expense of ${amount} paid for {description}")
        else:
            print(f"Insufficient balance to pay ${amount} for {description}")

    def show_summary(self):
        print(f"\nRestaurant: {self.name}")
        print(f"Revenue: ${self.revenue}")
        print(f"Expenses: ${self.expense}")
        print(f"Balance: ${self.balance}")

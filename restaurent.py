class Restaurant:
    def __init__(self, name, menu, chef=None, server=None, manager=None):
        self.name = name
        self.menu = menu
        self.chef = chef
        self.server = server
        self.manager = manager
        self.revenue = 0
        self.expense = 0
        self.balance = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee  
        elif employee_type == 'manager':
            self.manager = employee  

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            customer.due_amount = order.bill - amount
            return f"Insufficient payment. {customer.due_amount} is still due."

    def pay_expense(self, amount, description):
        if amount <= self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')    

    def pay_salary(self, employee):
        if employee.salary <= self.balance:
            self.balance -= employee.salary
            employee.receive_salary()
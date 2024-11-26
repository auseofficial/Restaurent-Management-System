class Restaurant:
    def __init__(self, name, chef, server, manager):
        self.name = name
        self.chef = chef
        self.server = server
        self.manager = manager
        self.menu = []
        self.revenue = 0
        self.profit = 0
        self.balance = 0  # Missing initialization
        self.expense = 0  # Missing initialization
 
    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee  
        elif employee_type == 'manager':
            self.manager = employee  
            
    def receive_payment(self, order, amount, customer):  # Fixed spelling of 'recieve' to 'receive'
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            customer.due_amount = order.bill - amount
            return f"Insufficient payment. {customer.due_amount} is still due."
        
    def pay_expense(self, amount, description):
        if amount <= self.balance:  # Fixed logical error with '<' to '<='
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')    
       
    def pay_salary(self, employee):
        if employee.salary <= self.balance:  # Fixed logical error with '<' to '<='
            self.balance -= employee.salary
            employee.recieve_salary()


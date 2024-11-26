class Restaurant:
    def __init__(self, name, chef, server, manager):
        self.name = name
        self.chef = chef
        self.server = server
        self.manager = manager
        self.menu = []
        self.revenue = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee  
        elif employee_type == 'manager':
            self.manager = employee  
            
    def recieve_salary(self):
        self.due=0        
            
    def recieve_payment(self,order,amount,customer):
        if amount>=order.bill:
            self.revenue+=order.bill
            self.balance +=order.bill
            customer.due_amount=0
            return amount - order.bill
        
    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense += amount
            self.balance -=amount
            print(f'Expense{amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')    
       
    def pay_salary(self,employee):
        if employee.salary < self.balance:
            employee.recieve_salary()
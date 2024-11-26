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
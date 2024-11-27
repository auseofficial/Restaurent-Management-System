class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.cooking_time=15

class Burger(Food):
    def __init__(self,name,price,meat,ingradients):
        super().__init__(name,price)
        self.meat=meat
        self.ingradients=ingradients

class Pizza(Food):
    def __init__(self,name,price,isCold=True):
        super()  .__init__(name,price)
        self.isCold=isCold
        
              
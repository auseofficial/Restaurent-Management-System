from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name):
        self.name=name
        
class Customer(User):
    def __init__(self,name,money):
        self.money=money
        self.__order=order
        super().__init__(name)
        
    @property
    def order(self):
        return self.__order
    
    testing
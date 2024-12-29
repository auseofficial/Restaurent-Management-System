# num1 = int(input('Enter first number: ')) 
# num2 = int(input("Enter second number: ")) 

# # Calculate the sum
# total = num1 + num2

# # Print the result
# print("The sum is:", total)

# num=input("Write a number :")
# num=int(num)

# if num%2==0:
#     print(num, "is even")
# else:
#     print(num,"is odd")

#inheritance

# class Animal:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
        
# class Dog:
#     def __init__(self,eat):
#         self.eat=eat
       
# class Don(Animal,Dog):
#     def __init__(self,name,color,pamp):
#      super().__init__(name,color)
#      self.pamp=pamp

# obj1=Animal("foggy","black")     
# obj2=Dog("meat")
# obj3=Don("foggy","black","pampi")
# print(obj1.name)                   
# print(obj2.eat)
# print(obj3.pamp)

"""Encap"""

class Bank:
    def __init__(self, name,account_number,balance):
        self.name=name
        self.__account_number=account_number #private
        self._balance=balance #protected
        
    def deposit(self, amount):
        if amount <= 0:
            print("Enter a positive amount.")
        else:
            self._balance += amount
            print(f"Deposited {amount} successfully.")
            self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount} successfully.")
            # self.show_balance()

    def show_balance(self):
        print(f"Current Balance: {self._balance}")
        
    def showing_the_an(self):
        print(self.__account_number) 
        
    def showing_the_blnc(self):
        print(self._balance)
        
obj1=Bank("Shonar Bank",12345689,6500)
print(obj1.name)
print(obj1.showing_the_an()) 
print(obj1.showing_the_blnc())    
print(f"Direct access to protected balance: {obj1._balance}")
print(obj1.showing_the_an())

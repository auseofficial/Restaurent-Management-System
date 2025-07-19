# Importing necessary modules
from menu import Pizza, Burger, Drinks, Menu
from restaurent import Restaurant
from users import Customer
def main():
# Create a menu object  
    menu = Menu()
    # Add pizzas  
    pizza_1 = Pizza('Chicken Pizza', 600, False)
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Cheese Pizza', 500, False)
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Meat Pizza', 700, False)
    menu.add_menu_item('pizza', pizza_3)
    # Add burgers 
    burger_1 = Burger('Chicken Burger', 350, 'chicken', ['chicken', 'lettuce'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 400, 'beef', ['beef', 'cheese'])
    menu.add_menu_item('burger', burger_2)
    # Add drinks
    coke = Drinks('Coke', 50, False)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha', 80, True)
    menu.add_menu_item('drinks', coffee)
    # Display menu with numbering
    print("\nMenu:")
    item_mapping = {}  # Maps numbers to food items
    index = 1
    for category, items in menu.items.items():
        print(f"\n{category.capitalize()}:")
        for item in items:
            print(f"{index}. {item.name} - ${item.price}")
            item_mapping[str(index)] = item
            index += 1
    # Ordering food
    print("\nOrdering Food:")
    total_bill = 0
    ordered_items = []
    print("Enter the numbers corresponding to the items you want to order :")
    order_items = input("Your order: ").split(",")
 
    for item_number in order_items:
        item_number = item_number.strip()
        if item_number in item_mapping:
            food_item = item_mapping[item_number]
            ordered_items.append(food_item)
            total_bill += food_item.price

    # Collecting customer details
    print("\nEnter your details:")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    
    # Create a Customer instance
    customer = Customer(name, phone, email, address, 2000)  # Assuming a starting balance

    restaurant = Restaurant("Bangla Hotel", 1000, menu)
    # Generate Invoice
    print("\n" + "=" * 50)
    print("|{:^48}|".format("INVOICE"))
    print("=" * 50)
    print(f"| { 'Customer'.ljust(15)} : {customer.name.ljust(28)} |")
    print(f"| { 'Phone'.ljust(15)} : {customer.phone.ljust(28)} |")
    print(f"| { 'Email'.ljust(15)} : {customer.email.ljust(28)} |")
    print(f"| { 'Address'.ljust(15)} : {customer.address.ljust(28)} |")
    print("=" * 50)

    # Ordered items with centered alignment and prices
    print("|{:^48}|".format("Ordered Items"))
    for item in ordered_items:
     print(f"| {item.name.ljust(28)} - ${item.price:<14} |")
    print("=" * 50)
    print(f"| {'Total'.ljust(28)} : ${total_bill:<14} |")
    print("=" * 50)
if __name__ == "__main__":
    main()

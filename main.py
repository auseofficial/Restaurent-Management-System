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
    print("Enter the numbers corresponding to the items you want to order (comma-separated):")
    order_items = input("Your order: ").split(",")

    for item_number in order_items:
        item_number = item_number.strip()
        if item_number in item_mapping:
            food_item = item_mapping[item_number]
            print(f"Added {food_item.name} - ${food_item.price} to the order.")
            total_bill += food_item.price

    # Add the separator line before showing the total
    print("\n" + "_" * 20)
    print(f"Total Bill: ${total_bill}")

    # Create a restaurant object
    restaurant = Restaurant("Bangla Hotel", 1000, menu)

    # Example Customer
    customer = Customer("Akib Us Suny Eshan", "123456789", "john@example.com", "123 Street", 2000)
    print("\nInvoice:")
    print(f"Customer: {customer.name}")
    print(f"Total Bill: ${total_bill}")


if __name__ == "__main__":
    main()

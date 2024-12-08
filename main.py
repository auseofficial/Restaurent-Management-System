from menu import Pizza, Burger, Drinks, Menu
from restaurent import Restaurant
from users import Customer


def main():
    # Create a menu object
    menu = Menu()

    # Add pizzas
    menu.add_menu_item('pizza', Pizza('Chicken Pizza', 600, False))
    menu.add_menu_item('pizza', Pizza('Cheese Pizza', 500, False))
    menu.add_menu_item('pizza', Pizza('Meat Pizza', 700, False))

    # Add burgers
    menu.add_menu_item('burger', Burger('Chicken Burger', 350, 'Chicken', ['Chicken', 'Lettuce']))
    menu.add_menu_item('burger', Burger('Beef Burger', 400, 'Beef', ['Beef', 'Cheese']))

    # Add drinks
    menu.add_menu_item('drinks', Drinks('Coke', 50, False))
    menu.add_menu_item('drinks', Drinks('Mocha', 80, True))

    # Display menu
    print("\nMenu:")
    menu.show_menu()

    # Create a restaurant object
    restaurant = Restaurant("Bangla Hotel", 1000, menu)

    # Create a customer
    customer = Customer("Akib Us Suny Eshan", "1234567890", "john@example.com", "123 Street", 2000)

    # Simulate ordering food
    print("\nOrdering Food:")
    total_bill = 0
    print("Enter the numbers corresponding to the items you want to order (comma-separated):")
    order_items = input("Your order: ").split(",")

    for item in order_items:
        item = item.strip()
        if item.isdigit():
            item_index = int(item) - 1
            for category, items in menu.items.items():
                if 0 <= item_index < len(items):
                    food_item = items[item_index]
                    print(f"Added {food_item.name} - ${food_item.price} to the order.")
                    total_bill += food_item.price
                    break

    print(f"\nTotal Bill: ${total_bill}")

    # Payment
    customer.pay_for_order(total_bill)
    restaurant.receive_payment(total_bill)

    # Show restaurant summary
    restaurant.show_summary()


if __name__ == "__main__":
    main()

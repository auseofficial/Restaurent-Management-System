from menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef,Customer,Server

def main():
    # Create a menu object
    menu = Menu()
    
    # Add pizzas
    pizza_1 = Pizza('chicken pizza', 600, False)
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('cheese pizza', 500, False)
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('meat pizza', 700, False)
    menu.add_menu_item('pizza', pizza_3)

    # Add burgers
    burger_1 = Burger('chicken burger', 350, 'chicken', ['chicken', 'lettuce'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('beef burger', 400, 'beef', ['beef', 'cheese'])
    menu.add_menu_item('burger', burger_2)

    # Add drinks
    coke = Drinks('Coke', 50, False)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha', 80, True)
    menu.add_menu_item('drinks', coffee)

    # Display menu
    menu.show_menu()
    
    # Create a restaurant object
    restaurant = Restaurant("Bangla Hotel", menu)
 
if __name__ == "__main__":
    main()

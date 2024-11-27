from menu import Pizza, Burger,Drinks,Menu

def main():
    menu=Menu()
    pizza_1=Pizza('chicken pizza',600,'large',['chicken','onion'])
    menu.add_menu_item('pizza'.pizza_1)
    pizza_2=Pizza('cheese pizza',600,'large',['cheese','onion'])
    menu.add_menu_item('pizza'.pizza_2)
    pizza_3=Pizza('meat pizza',600,'large',['meat','onion'])
    menu.add_menu_item('pizza'.pizza_3)
    
    burger_1=Burger('chicken burger',600,'large',['chicken','onion'])
    menu.add_menu_item('burger',burger_1)
    burger_2=Burger('beef burger',600,'large',['beef','onion'])
    menu.add_menu_item('burger',burger_1)
    
    coke=
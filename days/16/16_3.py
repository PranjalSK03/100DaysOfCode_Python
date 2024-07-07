from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

while True:
    
    choice = input(f"welcome to the coffee machine What will you have? ({menu.get_items()}) : ").lower()
    
    if(choice == "exit"):
        print("Thank you for coming to coffee shop !!")
        break

    elif(choice == "report"):
        coffee.report()
        money.report()
    
    else:
        item = menu.find_drink(choice)
        
        if not item:
            continue
        if not coffee.is_resource_sufficient(item) or not money.make_payment(item.cost):
            continue

        coffee.make_coffee(item)
    


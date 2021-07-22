from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffee_maker = CoffeeMaker() 
menu = Menu()

off = False  

while not off:
  option = menu.get_items()
  choice = input(f"What would you like? ({option}): ")  
  if choice == "off":
    off = True
  elif choice == "report":
    coffee_maker.report()
    moneymachine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
  



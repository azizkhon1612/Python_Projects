from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == '__main__':

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        order_name = input(f"What would you like? ({menu.get_items()}): ").lower()

        if order_name == 'off':
            break

        if order_name == 'report':

            coffee_maker.report()
            money_machine.report()

            continue

        found_drink = menu.find_drink(order_name)

        if found_drink is not None:

            if coffee_maker.is_resource_sufficient(found_drink):

                if money_machine.make_payment(found_drink.cost):

                    coffee_maker.make_coffee(found_drink)

                else:
                    continue
            else:
                continue
        else:
            continue


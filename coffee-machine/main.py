from data import *


def check_resources(prompt):

    sufficient = True

    for k, v in MENU[prompt]['ingredients'].items():
        temp = resources[k] - v
        if temp >= 0:
            resources[k] -= v
        else:
            print(f"Sorry there is not enough {k}.")
            sufficient = False

    return sufficient


if __name__ == '__main__':

    """
    penny 0.01$
    dime 0.10$
    nickel 0.05$
    quarter 0.25$

    """

    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if prompt == 'report':
            for k, v in resources.items():
                print(f"{k} : {v}")
            continue

        if prompt == 'off':
            break

        if prompt in MENU.keys():
            if check_resources(prompt):
                quarters = round(int(input("How many quarters: ")) * 0.25, 2)
                dimes = round(int(input("How many dimes: ")) * 0.10, 2)
                nickles = round(int(input("How many nickles: ")) * 0.05, 2)
                pennies = round(int(input("How many pennies: ")) * 0.01, 2)

                money = quarters + dimes + nickles + pennies
                if money >= MENU[prompt]['cost']:

                    change = money - MENU[prompt]['cost']
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {prompt} ☕ Enjoy!")
                    resources['money'] += MENU[prompt]['cost']

                    continue
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    continue
            else:
                continue
        else:
            break

    exit(0)

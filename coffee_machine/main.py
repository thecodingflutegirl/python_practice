from menu_resources import MENU, resources
coffee_machine = True
price = 0


def available_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f'Sorry, there is not enough {"item"}')
            return False
    return True


def coin_transaction():
    total = int(input('How many quarters? ')) * .25
    total += int(input('How many dimes? ')) * .10
    total += int(input('How many nickles? ')) * .05
    total += int(input('How many pennies? ')) * .01
    return total


def transaction(payment, drink_cost):
    if payment >= drink_cost:
        global price
        price += drink_cost
        change = round(payment - drink_cost, 2)
        print(f'Here is ${change} back in change')
        return True
    else:
        print('Sorry, that is not enough money. Your money is refunded.')
        return False


def deduct_resources(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. ☕️ Enjoy!")


while coffee_machine:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        coffee_machine = False
    elif choice == 'report':
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${price}")
        print(f"Water: {resources['water']}ml")
    else:
        drink = MENU[choice]
        if available_resources(drink['ingredients']):
            payment = coin_transaction()
            if transaction(payment, drink['cost']):
                deduct_resources(choice, drink['ingredients'])

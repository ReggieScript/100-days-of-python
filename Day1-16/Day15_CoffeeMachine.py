MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")

def ingredients(order):
    res_milk = resources['milk']
    res_water = resources['water']
    res_coffee = resources['coffee']

    if order == 'espresso':
        order_milk = 0
    else:
        order_milk = MENU[order]['ingredients']['milk']

    order_water = MENU[order]['ingredients']['water']
    order_coffee = MENU[order]['ingredients']['coffee']

    if (order_milk > res_milk) or (order_water > res_water) or (order_coffee > res_coffee):
        if (order_milk > res_milk):
            print("Sorry, there's not enough milk.")
        if (order_water > res_water):
            print("Sorry, there's not enough water.")
        if (order_coffee > res_coffee):
            print("Sorry, there's not enough coffee.")
        return False



def new_resources():
    res_milk = resources['milk']
    res_water = resources['water']
    res_coffee = resources['coffee']

    if order == 'espresso':
        order_milk = 0
    else:
        order_milk = MENU[order]['ingredients']['milk']

    order_water = MENU[order]['ingredients']['water']
    order_coffee = MENU[order]['ingredients']['coffee']

    resources['milk'] = res_milk-order_milk
    resources['water'] = res_water-order_water
    resources['coffee'] = res_coffee-order_coffee

x=1
while x==1:
    order=input("What coffee would you like?(espresso/capuccino/latte)\n")
    if order== 'report':
        report()
    elif order == 'off':
        print('Turning off...')
        break
    else:
        if ingredients(order)==False:
            break
        else:
            price=MENU[order]['cost']
            print(f"The price is: ${price} ")

            print("Please insert coins.")

            quarters=int(input("How many quarters?\n"))*0.25
            dimes=int(input("How many dimes?\n"))*0.10
            nickels=int(input("How many nickels?\n"))*0.05
            pennies=int(input("How many pennies?\n"))*0.01

            payment=quarters+dimes+nickels+pennies
            print(f"Your payment is{payment}")


            if payment < price:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change=payment-price
                print(f"Here is ${change} in change")
                print(f"Here is your {order}. Enjoy!")
                new_resources()
                resources["money"]=price

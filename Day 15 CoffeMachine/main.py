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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
ESPRESSO_COST = MENU["espresso"]["cost"]
LATTE_COST = MENU["espresso"]["cost"]
CAPPUCCINO_COST = MENU["cappuccino"]["cost"]


off=False


def process_coin():
    print("please insert coin")
    quarter=int(input("enter quarter:"))
    dime=int(input("enter dime:"))
    nickel=int(input("enter nickel:"))
    penny=int(input("enter penny:"))
    total=0.25*quarter+0.1*dime+0.05*nickel+0.01*penny
    return total


def is_resource_sufficent(choice_ingredients):
    for item in choice_ingredients:
        if choice_ingredients[item] > resources[item]:
            return False
        else:
            return True


def is_transcation_succesful(payment, cost):
    if payment >= cost:
        change=round(payment - cost,2)
        print(f"Here is ${change} in change.")
        return True
    elif payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(choice_ingredients,drink_name):
    for item in choice_ingredients:
        resources[item] -= choice_ingredients[item]
    print(f"Here is your {drink_name} coffee.")




while not off:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice in MENU:
        if is_resource_sufficent(MENU[choice]["ingredients"]):
            payment = process_coin()
            if is_transcation_succesful(payment, MENU[choice]["cost"]):
                profit += MENU[choice]["cost"]
                make_coffe(MENU[choice]["ingredients"],choice)
        else:
            print("Sorry that's not enough reusorece.")
    elif choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Profit:${profit}")
    else:
        off=True
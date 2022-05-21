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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def isResourceSufficient(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def processCoins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def isTransactionSuccessful(moneyRecieved, drinkCost):
    if moneyRecieved >= drinkCost:
        return True
    else:
        change = round(moneyRecieved - drinkCost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drinkCost
        print("Sorry that's not enough money. Money refunded. ")
        return False


def makeCoffee(drinkName, orderIngredients):
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName}")


isOn = True

while isOn:
    choice = input("What would you like? (expresso/latte/cappuccino): ")
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}g")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])

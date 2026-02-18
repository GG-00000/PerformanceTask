meals = ["McChiken","Big Mac","QuaterPounder"],
sides = ["Small Fries", "Medium Fries", "Large Fries"],
drinks = ["Coke", "Pepsi", "Sprite"]
    
def find_meal(order):
    for meal in meals:
        if meal[0] == order:
            return meal
    return None

def find_side(order):
    for side in sides:
        if side[0] == order:
            return side
    return None

def find_drink(order):
    for drink in drinks:
        if drink[0] == order:
            return drink
    return None
    
def tell_order(meal,side,drink):
    print("heres your order")
    print(meal)
    print(side)
    print(drink)

Beginning = input("Welcome would you like to order something today?")

while Beginning == "yes":
    print("Here are our meals: McChiken, Big Mac, QuarterPounder")
    print("Here are our sides: Small Fries, Medium Fries, Large Fries")
    print("Here are our drinks: Coke, Pepsi, Sprite")
    meal = input("what do you want for your meal?")
    side = input("what do you want for your side?")
    drink = input("what do you want for your drink?")

    if meal:
        tell_order(meal[0])
    else:
        print("That meal doesnt exist")
    
    if side:
        tell_order(side[0])

        print("Okay goodbye")
def outro():
    print("Thanks for ordering from McMarco's")
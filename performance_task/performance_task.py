
meals = ["McChicken", "Big Mac", "Quarter Pounder"]
meal_prices = [3.50, 4.00, 4.25]

sides = ["Small Fries", "Medium Fries", "Large Fries"]
side_prices = [2.15, 2.50, 2.75]

drinks = ["Coke", "Pepsi", "Sprite"]
drink_prices = [1.50, 1.25, 1.35]


def find_item(order, item_list):
    for item in item_list:
        if item.lower() == order.lower():
            return item
    return None


def calculate_total(meal, side, drink):
    meal_index = meals.index(meal)
    side_index = sides.index(side)
    drink_index = drinks.index(drink)

    total = (
        meal_prices[meal_index]
        + side_prices[side_index]
        + drink_prices[drink_index]
    )
    return total


def tell_order(meal, side, drink):
    total = calculate_total(meal, side, drink)
    print("\nHere's your order:")
    print(meal, "-", meal_prices[meals.index(meal)])
    print(side, "-", side_prices[sides.index(side)])
    print(drink, "-", drink_prices[drinks.index(drink)])
    print("Total: $", total)


def main():
    beginning = input("Welcome! Would you like to order something today? ")

    while beginning.lower() == "yes":

        add_new = input("\nWould you like to add a new meal to the menu? (yes/no) ")

        if add_new.lower() == "yes":
            new_meal = input("Enter the name of the new meal: ")
            new_price = float(input("Enter the price of the new meal: "))
            meals.append(new_meal)
            meal_prices.append(new_price)
            print(new_meal, "has been added to the menu!")

        print("\nHere are our meals:", meals)
        print("Here are our sides:", sides)
        print("Here are our drinks:", drinks)

        meal_input = input("What do you want for your meal? ")
        side_input = input("What do you want for your side? ")
        drink_input = input("What do you want for your drink? ")

        meal = find_item(meal_input, meals)
        side = find_item(side_input, sides)
        drink = find_item(drink_input, drinks)

        if meal and side and drink:
            tell_order(meal, side, drink)
        else:
            print("One or more items don't exist. Please try again.")

        beginning = input("\nWould you like to order again? (yes/no) ")

    print("Thanks for ordering from McMarco's!")


main()

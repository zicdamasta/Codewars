# ------------------------------------------------------
# Some new cashiers started to work at your restaurant.
#
# They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
#
# All the orders they create look something like this:
#   "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
#
# The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
#
# Their preference is to get the orders as a nice clean string with spaces and capitals like so:
#   "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
#
# The kitchen staff expect the items to be in the same order as they appear in the menu.
#
# The menu items are fairly simple, there is no overlap in the names of the items:
#
#   1. Burger
#   2. Fries
#   3. Chicken
#   4. Pizza
#   5. Sandwich
#   6. Onionrings
#   7. Milkshake
#   8. Coke
# ------------------------------------------------------


def get_order(order):
    menu = [
        "Burger",
        "Fries",
        "Chicken",
        "Pizza",
        "Sandwich",
        "Onionrings",
        "Milkshake",
        "Coke",
    ]

    # Generate list of matching menu items
    food_list = []
    slicer_index = 0
    for i in range(len(order) + 1):
        search_string = order[slicer_index:i].title()
        if search_string in menu:
            food_list.append(search_string)
            slicer_index = i

    # Generete sorted list matching menu item order ¯\_(ツ)_/¯
    sorted_food_list = []
    for item in menu:
        if item in food_list:
            for item_count in range(food_list.count(item)):
                sorted_food_list.append(item)
    return " ".join(sorted_food_list)


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))

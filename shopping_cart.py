# Project 05 Shopping Cart - Milestone submission

shopping_cart = []
action = 0

print("Welcome to the Shopping Cart Program!")

while action != 5:
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: "))
    if action == 1:
        new_item = input("What item would you like to add? ").lower()
        shopping_cart.append(new_item)
        print(f"'{new_item}' has been added to the cart.")
    elif action == 2:
        print(f"The contents of the shopping cart are:")
        for item in shopping_cart:
            print(item)
    elif action == 5:
        print("Thank you. Goodbye.")
    else:
        print("Please enter a valid action.")

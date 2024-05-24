# Project 05 Shopping Cart - Final submission
# This program allows users to manage a shopping cart by adding, viewing, removing, and computing the total price.

shopping_cart = []  # list of items in the shopping cart
action = 0  # Variable to store the action selected by the user
prices = []  # list of prices for items in the shopping cart


print("Welcome to the Shopping Cart Program!")

# Main loop
while action != 5:
    print()
    print(f"SHOPPING CART({len(shopping_cart)} items)")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = int(input("Please enter an action: "))

    # Add a new item to the shopping cart
    if action == 1:
        new_item = input("What item would you like to add? ").lower()
        shopping_cart.append(new_item)
        new_price = float(input(f"What is the price of '{
                          new_item.capitalize()}'? "))
        prices.append(new_price)
        print(f"'{new_item.capitalize()}' has been added to the cart.")

    # Display the contents of the cart
    elif action == 2:
        if len(shopping_cart) <= 0:
            print("Shopping Cart is empty")
        else:
            print(f"The contents of the shopping cart are:")
            for i in range(len(shopping_cart)):
                print(
                    f"{i+1}. {shopping_cart[i].capitalize():<12} ${prices[i]:>5.2f}")

    # Remove an item from the cart
    elif action == 3:
        remove_item = int(input("Which item would you like to remove? "))
        remove_item = remove_item - 1
        if 0 <= remove_item < len(shopping_cart):
            shopping_cart.pop(remove_item)
            prices.pop(remove_item)
            print("Item removed")
        else:
            print("Invalid item number")

    # Compute the total price of the shopping cart
    elif action == 4:
        total = 0
        for price in prices:
            total += price
        print(f"The total price of the items in the shopping cart is ${
              total:.2f}")

    # Exit the program
    elif action == 5:
        print("Thank you. Goodbye.")

    # Handle invalid inputs
    else:
        print("Please enter a valid action.")

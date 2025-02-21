# -*- coding: utf-8 -*-
"""helperfunctions

Original file is located at
    https://colab.research.google.com/drive/1B2bhWivONSI3qckfBbEhFdq9XvusEIb3

Hey guys! If you're stuck on the project, here are some functions to help.
Just copy and paste them into the correct cells in your instructor's notebook.

❗ IMPORTANT: Don't just copy blindly—make sure you understand how they work!
"""

# 🛒 FOOD ORDERING HELPER FUNCTIONS
# 🚀 This file contains structured functions to help you with your project.
# 📖 Need a step-by-step explanation? Check out EXPLANATION.md:
# 👉 https://github.com/Gana-Joshua-Danlami/food-ordering-helper/blob/main/EXPLANATION.md

def get_user_choice():
    """
    Gets user input for food item selection.
    Ensures the input is a valid number between 1 and 4.
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice if choice != 4 else None  # Return None if user selects "Exit"
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_quantity():
    """
    Gets user input for the quantity of the selected food item.
    Ensures the input is a positive integer.
    """
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_item_name(choice):
    """
    Returns the food item name based on user selection.
    """
    menu = {1: "Pizza", 2: "Burger", 3: "Noodles"}
    return menu.get(choice, "Unknown Item")

def calculate_total_price(item_price, quantity):
    """
    Calculates total cost for the selected food item.
    """
    return item_price * quantity # Corrected indentation: The return statement should be aligned with the function body.

def place_order():
    """
    Handles the process of selecting food items and adding them to the cart.
    Returns a dictionary of the final order.
    """
    cart = {}

    while True:
        choice = get_user_choice()
        if choice is None: # Exit condition
            break

        item_name = get_item_name(choice)
        item_price = get_item_price(choice)
        quantity = get_quantity()

        total_price = calculate_total_price(item_price, quantity)

        cart[item_name] = {'quantity': quantity, 'total_price': total_price}

    return cart

def check_out(cart):
    """
    Displays the final order summary and total cost.
    """
    if not cart:
        print("Your cart is empty. No items to check out.")
        return

    print("Checking out...")
    print("Your order details:")

    total_price = 0

    for item, details in cart.items():
        quantity = details['quantity']
        item_total = details['total_price']
        total_price += item_total
        print(f"{item}: Quantity - {quantity}, Total Price - {item_total}")

    print(f"Total Order Price: {total_price}")
    print("Thank you for ordering!")

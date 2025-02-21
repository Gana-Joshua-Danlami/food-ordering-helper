{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "🛒 FOOD ORDERING SYSTEM – STEP-BY-STEP EXPLANATION\n",
        "\n",
        "✅ Clear verbal breakdown of each function\n",
        "✅ No code—just explanations\n",
        "✅ Easy to understand for beginners\n",
        "\n",
        "\n",
        "1️⃣ get_user_choice() – Asking the User to Pick a Food Item\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function asks the user to enter a number (1-4) to select a food item from the menu.\n",
        "\n",
        "If the user picks 4, the function returns None (which means they chose to exit).\n",
        "\n",
        "If the user enters an invalid number or text, it will keep asking until they enter a correct choice.\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. The user is asked to enter a number (1-4).\n",
        "\n",
        "\n",
        "2. If they enter a valid number (1, 2, or 3), the function returns that number.\n",
        "\n",
        "\n",
        "3. If they enter 4, the function returns None (which stops the ordering process).\n",
        "\n",
        "\n",
        "4. If they enter anything invalid (like letters or wrong numbers), it tells them and asks again.\n",
        "\n",
        "\n",
        "\n",
        "📌 Example:\n",
        "👤 User inputs: 2 → ✅ Returns 2 (Burger is selected)\n",
        "👤 User inputs: invalid → ❌ \"Invalid input, try again.\" (Keeps asking)\n",
        "👤 User inputs: 4 → ✅ Returns None (User exits the menu)"
      ],
      "metadata": {
        "id": "8UH3gUX3ahp7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "2️⃣ get_quantity() – Asking the User for Quantity\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function asks how many units of the food item the user wants to order.\n",
        "\n",
        "It only accepts positive numbers (1 or more).\n",
        "\n",
        "If the user enters 0 or a negative number, it tells them and keeps asking until they enter a valid quantity.\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. The user is asked to enter a quantity.\n",
        "\n",
        "\n",
        "2. If they enter a valid positive number, it is returned.\n",
        "\n",
        "\n",
        "3. If they enter 0 or a negative number, the function says, \"Quantity must be greater than 0\" and asks again.\n",
        "\n",
        "\n",
        "4. If they enter letters or symbols, the function says, \"Invalid input\" and asks again.\n",
        "\n",
        "\n",
        "\n",
        "📌 Example:\n",
        "👤 User inputs: 3 → ✅ Returns 3 (Order confirmed)\n",
        "👤 User inputs: -1 → ❌ \"Quantity must be greater than 0.\" (Asks again)\n",
        "👤 User inputs: invalid → ❌ \"Invalid input, try again.\" (Asks again)"
      ],
      "metadata": {
        "id": "gMAWdl4ihdYv"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "3️⃣ get_item_name(choice) – Converting the User’s Choice into a Food Name\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function takes the user’s choice (1, 2, or 3) and returns the food name.\n",
        "\n",
        "It looks up a dictionary where:\n",
        "\n",
        "1 = \"Pizza\"\n",
        "\n",
        "2 = \"Burger\"\n",
        "\n",
        "3 = \"Noodles\"\n",
        "\n",
        "\n",
        "If somehow the choice is invalid, it returns \"Unknown Item\" (but this shouldn't happen in normal usage).\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. The function receives a number (1, 2, or 3).\n",
        "\n",
        "\n",
        "2. It checks the menu dictionary and returns the correct food name.\n",
        "\n",
        "\n",
        "3. If the number isn't in the dictionary, it returns \"Unknown Item\" (as a fallback).\n",
        "\n",
        "\n",
        "\n",
        "📌 Example:\n",
        "🔢 Input: 1 → ✅ Returns \"Pizza\"\n",
        "🔢 Input: 2 → ✅ Returns \"Burger\"\n",
        "🔢 Input: 99 → ❌ Returns \"Unknown Item\" (Shouldn’t happen if get_user_choice() is used)"
      ],
      "metadata": {
        "id": "GNoCJXiBi3e0"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "4️⃣ get_item_price(choice) – Getting the Price of the Food Item\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function takes the user’s choice (1, 2, or 3) and returns the price of that item.\n",
        "\n",
        "It looks up a dictionary where:\n",
        "\n",
        "1 = 6500 (Pizza)\n",
        "\n",
        "2 = 3000 (Burger)\n",
        "\n",
        "3 = 1300 (Noodles)\n",
        "\n",
        "\n",
        "If the choice isn't in the dictionary, it returns 0 (but this shouldn’t happen in normal use).\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. The function receives a number (1, 2, or 3).\n",
        "\n",
        "\n",
        "2. It checks the price dictionary and returns the correct price.\n",
        "\n",
        "\n",
        "3. If the number isn't in the dictionary, it returns 0.\n",
        "\n",
        "\n",
        "\n",
        "📌 Example:\n",
        "🔢 Input: 1 → ✅ Returns 6500 (Pizza price)\n",
        "🔢 Input: 2 → ✅ Returns 3000 (Burger price)\n",
        "🔢 Input: 99 → ❌ Returns 0 (Shouldn’t happen if get_user_choice() is used)"
      ],
      "metadata": {
        "id": "JimpECtFjP-C"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "5️⃣ calculate_total_price(item_price, quantity) – Calculating the Total Cost\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function multiplies the price of the selected item by the quantity to get the total cost.\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. It receives two numbers:\n",
        "\n",
        "item_price (e.g., 6500)\n",
        "\n",
        "quantity (e.g., 2)\n",
        "\n",
        "\n",
        "\n",
        "2. It multiplies them to return the total price.\n",
        "\n",
        "\n",
        "\n",
        "📌 Example:\n",
        "🔢 Input: 6500, 2 → ✅ Returns 13000\n",
        "🔢 Input: 3000, 5 → ✅ Returns 15000"
      ],
      "metadata": {
        "id": "uq64i8Lrjcvx"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "6️⃣ place_order() – Managing the Whole Order Process\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function handles the entire ordering process.\n",
        "\n",
        "The user selects multiple items and adds them to a cart dictionary.\n",
        "\n",
        "When they finish ordering, the cart is returned.\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. The function creates an empty cart.\n",
        "\n",
        "\n",
        "2. It keeps asking the user to select items and quantities until they choose to exit.\n",
        "\n",
        "\n",
        "3. It adds each item to the cart with its quantity and total price.\n",
        "\n",
        "\n",
        "4. When the user exits, the function returns the final cart.\n",
        "\n",
        "\n",
        "\n",
        "📌 Example Output:\n",
        "🛒 { \"Pizza\": {\"quantity\": 2, \"total_price\": 13000}, \"Burger\": {\"quantity\": 1, \"total_price\": 3000} }"
      ],
      "metadata": {
        "id": "VG9TBpzvkUjW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "7️⃣ check_out(cart) – Printing the Receipt\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This function takes the cart dictionary and prints a receipt.\n",
        "\n",
        "It shows each item, quantity, and total cost.\n",
        "\n",
        "It also calculates the grand total and displays a thank-you message.\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. If the cart is empty, it prints \"Your cart is empty. No items to check out.\"\n",
        "\n",
        "\n",
        "2. If there are items, it prints:\n",
        "\n",
        "\"Checking out...\"\n",
        "\n",
        "Each item, its quantity, and price.\n",
        "\n",
        "The total order price.\n",
        "\n",
        "\"Thank you for ordering!\"\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "📌 Example Output:\n",
        "\n",
        "Checking out...\n",
        "Your order details:\n",
        "Pizza: Quantity - 2, Total Price - 13000\n",
        "Burger: Quantity - 1, Total Price - 3000\n",
        "Total Order Price: 16000\n",
        "Thank you for ordering!"
      ],
      "metadata": {
        "id": "yo2df2qqkf-b"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "8️⃣ food_ordering_app() – Running the Whole Program\n",
        "\n",
        "📌 What it does:\n",
        "\n",
        "This is the main function that starts the entire ordering process.\n",
        "\n",
        "It calls place_order() to take orders and check_out(cart) to print the receipt.\n",
        "\n",
        "\n",
        "📌 How it works:\n",
        "\n",
        "1. It prints \"Welcome to the Food Ordering App!\"\n",
        "\n",
        "\n",
        "2. Calls place_order() to get user orders.\n",
        "\n",
        "\n",
        "3. Calls check_out(cart) to display the final order summary.\n"
      ],
      "metadata": {
        "id": "yCrNOo2plA5q"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "🎯 Now you understand exactly how each function works!"
      ],
      "metadata": {
        "id": "A5A9_X__lNfi"
      }
    }
  ]
}

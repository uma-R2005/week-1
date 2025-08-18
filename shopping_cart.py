shopping_cart = ["phone", "charger", "headphones"]

while True:
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout (Exit)")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item to add: ")
        shopping_cart.append(item)
        print(f"'{item}' added to your cart.")

    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(f"'{item}' removed from your cart.")
        else:
            print(f"'{item}' is not in your cart.")

    elif choice == '3':
        if shopping_cart:
            print("Items in your cart:")
            for idx, product in enumerate(shopping_cart, start=1):
                print(f"{idx}. {product}")
            print(f"Total items: {len(shopping_cart)}")
        else:
            print("Your cart is empty.")

    elif choice == '4':
        print("Checking out. Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


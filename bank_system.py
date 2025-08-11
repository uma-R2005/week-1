balance = 1000.00

while True:
    print("\n--- Banking Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ₹{balance:.2f}")

    elif choice == '2':
        amount_str = input("Enter amount to deposit: ")
        if amount_str.replace('.', '', 1).isdigit():
            amount = float(amount_str)
            if amount > 0:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid amount entered.")

    elif choice == '3':
        amount_str = input("Enter amount to withdraw: ")
        if amount_str.replace('.', '', 1).isdigit():
            amount = float(amount_str)
            if 0 < amount <= balance:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("Invalid amount entered.")

    elif choice == '4':
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid option! Please choose between 1 and 4.")

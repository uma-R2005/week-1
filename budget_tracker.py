budget = []

def add_transaction(amount, description):
    budget.append({"amount": amount, "description": description})

def get_balance():
    return sum(item["amount"] for item in budget)

print("Welcome to Simple Budget Tracker!")
print("Commands: add, balance, quit")

while True:
    command = input("Enter command: ").strip().lower()

    if command == "add":
        try:
            amount = float(input("Enter amount (+ income, - expense): "))
            balance = get_balance()

            # Check if expense is more than balance
            if amount < 0 and abs(amount) > balance:
                print("Insufficient balance! Transaction NOT added.")
                continue

            description = input("Enter description: ")
            add_transaction(amount, description)
            print("Transaction added!")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif command == "balance":
        print(f"Current balance: ${get_balance():.2f}")

    elif command == "quit":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")

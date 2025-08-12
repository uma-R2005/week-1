import getpass

correct_pin = "1234"
balance = 1000  
max_attempts = 3
attempts = 0
withdrawal_limit = 3  
withdrawals_made = 0

while attempts < max_attempts:
    pin = getpass.getpass("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN accepted. Welcome!")
        
        while True:
            print("\nOptions:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            
            choice = input("Choose an option (1-4): ")
            
            if choice == "1":
                print(f"Your balance is: ${balance}")
                
            elif choice == "2":
                if withdrawals_made >= withdrawal_limit:
                    print(f"Withdrawal limit reached! You can only withdraw {withdrawal_limit} times per day.")
                    continue
                
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= balance:
                    balance -= amount
                    withdrawals_made += 1
                    print(f"Withdrawal successful. New balance: ${balance}")
                    print(f"Withdrawals made today: {withdrawals_made}/{withdrawal_limit}")
                else:
                    print("Insufficient funds!")
                    
            elif choice == "3":
                amount = float(input("Enter amount to deposit: $"))
                balance += amount
                print(f"Deposit successful. New balance: ${balance}")
                
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
                
            else:
                print("Invalid option. Please try again.")
        break  # Exit retry loop on successful PIN
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.\n")

if attempts == max_attempts:
    print("Too many incorrect attempts. Access denied.")

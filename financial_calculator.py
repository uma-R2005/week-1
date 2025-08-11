def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time, n):
    return principal * (1 + rate / (100 * n)) ** (n * time) - principal

def loan_payment(principal, rate, time):
    r = rate / (12 * 100)  # monthly interest rate
    n = time * 12  # number of monthly payments
    payment = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return payment

def main():
    print("Welcome to the Financial Calculator!")

    while True:
        print("\nChoose an option:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Loan Payment")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 4:
            print("Thank you for using the Financial Calculator. Goodbye!")
            break

        try:
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter annual interest rate (%): "))
            time = float(input("Enter time in years: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == 1:
            si = simple_interest(principal, rate, time)
            print(f"Simple Interest: {si:.2f}")
        elif choice == 2:
            try:
                n = int(input("Enter number of times interest compounded per year: "))
                ci = compound_interest(principal, rate, time, n)
                print(f"Compound Interest: {ci:.2f}")
            except ValueError:
                print("Invalid input for compounding frequency.")
        elif choice == 3:
            payment = loan_payment(principal, rate, time)
            print(f"Monthly Loan Payment: {payment:.2f}")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time, n):
    # n = number of times interest applied per time period
    return principal * (1 + rate/(100*n))**(n*time) - principal

def loan_payment(principal, rate, time):
    # monthly payment for loan using formula
    r = rate / (12 * 100)  # monthly interest rate
    n = time * 12  # number of monthly payments
    payment = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return payment

def main():
    print("Financial Calculator")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Loan Payment")
    choice = int(input("Choose calculation (1/2/3): "))

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time in years: "))

    if choice == 1:
        si = simple_interest(principal, rate, time)
        print(f"Simple Interest: {si:.2f}")
    elif choice == 2:
        n = int(input("Enter number of times interest compounded per year: "))
        ci = compound_interest(principal, rate, time, n)
        print(f"Compound Interest: {ci:.2f}")
    elif choice == 3:
        payment = loan_payment(principal, rate, time)
        print(f"Monthly Loan Payment: {payment:.2f}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


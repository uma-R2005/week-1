rates = {
    'USD': 1.0,
    'EUR': 0.9,
    'INR': 82.5,
    'JPY': 110.0
}

print("Welcome to the Currency Converter!")
print("Supported currencies:", ', '.join(rates.keys()))

while True:
    amount_str = input("\nEnter amount in USD (or type 'exit' to quit): ")
    if amount_str.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        amount = float(amount_str)
    except ValueError:
        print("Please enter a valid number.")
        continue

    target = input("Convert to which currency? ").upper()
    if target not in rates:
        print("Currency not supported. Try again.")
        continue

    converted = amount * rates[target]
    print(f"{amount} USD is approximately {converted:.2f} {target}")

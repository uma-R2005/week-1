def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Choose an option (1, 2, or 3): ")
        
        if choice == "1":
            temp_input = input("Enter temperature in Celsius: ")
            try:
                celsius = float(temp_input)
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "2":
            temp_input = input("Enter temperature in Fahrenheit: ")
            try:
                fahrenheit = float(temp_input)
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

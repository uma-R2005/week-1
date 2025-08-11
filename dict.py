def display_profile(profile):
    print("\n--- User Profile ---")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")

def update_profile(profile):
    print("\nWhich attribute would you like to update? (e.g. name, age, email)")
    attribute = input("Attribute: ").lower()
    if attribute in profile:
        new_value = input(f"Enter new value for {attribute}: ")
        if attribute == "age":
            if new_value.isdigit():
                profile[attribute] = int(new_value)
            else:
                print("Invalid input for age. Must be a number.")
                return
        else:
            profile[attribute] = new_value
        print(f"{attribute.capitalize()} updated successfully.")
    else:
        print("Attribute not found in profile.")

def add_attribute(profile):
    print("\nAdd a new attribute to profile:")
    key = input("Attribute name: ").lower()
    if key in profile:
        print("Attribute already exists. Try updating instead.")
    else:
        value = input(f"Enter value for {key}: ")
        if value.isdigit():
            value = int(value)
        profile[key] = value
        print(f"Added new attribute '{key}' with value '{value}'.")

def user_profile_manager():
    profile = {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.j@example.com"
    }

    while True:
        print("\nUser Profile Manager Menu:")
        print("1. View Profile")
        print("2. Update Existing Attribute")
        print("3. Add New Attribute")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            display_profile(profile)
        elif choice == '2':
            update_profile(profile)
        elif choice == '3':
            add_attribute(profile)
        elif choice == '4':
            print("Exiting User Profile Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    user_profile_manager()

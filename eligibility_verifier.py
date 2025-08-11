def check_eligibility(age):
    can_vote = age >= 18
    can_drive = age >= 16
    
    if can_vote:
        print("You are eligible to vote.")
    else:
        print(f"You are not eligible to vote. You can vote in {18 - age} year(s).")
        
    if can_drive:
        print("You are eligible to drive.")
    else:
        print(f"You are not eligible to drive. You can drive in {16 - age} year(s).")

while True:
    user_input = input("Enter your age (or type 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if not user_input.isdigit():
        print("Invalid input! Please enter a positive whole number for age.")
        continue
    
    age = int(user_input)
    if age < 0:
        print("Age cannot be negative. Try again.")
        continue
    
    check_eligibility(age)
    print()

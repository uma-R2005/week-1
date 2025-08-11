age = int(input("Enter your age: "))
is_student_input = input("Are you a student? (yes/no): ").strip().lower()
day_of_week = input("Enter the day of the week: ").strip().lower()

is_student = is_student_input == "yes"
is_weekday = day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]
is_young_or_senior = age < 18 or age > 60

gets_discount = is_student or (is_weekday and is_young_or_senior)

print("\n--- Eligibility Report ---")
print(f"Student: {is_student}")
print(f"Weekday: {is_weekday}")
print(f"Young or Senior: {is_young_or_senior}")

if gets_discount:
    print("\n🎟️ You are eligible for a discount on the movie ticket!")
else:
    print("\n💰 Sorry, you are not eligible for a discount.")

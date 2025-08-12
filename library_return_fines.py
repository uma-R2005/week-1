# Library System Constants
due_date = 10         # Suppose due day of the month
grace_period = 3      # 3 days after due date
fine_per_day = 5      # 5 currency units per day
lost_book_fee = 500   # 500 currency units fixed for lost books

# Inputs
return_status = input("Return status (on-time, late, lost): ").strip().lower()
return_day = 0
if return_status == "late":
    return_day = int(input("Enter return day of the month (1-31): "))

is_student = input("Are you a student? (yes, no): ").strip().lower()
late_count = int(input("Number of times you were late this year: "))

print("\nLibrary Return Summary")

# Logic Begins
if return_status == "on-time":
    print("Book returned on time. No fine applied.")
elif return_status == "late":
    days_late = return_day - due_date
    if days_late <= grace_period:
        print("Returned within grace period. No fine applied.")
    else:
        total_fine = (days_late - grace_period) * fine_per_day
        if is_student == "yes":
            total_fine *= 0.5  # 50 percent student discount
            print("Student discount applied.")
        print(f"Late by {days_late} days. Fine to pay: {int(total_fine)}")
    if late_count >= 3:
        print("You have been late multiple times. Please return books on time.")
elif return_status == "lost":
    print(f"Book marked as lost. Please pay the replacement fee: {lost_book_fee}")
    if is_student == "yes":
        print("Tip: Students can request replacement from department library fund.")
else:
    print("Invalid return status provided.")

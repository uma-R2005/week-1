print("=== Student Grade Calculator ===")

student_name = input("Enter student's name: ")
subject_count = int(input("Enter the number of subjects: "))

total_marks = 0

for i in range(1, subject_count + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    total_marks += mark

average = total_marks / subject_count

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\n=== Report Card ===")
print(f"Name        : {student_name}")
print(f"Subjects    : {subject_count}")
print(f"Total Marks : {total_marks}")
print(f"Average     : {average:.2f}")
print(f"Grade       : {grade}")

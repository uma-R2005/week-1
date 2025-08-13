import os
import webbrowser

students = []
subjects = ["Math", "Science", "English"]

# Built-in sample student reports
builtin_students = [
    {
        "name": "Alice Johnson",
        "marks": {"Math": 95, "Science": 88, "English": 92},
        "total": 275,
        "average": 91.67,
        "grade": "A+",
        "strengths": ["Math", "English"],
        "weaknesses": ["Science"],
        "prediction": "Excellent! Likely to score high in finals."
    },
    {
        "name": "Bob Smith",
        "marks": {"Math": 62, "Science": 55, "English": 60},
        "total": 177,
        "average": 59,
        "grade": "D",
        "strengths": ["Math"],
        "weaknesses": ["Science"],
        "prediction": "Needs improvement. Focus more."
    }
]

# Subject-wise video resources based on performance
detailed_resources = {
    "Math": {
        "low": "https://youtu.be/5zb0h3DgRkU",      # <40
        "medium": "https://youtu.be/V6yixyiJcos"    # 40–59
    },
    "Science": {
        "low": "https://youtu.be/F3KxpxfQdSg",
        "medium": "https://youtu.be/3Z-cYz2tyf0"
    },
    "English": {
        "low": "https://youtu.be/3yXstvEa6d4",
        "medium": "https://youtu.be/5FQ4mdjJQ1Q"
    }
}

def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def analyze_strengths(marks):
    max_score = max(marks.values())
    min_score = min(marks.values())

    strengths = [subj for subj, mark in marks.items() if mark == max_score]
    weaknesses = [subj for subj, mark in marks.items() if mark == min_score]

    return strengths, weaknesses

def predict_performance(avg):
    if avg >= 85:
        return "Excellent! Likely to score high in finals."
    elif avg >= 70:
        return "Good performance. Keep it up!"
    elif avg >= 50:
        return "Needs improvement. Focus more."
    else:
        return "At risk of failing. Extra help recommended."

def add_student():
    name = input("Enter student name: ")
    marks = {}

    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= score <= 100:
                    marks[subject] = score

                    # Suggest video help and open browser if needed
                    if score < 60:
                        if score < 40:
                            print(f"❗ Score in {subject} is critically low.")
                            print("📺 Opening beginner-level support video...")
                            webbrowser.open_new_tab(detailed_resources[subject]["low"])
                            print(f"👉 Watch this video here: {detailed_resources[subject]['low']}")
                        else:
                            print(f"⚠️ Score in {subject} is below 60.")
                            print("📺 Opening improvement video...")
                            webbrowser.open_new_tab(detailed_resources[subject]["medium"])
                            print(f"👉 Watch this video here: {detailed_resources[subject]['medium']}")
                    break
                else:
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(marks.values())
    avg = total / len(subjects)
    grade = calculate_grade(avg)
    strengths, weaknesses = analyze_strengths(marks)
    prediction = predict_performance(avg)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": avg,
        "grade": grade,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "prediction": prediction
    }

    students.append(student)
    print(f"\n{name}'s report added successfully!\n")

def view_reports():
    if not builtin_students and not students:
        print("No student data available.")
        return

    print("\n--- Built-in Sample Reports ---")
    for student in builtin_students:
        print("\n------------------------------")
        print(f"Name       : {student['name']}")
        print("Marks      :")
        for subject, score in student['marks'].items():
            print(f"  {subject:8}: {score}")
        print(f"Total      : {student['total']}")
        print(f"Average    : {student['average']:.2f}")
        print(f"Grade      : {student['grade']}")
        print(f"Strength(s): {', '.join(student['strengths'])}")
        print(f"Weaknesses : {', '.join(student['weaknesses'])}")
        print(f"Prediction : {student['prediction']}")

    if students:
        print("\n--- User Added Reports ---")
        for student in students:
            print("\n------------------------------")
            print(f"Name       : {student['name']}")
            print("Marks      :")
            for subject, score in student['marks'].items():
                print(f"  {subject:8}: {score}")
            print(f"Total      : {student['total']}")
            print(f"Average    : {student['average']:.2f}")
            print(f"Grade      : {student['grade']}")
            print(f"Strength(s): {', '.join(student['strengths'])}")
            print(f"Weaknesses : {', '.join(student['weaknesses'])}")
            print(f"Prediction : {student['prediction']}")
    print("\n------------------------------")

def export_reports():
    if not students:
        print("No student data to export.")
        return

    folder = "student_reports"
    os.makedirs(folder, exist_ok=True)

    for student in students:
        filename = f"{folder}/{student['name'].replace(' ', '_')}_report.txt"
        with open(filename, "w") as file:
            file.write(f"Report Card for {student['name']}\n")
            file.write("------------------------------\n")
            for subject, score in student['marks'].items():
                file.write(f"{subject:10}: {score}\n")
            file.write(f"Total       : {student['total']}\n")
            file.write(f"Average     : {student['average']:.2f}\n")
            file.write(f"Grade       : {student['grade']}\n")
            file.write(f"Strength(s) : {', '.join(student['strengths'])}\n")
            file.write(f"Weakness(es): {', '.join(student['weaknesses'])}\n")
            file.write(f"Prediction  : {student['prediction']}\n")
        print(f"✅ Report for {student['name']} saved to {filename}")
    print("✅ All reports exported successfully!\n")

def main_menu():
    while True:
        print("\n--- Student Report Menu ---")
        print("1. Add Student")
        print("2. View All Reports")
        print("3. Export Reports to Files")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_reports()
        elif choice == '3':
            export_reports()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 4.")

if __name__ == "__main__":
    main_menu()

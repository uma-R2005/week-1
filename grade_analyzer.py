import matplotlib.pyplot as plt
import os
from statistics import median

def read_scores_from_file(filename):
    """Reads scores from a file and returns a list of integers."""
    scores = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        score = int(line)
                        if 0 <= score <= 100:
                            scores.append(score)
                        else:
                            print(f"Ignored invalid score: {score}")
                    except ValueError:
                        print(f"Ignored non-integer entry: {line}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating new one...")
        open(filename, 'w').close()
    return scores


def write_score_to_file(filename, score):
    """Appends a valid score to the file."""
    with open(filename, 'a') as file:
        file.write(f"{score}\n")


def analyze_scores(scores):
    """Returns statistics as a dictionary."""
    if not scores:
        return None

    total = sum(scores)
    highest = max(scores)
    lowest = min(scores)
    average = total / len(scores)
    med = median(scores)
    perfect_count = scores.count(100)

    return {
        "count": len(scores),
        "average": round(average, 2),
        "median": med,
        "highest": highest,
        "lowest": lowest,
        "perfect_scores": perfect_count
    }


def print_stats(stats_dict):
    """Prints statistics from the dictionary."""
    if stats_dict is None:
        print("No scores to analyze.")
    else:
        print("\n📊 Grade Statistics:")
        print(f"Total Scores: {stats_dict['count']}")
        print(f"Average Score: {stats_dict['average']}")
        print(f"Median Score: {stats_dict['median']}")
        print(f"Highest Score: {stats_dict['highest']}")
        print(f"Lowest Score: {stats_dict['lowest']}")
        print(f"Perfect Scores (100): {stats_dict['perfect_scores']}")


def print_grade_distribution(scores):
    """Prints a horizontal histogram of score ranges in color."""
    bins = [0] * 10
    for score in scores:
        index = min(score // 10, 9)
        bins[index] += 1

    ranges = ['00-09', '10-19', '20-29', '30-39', '40-49',
              '50-59', '60-69', '70-79', '80-89', '90-100']

    colors = [
        '\033[91m',  # Red
        '\033[93m',  # Yellow
        '\033[92m',  # Green
        '\033[96m',  # Cyan
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[91m',  # Red again
        '\033[92m',  # Green again
        '\033[94m',  # Blue again
        '\033[95m'   # Magenta again
    ]
    reset = '\033[0m'

    print("\n📊 Grade Distribution:")
    for i in range(10):
        bar = '*' * bins[i]
        print(f"{ranges[i]}: {colors[i]}{bar}{reset} ({bins[i]})")


def show_grade_bar_chart(scores, filename):
    """Displays a matplotlib bar chart for grade distribution and saves it with filename prefix."""
    if not scores:
        print("No scores to display.")
        return

    bins = [0] * 10
    for score in scores:
        index = min(score // 10, 9)
        bins[index] += 1

    ranges = ['00-09', '10-19', '20-29', '30-39', '40-49',
              '50-59', '60-69', '70-79', '80-89', '90-100']

    colors = plt.cm.tab10.colors

    plt.figure(figsize=(10, 5))
    plt.bar(ranges, bins, color=colors, edgecolor='black')
    plt.title('Grade Distribution (Bar Chart)')
    plt.xlabel('Score Ranges')
    plt.ylabel('Number of Scores')
    plt.tight_layout()

    base_name = os.path.splitext(filename)[0]
    save_path = f"{base_name}_bar_chart.png"
    plt.savefig(save_path)
    print(f"✅ Bar chart saved as '{save_path}'")
    plt.show()


def show_grade_pie_chart(scores, filename):
    """Displays a matplotlib pie chart for grade distribution and saves it with filename prefix."""
    if not scores:
        print("No scores to display.")
        return

    bins = [0] * 10
    for score in scores:
        index = min(score // 10, 9)
        bins[index] += 1

    labels = ['00-09', '10-19', '20-29', '30-39', '40-49',
              '50-59', '60-69', '70-79', '80-89', '90-100']

    filtered_bins = [count for count in bins if count > 0]
    filtered_labels = [labels[i] for i in range(10) if bins[i] > 0]

    colors = plt.cm.tab10.colors

    plt.figure(figsize=(8, 8))
    plt.pie(filtered_bins, labels=filtered_labels, autopct='%1.1f%%',
            startangle=140, colors=colors)
    plt.title('Grade Distribution (Pie Chart)')
    plt.tight_layout()

    base_name = os.path.splitext(filename)[0]
    save_path = f"{base_name}_pie_chart.png"
    plt.savefig(save_path)
    print(f"✅ Pie chart saved as '{save_path}'")
    plt.show()


def repl(filename):
    """REPL (Read-Eval-Print Loop) interface."""
    print("\n📘 Grade Analyzer CLI")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input(">> ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        elif command == "help":
            print("""
Available Commands:
  stats        - Show score statistics
  add [score]  - Add a new score (0-100)
  list         - List all scores
  clear        - Delete all scores
  graph        - Show histogram in terminal
  graphgui     - Show bar chart in a window and save image
  pie          - Show pie chart of score distribution and save image
  exit         - Exit the program
""")

        elif command == "stats":
            scores = read_scores_from_file(filename)
            stats = analyze_scores(scores)
            print_stats(stats)

        elif command.startswith("add "):
            parts = command.split()
            if len(parts) == 2 and parts[1].isdigit():
                score = int(parts[1])
                if 0 <= score <= 100:
                    write_score_to_file(filename, score)
                    print(f"✅ Score {score} added.")
                else:
                    print("❌ Score must be between 0 and 100.")
            else:
                print("❌ Usage: add [score]")

        elif command == "list":
            scores = read_scores_from_file(filename)
            print(f"Scores: {scores}")

        elif command == "clear":
            confirm = input("Are you sure you want to clear all scores? (yes/no): ")
            if confirm.lower() == "yes":
                open(filename, 'w').close()
                print("✅ All scores cleared.")
            else:
                print("Canceled.")

        elif command == "graph":
            scores = read_scores_from_file(filename)
            print_grade_distribution(scores)

        elif command == "graphgui":
            scores = read_scores_from_file(filename)
            show_grade_bar_chart(scores, filename)

        elif command == "pie":
            scores = read_scores_from_file(filename)
            show_grade_pie_chart(scores, filename)

        else:
            print("❓ Unknown command. Type 'help' for a list of commands.")


def main():
    filename = "grades.txt"
    repl(filename)


if __name__ == "__main__":
    main()

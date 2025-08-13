import time
import os
from collections import defaultdict

# Sentences of increasing difficulty
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python programming is both fun and educational",
    "Developing software requires patience and skill",
    "Continuous practice leads to significant improvement",
    "Optimizing algorithms can greatly enhance performance"
]

leaderboard_file = "leaderboard.txt"
max_attempts_per_level = 3
time_limit = 30  # seconds per sentence

def load_leaderboard():
    leaderboard = []
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as f:
            for line in f:
                name, accuracy, wpm = line.strip().split(",")
                leaderboard.append((name, float(accuracy), float(wpm)))
    return leaderboard

def save_leaderboard(leaderboard):
    with open(leaderboard_file, "w") as f:
        for entry in leaderboard:
            f.write(f"{entry[0]},{entry[1]:.2f},{entry[2]:.2f}\n")

def display_leaderboard(leaderboard):
    if not leaderboard:
        print("Leaderboard is empty.")
        return
    print("\n--- Leaderboard (Top Scores) ---")
    print(f"{'Name':10} {'Accuracy (%)':15} {'WPM':5}")
    for name, acc, wpm in leaderboard:
        print(f"{name:10} {acc:<15.2f} {wpm:<5.2f}")

def calculate_accuracy(target, typed):
    correct_chars = 0
    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(target)) * 100
    return accuracy, correct_chars

def calculate_wpm(typed_text, elapsed_time):
    words = len(typed_text.split())
    minutes = elapsed_time / 60
    if minutes == 0:
        return 0
    return words / minutes

def analyze_input(original, user_input):
    original_words = original.split()
    input_words = user_input.split()

    missed_words = []
    spelling_mistakes = []

    for i, word in enumerate(original_words):
        if i >= len(input_words):
            missed_words.append(word)
        elif input_words[i] != word:
            spelling_mistakes.append((input_words[i], word))

    return missed_words, spelling_mistakes

def update_error_patterns(original, typed, error_dict):
    # Track character-level errors for learning report
    original_words = original.split()
    typed_words = typed.split()
    for i in range(len(original_words)):
        if i >= len(typed_words) or original_words[i] != typed_words[i]:
            error_dict[original_words[i]] += 1

def typing_test(sentence, error_dict):
    attempts = 0
    while attempts < max_attempts_per_level:
        print(f"\nType this sentence within {time_limit} seconds:")
        print(sentence)

        start_time = time.time()
        timed_out = False
        try:
            user_input = input("Your input: ")
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            return 0, 0, False

        elapsed = time.time() - start_time
        if elapsed > time_limit:
            print(f"\nTime's up! You took {elapsed:.2f} seconds, exceeding the limit.")
            attempts += 1
            continue

        accuracy, correct_chars = calculate_accuracy(sentence, user_input)
        wpm = calculate_wpm(user_input, elapsed)

        missed_words, spelling_mistakes = analyze_input(sentence, user_input)

        print("\nMistake Summary:")
        if missed_words:
            print("Missed words:", ", ".join(missed_words))
        else:
            print("No words missed!")

        if spelling_mistakes:
            print("Spelling mistakes:")
            for typed_w, correct_w in spelling_mistakes:
                print(f" - You typed '{typed_w}', expected '{correct_w}'")
        else:
            print("No spelling mistakes!")

        print(f"\nTime taken: {elapsed:.2f} seconds")
        print(f"Accuracy: {accuracy:.2f}% ({correct_chars} correct characters)")
        print(f"Typing Speed: {wpm:.2f} WPM")

        # Update error patterns
        update_error_patterns(sentence, user_input, error_dict)

        if accuracy >= 80:
            print("Great job! You passed this level.")
            return accuracy, wpm, True
        else:
            print("Accuracy below 80%. Try again.")
            attempts += 1

    print("Max attempts reached for this level.")
    return 0, 0, False

def update_leaderboard(leaderboard, name, accuracy, wpm):
    leaderboard.append((name, accuracy, wpm))
    leaderboard.sort(key=lambda x: (x[1], x[2]), reverse=True)
    if len(leaderboard) > 5:
        leaderboard.pop()
    save_leaderboard(leaderboard)

def main():
    print("Welcome to the Typing Speed and Accuracy Tester!")
    name = input("Enter your name: ")

    leaderboard = load_leaderboard()
    level = 0
    total_accuracy = 0
    total_wpm = 0
    levels_completed = 0
    error_dict = defaultdict(int)  # Tracks common word errors

    while level < len(sentences):
        print(f"\n--- Level {level + 1} ---")
        acc, wpm, passed = typing_test(sentences[level], error_dict)
        if passed:
            total_accuracy += acc
            total_wpm += wpm
            levels_completed += 1
            level += 1
        else:
            break

    if levels_completed > 0:
        avg_accuracy = total_accuracy / levels_completed
        avg_wpm = total_wpm / levels_completed
        print(f"\n{name}, you completed {levels_completed} level(s)!")
        print(f"Average Accuracy: {avg_accuracy:.2f}%")
        print(f"Average WPM: {avg_wpm:.2f}")
        update_leaderboard(leaderboard, name, avg_accuracy, avg_wpm)
    else:
        print("\nYou did not complete any levels. Better luck next time!")

    display_leaderboard(leaderboard)

    # Personalized weakness report
    print("\n--- Personalized Weakness Report ---")
    if error_dict:
        sorted_errors = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
        for err, count in sorted_errors:
            print(f"Word '{err}' mistyped {count} time(s)")
    else:
        print("No consistent errors detected. Great job!")

    print("\nThank you for playing!")

if __name__ == "__main__":
    main()

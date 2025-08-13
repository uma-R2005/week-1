import string
import time
import getpass

def has_repeated_chars(pwd, limit=3):
    count = 1
    for i in range(1, len(pwd)):
        if pwd[i] == pwd[i-1]:
            count += 1
            if count >= limit:
                return True
        else:
            count = 1
    return False

def has_sequential_chars(pwd, limit=4):
    for i in range(len(pwd) - limit + 1):
        seq = pwd[i:i+limit]
        if all(ord(seq[j]) + 1 == ord(seq[j+1]) for j in range(len(seq)-1)):
            return True
        if all(ord(seq[j]) - 1 == ord(seq[j+1]) for j in range(len(seq)-1)):
            return True
    return False

def score_password(pwd):
    score = 0
    feedback = []

    if len(pwd) >= 10:
        score += 1
    else:
        feedback.append("Add more characters (10+).")

    if any(c.islower() for c in pwd):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in pwd):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in pwd):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in string.punctuation for c in pwd):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !@#$).")

    return score, feedback

def show_strength_bar(score):
    bars = [
        "Very Weak",
        "Weak",
        "Fair",
        "Good",
        "Strong",
        "Excellent"
    ]
    print("Strength:", bars[score])

# --- Main program starts ---
print("Welcome to the Password Training Quest!")
print("Create a strong password to unlock the gate.\n")

creation_attempts = 0
recall_attempts = 0
MAX_RECALL_ATTEMPTS = 3

# Password creation loop
while True:
    password = getpass.getpass("Enter your password (input hidden): ")
    creation_attempts += 1

    if has_repeated_chars(password):
        print("Your password has too many repeated characters in a row. Try again.\n")
        continue

    if has_sequential_chars(password):
        print("Your password has sequential characters (like 1234 or abcd). Try again.\n")
        continue

    score, feedback = score_password(password)
    show_strength_bar(score)

    if score >= 5:
        print("Great! Your password is strong enough.")
        break
    else:
        print("Suggestions to improve:")
        for tip in feedback:
            print("-", tip)
        print("Try again...\n")

# Memory Delay with fading messages
print("\nYou now have 2 minutes to remember your password.")
print("We will test your memory after the timer ends.\n")

for i in range(1, 7):  # Every 20 seconds for 2 minutes
    time.sleep(20)
    print(f"Password strength is fading... Time passed: {i * 20} seconds")

# Memory recall attempts
print("\nTime's up!")

while recall_attempts < MAX_RECALL_ATTEMPTS:
    recall_attempts += 1
    user_memory = input(f"Re-enter your password from memory — Attempt {recall_attempts}: ")

    print("\nPassword Recall Check:")
    correct_chars = 0

    for i in range(min(len(password), len(user_memory))):
        real_char = password[i]
        user_char = user_memory[i]
        if real_char == user_char:
            print(f"Position {i+1}: Correct")
            correct_chars += 1
        else:
            print(f"Position {i+1}: Expected '{real_char}', got '{user_char}'")

    if len(password) != len(user_memory):
        print(f"Length mismatch: expected {len(password)} characters, got {len(user_memory)}")

    memory_result = correct_chars == len(password) and len(password) == len(user_memory)

    if memory_result:
        print("\nAccess Granted! You remembered the password correctly.")
        break
    else:
        print("\nIncorrect password. Try again.\n")

else:
    print("Access Denied! You failed to recall the password correctly after multiple attempts.")
    exit()

# Final outcome
print("\nFinal Outcome:")
print("Success! You created and remembered a strong password. You win.")
print(f"\nPassword Strength Score: {score}/5")
print(f"Correct Characters Recalled: {correct_chars}/{len(password)}")
print(f"Password Creation Attempts: {creation_attempts}")
print(f"Recall Attempts Taken: {recall_attempts}")

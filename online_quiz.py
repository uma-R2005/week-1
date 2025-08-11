import random
import threading

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) H2O", "B) CO2", "C) NaCl", "D) O2"],
        "answer": "A"
    }
]

TIME_LIMIT = 10  # seconds per question

def timed_input(prompt, time_limit):
    answer = [None]

    def get_input():
        answer[0] = input(prompt)

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(time_limit)

    if thread.is_alive():
        print(f"\nTime's up! No answer recorded.\n")
        return None
    return answer[0].strip().upper()

def run_quiz(questions_list):
    score = 0
    wrong_questions = []

    for i, q in enumerate(questions_list, 1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = timed_input(f"Your answer (A/B/C/D) - You have {TIME_LIMIT} seconds: ", TIME_LIMIT)

        if answer is None:
            print(f"Skipped! The correct answer was {q['answer']}.\n")
            wrong_questions.append(q)
        elif answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
            wrong_questions.append(q)

    return score, wrong_questions

def main():
    print("Welcome to the Online Quiz System!\n")

    all_questions = questions[:]
    random.shuffle(all_questions)

    score, wrong_questions = run_quiz(all_questions)
    print(f"Initial round complete! Your score: {score} out of {len(all_questions)}.\n")

    while wrong_questions:
        retry = input("Do you want to retry the questions you missed? (y/n): ").strip().lower()
        if retry == 'y':
            score_retry, wrong_questions = run_quiz(wrong_questions)
            score += score_retry
            print(f"Your updated score: {score}.\n")
        else:
            break

    print(f"Quiz finished! Final score: {score} out of {len(questions)}. Thanks for playing!")

if __name__ == "__main__":
    main()

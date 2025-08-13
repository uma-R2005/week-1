# Week 1 - DAY-4 Python Assignments

This repository demonstrates various concepts of loops (for and while) along with other essential Python programming constructs. The scripts explore real-world problems and practical use cases such as password strength validation, student performance reporting, typing speed testing, and statistical calculations.

## Files 

## password_strength_test.py
- Validates password strength based on:
  - Minimum length requirement.
  - Presence of uppercase and lowercase letters.
  - Inclusion of digits and special characters.
- Uses loops to iterate over password characters to check conditions.
- Provides detailed feedback on weaknesses like:
  - Repeated characters.
  - Sequential characters (e.g., 'abc', '123').
- Incorporates masking input using `getpass` for privacy.
- Offers real-time strength assessment and tips to improve passwords.

## student_report.py
- Collects student information and multiple subject marks.
- Calculates average marks and determines pass/fail status.
- Identifies weak subjects with marks below threshold.
- Provides recommendations by opening related educational videos in a browser.
- Saves reports to text files for record keeping.
- Demonstrates:
  - Use of loops to process multiple subjects.
  - Conditional logic for grading and feedback.
  - Interaction with external resources (web browser).

## typing_tester.py
- A comprehensive typing test with multiple difficulty levels.
- Implements a time limit per sentence using Python’s `time` module.
- Calculates accuracy by comparing typed input with the original sentence character-by-character.
- Computes Words Per Minute (WPM) as a performance metric.
- Tracks typing mistakes such as missed words and spelling errors.
- Maintains a leaderboard by saving top scores to a file.
- Provides a personalized weakness report highlighting commonly mistyped words.
- Uses:
  - Loops to allow multiple attempts and multiple levels.
  - File handling for leaderboard management.
  - String manipulation for analysis.
  - Dictionary for error tracking.

## assignment.py
- Implements calculation of mean, median, and mode for a list of scores.
- Uses sorting to find the median value.
- Uses dictionaries to count frequency of values for mode calculation.
- Handles edge cases such as:
  - No mode (all values equally frequent).
- Demonstrates looping over collections for calculations and frequency counts.
- Utilizes conditional statements to determine median in even/odd length lists.

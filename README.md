# Grade Analyzer CLI

The Grade Analyzer CLI is a Python-based command-line tool for managing and analyzing student grades. It supports storing grades, calculating statistics, and visualizing distributions through text-based and graphical outputs. Ideal for educators, tutors, or anyone working with student performance data.

---

## What It Does

This tool allows users to:

- Record valid student scores (0–100) to a text file.
- Analyze scores to compute key statistics such as average, median, highest, and lowest grades.
- Visualize the grade distribution via terminal-based histograms or GUI charts (bar/pie).
- Persistently store scores across sessions using a flat text file (`grades.txt`).

---

## Features & Functionality

### Add Scores
Accepts only valid integers between 0 and 100. Automatically appends the score to `grades.txt`.

### Analyze Scores
Calculates:
- Total number of scores
- Average score (rounded to 2 decimals)
- Median
- Highest and lowest scores
- Number of perfect scores (100)

### Grade Distribution
- Text Histogram: Colored bar graph in terminal
- Bar Chart (GUI): Uses `matplotlib` to display and save a bar chart
- Pie Chart (GUI): Shows percentage breakdown per grade range and saves it

### Score Management
- List: Displays all stored scores
- Clear: Erases all scores from the file with confirmation prompt

---

## Requirements

- Python 3.x
- `matplotlib` (for GUI-based visualizations)

Install dependencies with:

```bash
pip install matplotlib

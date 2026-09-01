# Task 0: Python Fundamentals, Data Analysis & Git

## Description
This repository contains the solutions for **Task 0**, a progressive mini-project covering Python basics, array manipulation with NumPy, tabular data analysis using Pandas, and data visualization using Matplotlib.

## Repository Structure
```text
task-0/
├── README.md
├── q1.py
├── q2.py
├── q3.py
├── q4.py
├── q5.py
├── q6.py
├── data/
│   ├── student_performance.csv
│   └── processed_student_performance.csv
└── plots/
    ├── final_scores.png
    ├── study_vs_score.png
    ├── score_distribution.png
    └── custom_plot.png
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pranjalgoyal7/IEEE-TASK-0.git
   cd task-0
   ```

2. **Set up a virtual environment (Recommended):**
   It is recommended to use a virtual environment to keep dependencies isolated and avoid polluting your main environment.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   The data analysis and visualization scripts (Q4-Q6) require external libraries. Install them via pip:
   ```bash
   pip install numpy pandas matplotlib
   ```

## Running the Solutions

Execute each script from the terminal inside the root directory of the repository (`task-0/`).

- **Q1 - List Analyzer:**
  ```bash
  python3 q1.py
  ```
- **Q2 - Lists, Functions and .copy():**
  ```bash
  python3 q2.py
  ```
- **Q3 - Prime Numbers Using for-else:**
  ```bash
  python3 q3.py
  ```
- **Q4 - NumPy Basics:**
  ```bash
  python3 q4.py
  ```
- **Q5 - Pandas and CSV Analysis:**
  *Ensure `data/student_performance.csv` is present in the `data/` directory before running.*
  ```bash
  python3 q5.py
  ```
- **Q6 - Visualizing Data with Matplotlib:**
  *Ensure Q5 has been run successfully so that `processed_student_performance.csv` is generated.*
  ```bash
  python3 q6.py
  ```

## Author
Pranjal Goyal
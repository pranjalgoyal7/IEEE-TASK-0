import matplotlib.pyplot as plt
import pandas as pd

# Load the processed data (or use the existing student_performance DataFrame)
# If your column is 'Name' instead of 'Student_Name', adjust the key accordingly.
student_performance = pd.read_csv('data/processed_student_performance.csv')


# 1. Bar Chart: Student Names vs Final Scores

plt.figure(figsize=(10, 5))
plt.bar(
    student_performance['Student'],
    student_performance['Final_Score'],
    color='#4C72B0',
    edgecolor='black',
    alpha=0.85,
)
plt.title('Student Names vs Final Scores', fontsize=13, fontweight='bold')
plt.xlabel('Student Name', fontsize=11)
plt.ylabel('Final Score', fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/final_scores.png', dpi=300)
plt.close()

# 2. Scatter Plot: Hours Studied vs Final Score

plt.figure(figsize=(8, 5))
plt.scatter(
    student_performance['Hours_Studied'],
    student_performance['Final_Score'],
    color='#DD8452',
    edgecolors='black',
    s=70,
    alpha=0.85,
)
plt.title('Hours Studied vs Final Score', fontsize=13, fontweight='bold')
plt.xlabel('Hours Studied', fontsize=11)
plt.ylabel('Final Score', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/study_vs_score.png', dpi=300)
plt.close()


# 3. Histogram: Distribution of Final Scores

plt.figure(figsize=(8, 5))
plt.hist(
    student_performance['Final_Score'],
    bins=8,
    color='#55A868',
    edgecolor='black',
    alpha=0.85,
)
plt.title('Distribution of Final Scores', fontsize=13, fontweight='bold')
plt.xlabel('Final Score Range', fontsize=11)
plt.ylabel('Number of Students', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/score_distribution.png', dpi=300)
plt.close()

# 4. Custom Plot: Attendance vs Score Improvement
# (Color-mapped by Final Score to show multi-variable correlation)

plt.figure(figsize=(9, 5))
scatter = plt.scatter(
    student_performance['Attendance'],
    student_performance['Improvement'],
    c=student_performance['Final_Score'],
    cmap='viridis',
    s=80,
    edgecolors='black',
    alpha=0.9,
)

# Reference line at Improvement = 0 to clearly divide gains vs drops
plt.axhline(
    0, color='crimson', linestyle='--', linewidth=1.2, label='Zero Improvement Baseline'
)

cbar = plt.colorbar(scatter)
cbar.set_label('Final Score', fontsize=10)

plt.title('Attendance vs Score Improvement', fontsize=13, fontweight='bold')
plt.xlabel('Attendance Rate (%)', fontsize=11)
plt.ylabel('Improvement (Final - Previous)', fontsize=11)
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/custom_plot.png', dpi=300)
plt.close()
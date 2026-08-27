import numpy as np

hours_studied = np.array([2, 4, 5, 6, 9])
attendance = np.array([80, 85, 90, 95, 100])
previous_scores = np.array([70, 75, 80, 85, 90])
final_scores = np.array([75, 80, 85, 90, 95])

print("Hours Studied:", hours_studied.shape, hours_studied.dtype)
print("Attendance:", attendance.shape, attendance.dtype)
print("Previous Scores:", previous_scores.shape, previous_scores.dtype)
print("Final Scores:", final_scores.shape, final_scores.dtype)

mean_final_scores = np.mean(final_scores)
max_final_scores = np.max(final_scores)
min_final_scores = np.min(final_scores)
standard_deviation_final_scores = np.std(final_scores)

print("Mean of Final Scores:", mean_final_scores)
print("Max of Final Scores:", max_final_scores)
print("Min of Final Scores:", min_final_scores)
print("Standard Deviation of Final Scores:", standard_deviation_final_scores)

final_scores_bonus = final_scores + 5
print("Final Scores after adding bonus points:", final_scores_bonus)

min75 = final_scores >= 75

passing_scores = final_scores[min75]
print("Scores >= 75:", passing_scores)
import pandas as pd

student_performance = pd.read_csv('data/student_performance.csv')

print(student_performance.head())

rows, cols = student_performance.shape
print("Number of rows, columns are: ", rows, cols)
print(student_performance.columns)

print(student_performance.isnull().values.any())

avg_final_score = student_performance['Final_Score'].mean()
print("Average Final Score:", avg_final_score)

top_student = student_performance.loc[student_performance['Final_Score'].idxmax()]
print("Top Performing Student:\n", top_student)

student_performance['Improvement'] = (student_performance['Final_Score'] - student_performance['Previous_Score'])

high_attendance_students = student_performance[student_performance['Attendance'] >= 80]
print("Students with Attendance >= 80%:\n", high_attendance_students)

student_performance = student_performance.sort_values(by='Final_Score', ascending=False)

student_performance.to_csv('data/processed_student_performance.csv', index=False)
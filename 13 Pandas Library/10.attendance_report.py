import pandas as pd
import numpy as np
import os

np.random.seed(42)

student_size = 50

roll_no = np.arange(1001, 1001 + student_size)

name_poll = ['Rishi','Akash','Rishika','Ankit', 'Rahul', 'Mohan', "Rohit", "Priya", 'Rajnandani']
name = np.random.choice(name_poll, size= student_size)

days = [f'Day_{i}' for i in range(1,31)]

attendance = np.random.choice(['P', 'A'], size= (student_size, len(days)), p=[0.70, 0.30])

df = pd.DataFrame(attendance, columns=days)

df.insert(0, 'Roll NO', roll_no)
df.insert(1, 'Name', name)

# print(df)


total_present = (df[days] == "P").sum(axis=1)
total_absent = (df[days] == "A").sum(axis=1)
attendance_per = (total_present / len(days)) * 100

summary_attendance = pd.DataFrame({
    'Roll No' : df['Roll NO'],
    'Name' : df['Name'],
    'Total Present' : total_present,
    'Total Absent' : total_absent,
    'Attendance % ' : attendance_per.round(2),
    'Status' : np.where(attendance_per < 60, 'Detain', 'Pass')
})

print("===== Final Student Attendance Report =====")
print(summary_attendance.head())

summary_attendance.to_csv("Student_Attendance_Report.csv", index = False)
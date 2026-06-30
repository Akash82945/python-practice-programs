import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Student_Attendance_Report.csv')
print(df.head())


total_day = df['Total Present'] + df['Total Absent']
persent = df['Total Present']
students = df['Roll No']

plt.plot(students, persent, marker='o', markersize=4)
plt.title('Line Chart of Students Attendance')
plt.xlabel("Students")
plt.ylabel('Marks')
plt.legend()
plt.tick_params(axis='x', rotation=45)


plt.tight_layout()
plt.show()





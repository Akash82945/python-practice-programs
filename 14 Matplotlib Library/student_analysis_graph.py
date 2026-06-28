import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student_Attendance_Report.csv')
print(df.head())

# Count Status
status_count = df['Status'].value_counts()
print(status_count)

# Visualize
categories = status_count.index
values = status_count.values

plt.bar(categories,values, color= ['green','red'], label= 'Student Count')
plt.title('Students Attendance Report')
plt.xlabel('Result Status')
plt.ylabel('No of Students')
plt.legend()
plt.grid(axis= 'y', linestyle = '--', alpha= 0.7)
plt.show()
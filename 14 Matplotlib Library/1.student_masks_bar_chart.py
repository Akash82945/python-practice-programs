import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Student_marksheet.csv')
print(df.head())

student_id = df['StudentID']
marks = df['Total Marks']
# marks = df['Percentage']
# marks = df['English']

plt.bar(student_id, marks, label= 'Students Marks')
plt.plot(student_id, marks, label= 'Students Marks', color= 'red')
plt.title('Student Marks Bar Chart')
plt.xlabel('Number of students')
plt.ylabel('Totla marks')
plt.legend()
plt.grid(True)
plt.show()
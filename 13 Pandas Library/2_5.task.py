import pandas as pd
import numpy as np

df = pd.read_csv('Student_marksheet.csv')
#print(df.head())
# 2. Find Average marks
# Average Column is already present in Dataset
# average_marks = (df['Total Marks']/5)
# print(f"Average marks : \n{average_marks}")



# 3. Filter Top Students
# top_5_student = df.sort_values(by='Total Marks', ascending=False).head()
# print(top_5_student)

# # Filter studetn who score gresster than 80% marks
# top_student = df[df['Maths']>75].sort_values(by='Percentage', ascending=False)[['Maths']]
# print(top_student) 
# print(f"No of student who get above 75 marks in maths : {len(top_student)}")




# 4. Add grade column
# grade_condition = [
#     (df['Percentage'] > 80) & (df["Result"] == 'Pass'),
#     (df['Percentage'] > 60) & (df["Result"] == 'Pass'),
#     (df['Percentage'] > 40) & (df["Result"] == 'Pass')
# ]

# grade_choices = ['A', 'B', 'C']

# df["Grade"] = np.select(grade_condition, grade_choices, default='F')

# print(df[['Student Name', 'Percentage', 'Result', 'Grade']])





# Loac CSV file

loaded_csv = pd.read_csv("Sales.csv")
print(loaded_csv.head())

import numpy as np
import pandas as pd


# Create Student marksheet 

np.random.seed(42)

student_size = 50

student_id = np.arange(1001, 1001 + student_size)

name_pool = [f"STU0{i}" for i in range(1,11)]
student_name = np.random.choice(name_pool, size=student_size)


math_marks = np.random.randint(20,90, size=student_size)
english_marks = np.random.randint(20,90, size=student_size)
python_marks = np.random.randint(20,90, size=student_size)
c_marks = np.random.randint(20,90, size=student_size)
java_marks = np.random.randint(20,90, size=student_size)



gender_pool = ['Male','Female']
gender = np.random.choice(gender_pool, size=student_size)



attendance = np.random.randint(55,100, size=student_size)

stream_pool = ['CSE','AIML','ME','CIVIL']
stream = np.random.choice(stream_pool,size=student_size)


student_data ={
    'StudentID' : student_id,
    'Student Name' : student_name,
    'Gender' : gender,
    'Stream' : stream,
    'Maths' : math_marks,
    'English' : english_marks,
    'Python' : python_marks,
    'C lang' : c_marks,
    'Java' : java_marks,
    'Attendance %' : attendance
}


df = pd.DataFrame(student_data)

df.to_csv("Student_marksheet.csv", index=False)

# Total Column
df['Total Marks'] = df['Maths'] + df['English'] + df['Python'] + df['C lang'] + df['Java']

# Percentage column
df['Percentage'] = (df['Total Marks']/500)*100

# Result
df['Result'] = np.where(
    (df['Maths']<33) | (df['English']<33) | (df['C lang']< 33) | (df['Java'] < 33) | (df['Python']<33),
    'Fail', 'Pass'
)


df.to_csv("Student_marksheet.csv", index=False)

print(df)
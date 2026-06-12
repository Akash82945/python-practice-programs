import numpy as np


# Task 8 : Create attendance dataset

# Create list of attendance
attendance = ['Present','Absent']
np.random.seed(42)     # fixe random value to permanent

# Create Dataset
attendance_dataset = np.random.choice(attendance, size=20, p=[0.7, 0.3] )
# Reshape into matrix (each row indicate Student and column indicate attendance)
attendance_matrix = attendance_dataset.reshape(4,5)

# Print attendance on terminal
print(f"\nAttendace : \n{attendance_matrix}")

# Total no of Persent of each student
present = np.sum(attendance_matrix == 'Present', axis=1)
print(f"\nTotal attendance of each students : {present}")

# Total no of Absent of each student
absent = np.sum(attendance_matrix == "Absent", axis=1)
print(f"\nTotal absent attendance : {absent}")

# Average of Overall class who Present
average_attendance = np.mean(present/5)*100
print(f"\nAverage of attendance of overall class : {average_attendance}%")

# Average of each student who present in class
np_average = np.mean(attendance_matrix == 'Present', axis=1)
print(f"\nAverage attendance of each students : {np_average}\n")


# Boolean masking to apply some condition
exam = np.where(np_average >= 75, "Eligible", "Not Eligible")
print("=== Students Details ===")
for i,(avg,stat) in enumerate(zip(np_average,exam),1):
    print(f"Student {i} : Attendance : {avg:.2f}%  |  Status : {stat}")
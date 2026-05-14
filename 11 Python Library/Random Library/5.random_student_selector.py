import random

students = [
    "Aarav Sharma", "Vivaan Patel", "Aditya Verma", "Ananya Iyer", "Diya Joshi",
    "Ishaan Gupta", "Kabir Rao", "Meera Nair", "Neha Kulkarni", "Rahul Mishra",
    "Rohan Deshmukh", "Saanvi Reddy", "Sai Choudhury", "Samaira Kapoor", "Siddharth Sen",
    "Tanya Saxena", "Arjun Malhotra", "Devansh Joshi", "Isha Bhatia", "Kriti Sethi",
    "Pranav Shah", "Riya Bansal", "Shreya Dutta", "Utkarsh Singh", "Yash Wardhan",
    "Aanya Dwivedi", "Hrithik Jain", "Kavya Pandey", "Manish Tiwari", "Pooja Hegde"
]

# random_student = random.choices(students, k=3)
random_student = random.sample(students, k=3)
print(random_student)
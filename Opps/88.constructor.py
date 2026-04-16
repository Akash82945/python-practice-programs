class constructor_example():
    
    def __init__(self,name,roll_no,s_class):
        self.name = name
        self.roll_no = roll_no
        self.subject = []
        self.s_class = s_class
        self.marks = None
        
    def s_marks(self):
        user_input = input(f"Enter each  subject  Marks, Seperated by space : ")
        new_marks = [ int(x) for x in user_input.split()]
        self.marks = new_marks
        return
    
    def result(self):
        if isinstance(self.marks,list):
            average = sum(self.marks)/len(self.marks) if self.marks else 0
        else:
            average = self.marks
            
        if 90 <= average <= 100:
            return "Excellent"
        elif 70 <= average < 90:
            return "Veryb Good"
        elif 50 <= average < 70:
            return "Average"
        elif 30 <= average < 50:
            return "Good"
        else:
            return "FAIL! Try Again."
        
    def subjects(self):
        sub = input("Enter any Subjects : ")
        new_sub = [ str(x) for x in sub.split()]
        self.subject = new_sub
        return 
    
    def average(self):
        if isinstance (self.marks,list):
            average = sum(self.marks) / len(self.marks) if self.marks else 0
            self.average = average
        return f"{average:.2f}"
    
    def student_details(self):
        return f"""
    Stuent Name : {self.name}
    Student Roll_no : {self.roll_no}
    student Subject : {self.subject} 
    Student Class : {self.s_class}
    Student Marks : {self.marks}
    Student Average Marks : {self.average()}
    Student Result : {self.result()} 
    """
    
student1 = constructor_example("Ankit",2304324,'AIML')

student1.subjects()
student1.s_marks()
student1.result()
print(student1.student_details())
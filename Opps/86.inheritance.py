class Employee():
    
    def __init__(self,id,name,department,salary,leave,attendance):
        self.id = id
        self.name = name
        self.department = department
        self.__salary = salary
        self.attendance = attendance
        self.leave = leave
        
    def get_salary(self):
        return self.__salary
        
    def emp_leave(self):
        if self.leave > 10:
            return "Policy Alert! Only 10 Day Leave Allowed!"
        
        per_day_salary = self.__salary/30
        deduction = per_day_salary * self.leave
        self.attendance -= self.leave
        self.__salary -= deduction
    
        return f"""
    Employee Attendance After Leave : {self.attendance}
    Employee Per-Day-Salary : {per_day_salary:.2f}
    Employee Deduction : {deduction:.2f}
    Employee Salary After Leave : {self.__salary:.2f} """
    
    def mark_attendance(self):
        employee_input = input(f"Click [Enter] to mark Attendance for {self.name}: ").lower()
        if employee_input == "":
            self.attendance += 1
            status =  "Attendance Marked"
        else:
            status = "Input not recognize."
            
        if self.attendance >=30:
            bonus = self.__salary*0.10
            self.__salary += bonus
            return f"{status} | Bonus Applied. New Salary {self.__salary:.2f}"
        
        return f"{status} | Error! Employee Not eligible."
    
    def promotion(self):
        if  20000 <=  self.__salary < 50000:
            self.department = "Senior AIML DEVELOPER"
            return self.department
        elif self.__salary >=50000 :
            self.department = "Super Senior AIML DEVELOPER"
        else:
            return "Employee Not eligible for Promotion"
        return f"Employee Promoted to {self.department}"
    
    def emp_details(self):
        return f"""
    
    === EMPLOYEE DETAILS ===
    Employee ID : {self.id}
    Employee Name : {self.name}
    Employee Department : {self.department}
    Employee Salary : {self.__salary:.2f}
    Current Attendance : {self.attendance}
    """
    
    
    
class Developer(Employee):
    
    def __init__(self,id,name,salary,leave,attendance,tech_stack):
        super().__init__(id,name,"AIML",salary,leave,attendance)
        self.tech_stack = tech_stack
        
    # def get_dev_details(self):
    #     return f"Developer Experties : {self.tech_stack}"

    def emp_details(self):
        basic = super().emp_details()
        return basic + f"Developer Experties : {self.tech_stack}"
    
    
emp1 = Employee(101,"Ankit",'AIML',25000,25,14)
emp2 = Developer(102,"Ankit",48000,0,20,"Python,C,C++,HTML,ChatCPT")

# print(f'''
#       {emp1.emp_details()}
#       {emp1.mark_attendance()}
#       {emp1.emp_leave()}
#       {emp1.promotion()}
#       {emp1.emp_details()}
#       ''')



print(f'''
      {emp2.emp_details()}
      {emp2.mark_attendance()}
      {emp2.emp_leave()}
      {emp2.promotion()}
      {emp2.emp_details()}
      ''')

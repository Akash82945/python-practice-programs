class Employee():
    
    def __init__(self,id,name,department,salary,leave):
        self.id = id
        self.name = name
        self.department = department
        self.__salary = salary
        self.attendance = 30
        self.leave = leave
        
    def work_details(self):
        if self.attendance > 0:
            return f"Work in Progress."
        return "Employee On Leave."
    
    def bonus(self):
        if self.attendance == 30:
            self.__salary = self.__salary + (self.__salary)*0.10
            return f"Employee Bonus Salalry : {self.__salary}"
        return "Not Eligible for Bonus."
    
    
    def get_salary_details(self):
        return self.__salary
    
    def emp_leave(self):
        if self.attendance == self.attendance:
            if self.leave > 10:
                return "Only Maximum 10 Day Leave Allowed!"
            else:
                self.attendance = self.attendance - self.leave
                per_day_salary = self.__salary/30
                deducation = per_day_salary*self.leave
                self.__salary = self.__salary - deducation
        return f"""
    === Leave Process ===
    Leave Day : {self.leave}
    Deduction : {deducation:.2f}
    Employee Attendance after Leave : {self.attendance}
    Employee Salary after Leave : {self.__salary:.2f}
        """
    
    def employee_details(self):
        return f'''
    === EMPLOYEE SETAILS ===
    ID : {self.id} 
    Name : {self.name}
    Department : {self.department}
    Attendance : {self.attendance}
    Salary : {self.__salary}
    '''
    
    
    
    
emp1 = Employee(121,"Akash","AIML",8000,5)

# print(emp1.employee_details())
# print(emp1.emp_leave())
# print(emp1.bonus())
# print(emp1.work_details())

print(f"""
      
      {emp1.employee_details()}
      {emp1.emp_leave()}
      {emp1.bonus()}
      {emp1.work_details()}
      
      """)
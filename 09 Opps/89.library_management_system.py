# class Library():
    
#     def __init__ (self,book_name,book_id,author,category,price,status,sr_no):
#         self.book_name = book_name
#         self.book_id = book_id
#         self.author = author
#         self.category = category
#         self.price = price
#         self.status = status
#         self.sr_no = sr_no
#         self.all_books = []
        
#     def book_issue(self):
#         if self.status == 'Available':
#             self.status = "Issue"
#             return 
#         else:
#             return 
            
#     def add_add(self):
#         user_input = input("Enter new Book : ")
#         user_input2 = int(input("Enter Book ID : "))
#         self.book_id = self.book_id.append(user_input2)
#         self.book_name = self.book_name.append(user_input)
#         return 
    
#     def search_book(self):
#         search = int(input("Enter name or id : "))
#         if self.book_id == search or self.book_name == search:
#             return f"Book Find : {self.book_id} / {self.book_name}"
    
#     def display_all_book(self):
#         return self.all_books
    
    
#     def details (self):
#         return f"""
#     Book Name : {self.book_name}
#     Book id : {self.book_id}
#     Book Author : {self.author}
#     Book category : {self.category}
#     Book Price : {self.price}
#     Book Status : {self.status}
#     Book sr_no : {self.sr_no}
#     """
    

# class student(Library):
    
#     def __init__(self,student_id,student_name,book_list):
#         super().__init__(student_id,student_name,book_list)
#         self.student_id = student_id
#         self.student_name = student_name
#         self.book_list = book_list
        
#     def details(self):
#         basic = super().details()
#         return basic + f"\nStudent Name : {self.student_id}\nStudent ID : {self.student_id}\nIssued Books : {self.book_list}"


    
# student1 = student('Physics',1342,'Newton','Science',599,'Received',12)
# student1.book_issue()

# print(student1.details())
    
    
    

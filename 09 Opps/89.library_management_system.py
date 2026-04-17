class Library():
    
    def __init__ (self,book_name,book_id,author,category,price,status,sr_no):
        self.book_name = book_name
        self.book_id = book_id
        self.author = author
        self.category = category
        self.price = price
        self.status = status
        self.sr_no = sr_no
        
    def book_issue(self):
        if self.status == 'Availabe':
            self.status = "Issue"
            return 
        else:
            return 
            
        
          
    def details (self):
        return f"""
    Book Name : {self.book_name}
    Book id : {self.book_id}
    Book Author : {self.author}
    Book category : {self.category}
    Book Price : {self.price}
    Book Status : {self.status}
    Book sr_no : {self.sr_no}
    """
    
student1 = Library('Physics',1342,'Newton','Science',599,'Received',12)
student1.book_issue()

print(student1.details())
    
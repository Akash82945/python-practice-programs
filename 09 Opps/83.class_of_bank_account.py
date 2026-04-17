# class Bank_Account():
    
#     def __init__(self,account_id,name,account_no,account_type):
#         self.account_id = account_id
#         self.name = name
#         self.account_no = account_no
#         self.account_type = account_type
        
#     def details_customer(self):
#         return f"===Customer Details=== \nAccount_id : {self.account_id}\nName : {self.name}\nAccount No : {self.account_no}\nAccount Type : {self.account_type}\n"
    
# customer1 = Bank_Account(101,"Akash",2304324,"Saving")
# customer2 = Bank_Account(102,"Ankit",2304327,"Current")

# print(customer1.details_customer())
# print(customer2.details_customer())




class Bank_Acount:
    
    def __init__(self,id,name,acc_no,acc_type,balance):
        
        self.id = id
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def transfer(self, receiver_user, amount):
        if amount <= 0:
            print(f"FAILED: Amount {amount} must be positive.")
            return False
        
        if self.__balance < amount:
            print(f"FAILED: Insufficient Balance for {self.name}")
            return False
        
        self.__balance -= amount
        receiver_user.__balance += amount
        
        # Sabhi widths ko 35 par set kiya taaki box perfect square bane
        w = 35 
        return f"""
+--------------------------------------------------+
|               BANKING TRANSACTION                |
+--------------------------------------------------+
|  [SENDER DETAILS]                                |
|  Name         : {self.name:<{w}} |
|  Acc No       : {self.acc_no:<{w}} |
|  Type         : {self.acc_type:<{w}} |
|  New Balance  : {self.__balance:<{w}} |
|                                                  |
|  [RECEIVER DETAILS]                              |
|  Name         : {receiver_user.name:<{w}} |
|  Acc No       : {receiver_user.acc_no:<{w}} |
|  New Balance  : {receiver_user.__balance:<{w}} |
+--------------------------------------------------+
| Status: SUCCESSFUL | Amount: {amount:<19} |
+--------------------------------------------------+"""

    
    
user1 = Bank_Acount(101, "Akash", 2304324, "Current", 5000)
user2 = Bank_Acount(102, "Ankit", 2304325, "Saving", 1200)
user3 = Bank_Acount(103, "Rahul", 2304326, "Saving", 1000)
user4 = Bank_Acount(104, "Sohan", 2304327, "Current", 500)

print(user1.transfer(user2,400))

# transfer = [
#     (user2,500),
#     (user3,200),
#     (user4,350)
# ]

# for receiver,amount in transfer:
#     result = user1.transfer(receiver,amount)
#     if result:
#         print(result)
#         print("-"*50)


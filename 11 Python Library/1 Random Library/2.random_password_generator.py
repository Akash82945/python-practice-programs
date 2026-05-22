# Random Password Generator
import random
import string

def generate_password(length=12):
    
    char = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(char) for i in range(length))
    
    return password

print(f"Your password is : {generate_password()}")
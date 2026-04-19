import random
import string

def generate_pass(length=12):
    char = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(char) for i in range(length))
    
    return password

print(f"Generate Password : {generate_pass(16)}")


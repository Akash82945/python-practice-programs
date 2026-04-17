def check_password(password):
    score = 0
    
    if len(password)>=8:
        score += 1
        
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isnumeric():
            num = True
        elif not char.isalnum():
            spc = True
            
    if upper: score+=1
    if lower: score+=1
    if num: score+=1
    if spc: score+=1
    
    if score<=2: return "Week"
    elif score<=4: return "Medium"
    else: return "Strong"
    
password = input("Enter the password: ")
result = check_password(password)
print(f"{password} is {result}")
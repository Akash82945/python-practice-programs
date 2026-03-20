def lcm(a,b):
    
    num_max= max(a,b)
    
    while True:
        if num_max%a == 0 and num_max%b ==0:
            return num_max
        num_max+=1
        
a = 4
b = 4

print(lcm(a,b))
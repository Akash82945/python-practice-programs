def count_vowels(string):
    
    vowels = "aeiouAEIOU"
    
    count = 0
    
    for i in string:
        if i in vowels:
            count += 1
    return count
        
print(count_vowels("Akash").lower())
def convert_to_lower(sentence):
    sentence = list(sentence)
    result = ""
    
    for num in sentence:
        code = ord(num)
        
        if code >=65 and code <=90:
            lower_code = code +32
            
            lower_char = chr(lower_code)
            # result.append(lower_char)
            result += lower_char
            
        else:
            result += num
            # result.append(num)
            
    return result
    
sentence = input("Enter the sentence: ")
result = convert_to_lower(sentence)
print(f"Original sentence ({sentence})")
print(f"lower sentence ({result})")
def count_character(sentence):
    map = {}
    
    for char in sentence:
        if char in map:
            map[char] = map[char]+1
        else:
            map[char] = 1
            
    return map

sentence = "This is the code."
result = count_character(sentence)
print(f"Frequency in character {result}")
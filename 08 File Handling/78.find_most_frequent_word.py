def most_frequent():
    
    with open ("File Handling/Note.txt", "r") as file:
        content = file.read()
    
    words = content.lower().replace(".","").split()
        
    word_map = {}
    
    # frequent_word = []
    for word in words:
        if word in word_map:
            # frequent_word.append(word)
            word_map[word] += 1
        else:
            word_map[word] = 1
                
    most_frequent_word = max(word_map, key=word_map.get)
    return most_frequent_word,word_map[most_frequent_word]


word , count = most_frequent()
print(f"Most frequent word is {word} appering {count} time.")
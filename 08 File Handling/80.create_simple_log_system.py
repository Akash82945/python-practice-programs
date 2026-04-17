# import logging

# logging.basicConfig(
#     filename= 'app.log',
#     filemode='a',
#     format='%(asctime)s- %(levelname)s -%(message)s',
#     level=logging.INFO
# )

# def divide(a,b):
#     logging.info(f"Attempting to divide {a} by {b}")
#     try:
#         result = a/b
#         logging.info("Division successful")
#         return result
#     except ZeroDivisionError:
#         logging.error("User attempted to divide by zero!")
#         return None
    
# divide(10,0)


import datetime

def write_log(level, message):
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d  %H:%M:%S")
    
    log_entry = f"[{timestamp}] {level.upper()}: {message}\n"
    
    with open("Programing_history" , "a") as log_file:
        log_file.write(log_entry)
        
        
def replace_word_with_loggin(old_word, new_word):
    try:
        with open("File Handling/Note.txt", 'r') as file:
            content = file.read()
            
        if old_word in content:
            new_content = content.replace(old_word,new_word)
            with open ("File Handling/Note.txt", 'w') as file:
                file.write(new_content)
                
            write_log("INFO", f"Replace {old_word} with {new_word}")
            return "successfull"
        
        else:
            write_log("WARNING", f"Failed to replace {old_word} not found.")
            return "Word not found."
        
    except Exception as e:
        write_log("ERROR", f"System Crash {str(e)}")
        return "An error occurred."
    
print(replace_word_with_loggin("Python","Java"))
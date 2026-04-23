import random
import time

def quize_game():
    
    quize_data = [
        {
            "question": "Q. Python ka extension kya hai?",
            "option": ["A. .py", "B. .js", "C. .php", "D. .txt"],
            "answer": "A"
        },
        {
            "question": "Q. Computer ka brain kise kaha jata hai?",
            "option": ["A. RAM", "B. CPU", "C. Mouse", "D. Keyboard"],
            "answer": "B"
        },
        {
            "question": "Q. World Wide Web (www) kisne banaya?",
            "option": ["A. Bill Gates", "B. Mark Zuckerberg", "C. Tim Berners-Lee", "D. Steve Jobs"],
            "answer": "C"
        },
        {
            "question": "Q. Sabse chhota planet kaun sa hai?",
            "option": ["A. Mars", "B. Venus", "C. Earth", "D. Mercury"],
            "answer": "D"
        },
        {
            "question": "Q. RAM ka full form kya hai?",
            "option": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Any Memory", "D. Rapid Access Memory"],
            "answer": "B"
        },
        {
            "question": "Q. Ek Byte mein kitne Bits hote hain?",
            "option": ["A. 4", "B. 8", "C. 16", "D. 32"],
            "answer": "B"
        },
        {
            "question": "Q. Bharat ki Rajdhani (Capital) kya hai?",
            "option": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
            "answer": "C"
        },
        {
            "question": "Q. Python mein list banane ke liye kaun sa bracket use hota hai?",
            "option": ["A. ()", "B. {}", "C. <>", "D. []"],
            "answer": "D"
        },
        {
            "question": "Q. Solar System mein kitne planets hain?",
            "option": ["A. 7", "B. 8", "C. 9", "D. 10"],
            "answer": "B"
        },
        {
            "question": "Q. HTML ka use kya banane mein hota hai?",
            "option": ["A. Mobile App", "B. Operating System", "C. Web Page", "D. Video Game"],
            "answer": "C"
        }
    ]
    
    
    score = 0
    
    print(" ===== Welcome to Quiz Game! =====")
    
    random.shuffle(quize_data)
    
    for ques in quize_data:
        print(f"\n{ques['question']}")
        for opt in ques['option']:
            print(opt)
           
            
                
        start_time = time.time()
        user_input = input("Enter your answer [A,B,C,D] or '5050' : ").lower().strip()
        end_time = time.time()
        
        duration = end_time - start_time
                
                
        lifeline = True
        if user_input == '5050':
            if lifeline:
                lifeline = False
            
                correct_option = [o for o in ques['option'] if not o.startswith(ques['answer'])][0]
                wronge_option = [o for o in ques['option'] if not o.startswith(ques['answer'])]
                random_wrong = random.choice(wronge_option)
                
                print(f"\n--Lifeline Used! -- \n{correct_option}\n{random_wrong}")
                user_input = input("Final Answer: ").strip().lower()
            
            else:
                print("Lifeline already used! Choose an answer quickly.")
                user_input = input("Answer: ").strip().lower()
                

        
        
        
        if user_input == ques['answer'].lower():
            if duration <= 10:
                print(f"Correct! You Took {duration:.2f} Time.")
                score += 10
            else:
                print(f"Wrone! You Took {duration:.2f} Time")
        else:
            print(f"Wrong Answer. Correct answer {ques['answer']}")  
    
    
    print('-'*30)
    print(f"Quize test End. Your Score {score}/100")
    
quize_game()
            
        
    
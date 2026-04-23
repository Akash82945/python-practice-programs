def quize_game():
    
    quize_data = [
        {
            "question": "1. Python ka extension kya hai?",
            "option": ["A. .py", "B. .js", "C. .php", "D. .txt"],
            "answer": "A"
        },
        {
            "question": "2. Computer ka brain kise kaha jata hai?",
            "option": ["A. RAM", "B. CPU", "C. Mouse", "D. Keyboard"],
            "answer": "B"
        },
        {
            "question": "3. World Wide Web (www) kisne banaya?",
            "option": ["A. Bill Gates", "B. Mark Zuckerberg", "C. Tim Berners-Lee", "D. Steve Jobs"],
            "answer": "C"
        },
        {
            "question": "4. Sabse chhota planet kaun sa hai?",
            "option": ["A. Mars", "B. Venus", "C. Earth", "D. Mercury"],
            "answer": "D"
        },
        {
            "question": "5. RAM ka full form kya hai?",
            "option": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Any Memory", "D. Rapid Access Memory"],
            "answer": "B"
        },
        {
            "question": "6. Ek Byte mein kitne Bits hote hain?",
            "option": ["A. 4", "B. 8", "C. 16", "D. 32"],
            "answer": "B"
        },
        {
            "question": "7. Bharat ki Rajdhani (Capital) kya hai?",
            "option": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
            "answer": "C"
        },
        {
            "question": "8. Python mein list banane ke liye kaun sa bracket use hota hai?",
            "option": ["A. ()", "B. {}", "C. <>", "D. []"],
            "answer": "D"
        },
        {
            "question": "9. Solar System mein kitne planets hain?",
            "option": ["A. 7", "B. 8", "C. 9", "D. 10"],
            "answer": "B"
        },
        {
            "question": "10. HTML ka use kya banane mein hota hai?",
            "option": ["A. Mobile App", "B. Operating System", "C. Web Page", "D. Video Game"],
            "answer": "C"
        }
    ]
    
    
    score = 0
    
    for ques in quize_data:
        print(f"\n {ques['question']}")
        for opt in ques['option']:
            print(opt)
            
        user_input = input("Enter your answer [A,B,C,D] : ").lower()
        if user_input == ques['answer'].lower():
            print("Correct.")
            score += 10
            
        else:
            print("Wrong")
            
    print(f"Quize test End. Your Score {score}")
    
quize_game()
            
        
    
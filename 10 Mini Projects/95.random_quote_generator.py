import random

quotes = [
    {"author": "Steve Jobs", "text": "The only way to do great work is to love what you do."},
    {"author": "Albert Einstein", "text": "In the middle of every difficulty lies opportunity."},
    {"author": "Winston Churchill", "text": "Success is not final, failure is not fatal: it is the courage to continue that counts."},
    {"author": "Ralph Waldo Emerson", "text": "Do not go where the path may lead, go instead where there is no path and leave a trail."},
    {"author": "John Lennon", "text": "Life is what happens when you're busy making other plans."},
    {"author": "George Addair", "text": "Everything you've ever wanted is on the other side of fear."},
    {"author": "Henry Ford", "text": "Whether you think you can or you think you can't, you're right."},
    {"author": "Chinese Proverb", "text": "The best time to plant a tree was 20 years ago. The second best time is now."},
    {"author": "Abraham Lincoln", "text": "Whatever you are, be a good one."},
    {"author": "Franklin D. Roosevelt", "text": "The only thing we have to fear is fear itself."}
]

# Example: How to access a specific quote
# print(quotes_dict["Steve Jobs"])

random_quote = random.choice(quotes)
print(f'\nToday Inspiration :\nAuthor Namr: "{random_quote["author"]}\nQuotes : "{random_quote["text"]}\n')
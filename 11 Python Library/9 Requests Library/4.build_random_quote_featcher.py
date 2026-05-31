import requests


# Random quotes generator

def get_random_quote():

    url = 'https://dummyjson.com/quotes/random'

    try:
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        quotes = data.get("quote")
        author = data.get("author")
        
        print('=== Random Quotes Generator ===')
        print(f'\nQuotes : {quotes}')
        print(f"\nAuthor : {author}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        

get_random_quote()





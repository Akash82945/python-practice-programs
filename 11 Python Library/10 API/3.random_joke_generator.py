import requests


# Random Joke generator

url = 'https://v2.jokeapi.dev/joke/Any?type=single'

try:
    
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    
    print(f'''
=== Random Joke Generator ===
Joke : {data['joke']}
          ''')
    
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
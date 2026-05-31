import requests


# Fetch github API data

url = 'https://api.github.com'

try:
    response = requests.get(url)

    response.raise_for_status()
    
    data = response.json()

    print(data)
    
except requests.exceptions.RequestException as e:
    print(f"Error {e}")
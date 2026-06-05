import requests
from bs4 import BeautifulSoup


# Extract website title

url = 'https://github.com'

try:
    
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    
    title = soup.title.text
    print(title)
    
except requests.exceptions.RequestException as e:
    print(f'Error : {e}')
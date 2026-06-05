import requests
from bs4 import BeautifulSoup


# Extract all links

url = 'https://github.com'

try:
    
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
    
except requests.exceptions.RequestException as e:
    print(f'Error : {e}')
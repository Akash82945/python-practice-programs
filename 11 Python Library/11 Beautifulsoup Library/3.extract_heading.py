import requests
from bs4 import BeautifulSoup


# Extract heading

url = 'https://github.com'

try:
    
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find_all('h2')
    for t in title:
        headings =  t.text.strip()
        print('* ',headings)
        
except requests.exceptions.RequestException as e:
    print(f'Error : {e}')
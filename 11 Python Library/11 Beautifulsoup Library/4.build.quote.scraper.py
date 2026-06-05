import requests
from bs4 import BeautifulSoup


# Build Quote Scraper

url = 'https://quotes.toscrape.com'

try:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_quotes = soup.find_all('div', class_='quote')
    print(f'Total quotes : {len(all_quotes)}')
    
    for quote in all_quotes:
        text = quote.find('span', class_='text').text.strip()
        author = quote.find("small", class_='author').text.strip()
        
        tags_list = []
        
        tags = quote.find_all('a', class_ ='tag')
        for tag in tags:
            tags_list.append(tag.text.strip())
        
        clean_tags = ', '.join(tags_list)
        
        print(f'''
    Quote : {text}
    Author : {author}
    Tags : {clean_tags}
              ''')
    
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
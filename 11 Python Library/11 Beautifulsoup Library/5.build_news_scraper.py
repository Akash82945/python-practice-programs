import requests
from bs4 import BeautifulSoup


# Build News Scraper

url = 'https://www.indiatoday.in'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try: 
    
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    all_headings = soup.find_all('h2')
    
    print('INDIA TODAY - TOP 5 NEWS HEADLINES')
    
    count = 0
    for line in all_headings:
        clean_text = line.text.strip()
        
        if clean_text and len(clean_text) > 20:
            count += 1
            print(f"{count} : {clean_text}")
            
            if count == 5:
                break
    if count == 0:
        print*"No News Headlines not found." 
        
           
except requests.exceptions.RequestException as e:
    print(f'Error : {e}')
    
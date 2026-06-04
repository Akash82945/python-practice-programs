import requests
import xml.etree.ElementTree as ET


# Featch News Headline

def news_headlines():
    
    # url = 'https://feeds.bbci.co.uk/news/rss.xml'   # UK News
    url = 'https://timesofindia.indiatimes.com//rssfeeds/-2128936835.cms'    # Indian News
    
    try:
        
        response = requests.get(url)
        response.raise_for_status()
        
        
        root = ET.fromstring(response.content)
        
        print('=== Live News Headlines ===')
        
        count = 1
        
        for item in root.findall('.//item'):
            if count > 5:
                break
            
            title = item.find('title').text
            content = item.find('description').text.split('</a>')[-1]
            
            print(f'''
{count}. Headline : {title}
Summary : {content}
                  ''')
            
            count += 1
            
    except requests.exceptions.RequestException as e:
        print(f'Error : {e}')
        

news_headlines()
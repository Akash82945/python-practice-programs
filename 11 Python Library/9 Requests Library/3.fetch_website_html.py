import requests


# Fetch website HTML 

# url = 'https://api.github.com'
url = 'https://httpbin.org'

try:
    
    response = requests.get(url)
    
    response.raise_for_status()
    
    website_html = response.text
    
    # print(website_html[:500])
    file_path = r'C:\Users\LENOVO\Desktop\Practice set\python-practice-programs\11 Python Library\9 Requests Library\index.html'
    with open (file_path, 'w', encoding='utf-8') as file:
        file.write(website_html)
        
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
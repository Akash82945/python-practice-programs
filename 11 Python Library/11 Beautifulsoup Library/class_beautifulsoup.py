import requests
from bs4 import BeautifulSoup

# url = 'https://example.com'
# try:
#     response = requests.get(url)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.title.text)

# except requests.exceptions.RequestException as e:
#     print(f'Error : {e}')




# url = 'https://example.com'

# try:
    
#     response = requests.get(url)
#     response.raise_for_status()
    
#     soup = BeautifulSoup(response.text, 'html.parser')

#     links = soup.find_all('a')
#     for link in links:
#         print(link.get('href'))
        
# except requests.exceptions.RequestException as e:
#     print(f'Error : {e}')





html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
</body>
</html>
"""


url = html_doc

soup = BeautifulSoup(html_doc, 'html.parser')
    
print(soup)
    
title = soup.title.text
print(title)
    
link_two = soup.find(id = 'link2')
if link_two:
    print(link_two.get('href'))
else:
    print('ID link2 not found')
    
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
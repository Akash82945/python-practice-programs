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




# The warm up questions
# html_doc = """
# <html>
# <head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
    
# print(soup)
    
# title = soup.title.text
# print(title)
    
# link_two = soup.find(id = 'link2')
# if link_two:
#     print(link_two.get('href'))
# else:
#     print('ID link2 not found')
    
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))







# Scraping a fake online boolstore
# url = 'https://books.toscrape.com/'

# try:
#     response = requests.get(url)
#     response.raise_for_status()
    
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup)
    
#     all_books = soup.find_all('article', class_='product_pod')
#     print(f"All find books no : {len(all_books)}")
    
#     for books in all_books:
#         title_tag = books.h3.a
#         full_title = title_tag.get('title')
        
#         price = books.find('p',class_ = 'price_color').text
#         avibility = books.find('p', class_='instock availability').text.strip()
        
#         print(f'''
#     Title : {full_title}
#     Price : {price}
#     Status : {avibility}
#               ''')
    
# except requests.exceptions.RequestException as e:
#     print(f'Error : {e}')










job_html = """
<div id="job-board">
    <div class="job-card featured" data-id="101">
        <h2 class="title">Senior Python Developer</h2>
        <span class="company">TechCorp</span>
        <span class="location">Remote</span>
        <p class="salary">$120,000 - $140,000</p>
    </div>
    <div class="job-card" data-id="102">
        <h2 class="title">Data Analyst</h2>
        <span class="company">DataInc</span>
        <span class="location">New York, NY</span>
        <p class="salary">$85,000 - $95,000</p>
    </div>
    <div class="job-card featured" data-id="103">
        <h2 class="title">DevOps Engineer</h2>
        <span class="company">CloudScale</span>
        <span class="location">Remote</span>
        <p class="salary">$130,000 - $150,000</p>
    </div>
</div>
"""

soup = BeautifulSoup(job_html, 'html.parser')
featured_job = soup.find_all('div', class_='featured')
for job in featured_job:
    title = job.find('h2', class_='title').text
    
    job_id = job.get('data-id')
    
    print(f"Featured Job : {title} | Data ID : {job_id}")
    

remote_jobs_list = []

all_jobs = soup.find_all('div', class_='job-card')
for job in all_jobs:
    location = job.find('span', class_='location').text
    
    if location == 'Remote':
        title = job.find('h2', class_='title').text
        company = job.find('span', class_='company').text
        
        job_dict = {
            'Title' : title,
            'Company' : company
        }
        
        remote_jobs_list.append(job_dict)
    
print(remote_jobs_list)
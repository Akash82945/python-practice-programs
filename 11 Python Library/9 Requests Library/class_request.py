import requests


# First internet request
# response = requests.get("https://api.github.com")
# print(response)



# response = requests.get("https://api.github.com")
# print(response.text)


# url = "https://api.github.com/users/Akash82945"

# try:
#     response = requests.get(url)
#     response.raise_for_status()
    
#     data = response.json()
    
    
#     print('Github profil details')
#     print(f'''
#           Name : {data.get('name')}
#           Bio : {data.get('bio')}
#           Location : {data.get('location')}
#           Repos : {data.get('public_repos')}
#           ''')
    
#     repo_url = data.get('repos_url')
    
#     repo_response = requests.get(repo_url)
#     repo_response.raise_for_status()
    
#     repo_list = repo_response.json()
    
#     for idx,repo in enumerate(repo_list, start=1):
#         name = repo.get('name')
#         lang = repo.get('language') or 'Unknown'
#         print(f'{idx} : {name} [Language {lang}]')
    
# except requests.exceptions.RequestException as e:
#     print(f'Error: {e}')




url = "https://api.github.com/users/Akash82945"
response = requests.get(url)
data = response.json()
print(data)
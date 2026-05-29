# import requests


# First internet request
# response = requests.get("https://api.github.com")
# print(response)




# Get all HTML of this link
# response = requests.get("https://api.github.com")
# print(response.text)





# Get All deatils of user with HTML and py Dict
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





# Get Json format data
# url = "https://api.github.com/users/Akash82945"
# response = requests.get(url)
# data = response.json()
# print(data)







# # University Student Data
# import requests
# import json

# domain = "https://universities.hipolabs.com"
# end_point = '/search?country=india'

# url = f"{domain}{end_point}"

# try:
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#     data = response.json()
#     print(json.dumps(data[:5], indent=4))
# except requests.exceptions.RequestException as e:
#     print(f"Error {e}")





# Weather Api
import requests
import json
url = 'https://api.open-meteo.com/v1/forecast'

query_params = {
    'latitude': 28.6129,
    'longitude': 77.2390,
    'current_weather':'true'
}

try:
    response = requests.get(url, params=query_params, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data['current_weather'], indent=4))

except requests.exceptions.RequestException as e:
    print(f"error : {e}")
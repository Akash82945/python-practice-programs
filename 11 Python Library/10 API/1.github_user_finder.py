import requests


# User finder

def find_user(username):
    
    url = f'https://api.github.com/users/{username}'
    
    try:
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()

        name = data.get('name')
        bio = data.get('bio')
        followers = data.get('follower')
        location = data.get('location')
        repo = data.get('public_repos')
        
        
        print(f'''
=== Find User Details===
User Name : {name}
Followers : {followers}
Location : {location}
Public Repositry : {repo}
Bio : {bio}
              ''')
        
        
    
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        
user = input('Enter User ID : ')

find_user(user)
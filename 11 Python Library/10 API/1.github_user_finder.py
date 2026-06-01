import requests


# User finder

def find_user(username):
    
    url = f'https://api.github.com/users/{username}'
    
    GITHUB_TOKEN = ""
    
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f"token {GITHUB_TOKEN}"
    
    try:
        
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        
        data = response.json()

        name = data.get('name')
        bio = data.get('bio')
        followers = data.get('followers')
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
        
        
        page = 1
        current_repo_number = 1
        print("=== Repositories List ===")
        while True:
            repos_url = f'https://api.github.com/users/{username}/repos?page={page}&per_page=100'
            
            r = requests.get(repos_url,headers=headers)
            r.raise_for_status()
            
            repo_list = r.json()
            
            if not repo_list:
                break
                
            for rep in repo:
                # print(repo)
                print(f"Repositry: \n{rep.get('name')}")
                current_repo_number += 1
            page += 1
            
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        
user = input('Enter User ID : ')

find_user(user)









# import requests
# import time
# from datetime import datetime

# def check_rate_limit():
#     url = "https://api.github.com/rate_limit"
    
#     try:
#         response = requests.get(url)
#         data = response.json()
        
#         # 'core' एपीआई की जानकारी निकालना
#         core_data = data.get("resources", {}).get("core", {})
        
#         limit = core_data.get("limit")
#         remaining = core_data.get("remaining")
#         reset_timestamp = core_data.get("reset") # Unix timestamp
        
#         # वर्तमान समय (Current time) निकालना
#         current_timestamp = time.time()
        
#         # बाकी बचा समय सेकंड में कैलकुलेट करना
#         seconds_remaining = int(reset_timestamp - current_timestamp)
        
#         print("=== GitHub API Rate Limit Status ===")
#         print(f"Total Limit      : {limit}")
#         print(f"Remaining Requests: {remaining}")
        
#         if seconds_remaining > 0:
#             minutes = seconds_remaining // 60
#             seconds = seconds_remaining % 60
#             print(f"Time Remaining   : {minutes} मिनट और {seconds} सेकंड बाद रीसेट होगा।")
#         else:
#             print("Time Remaining   : आपकी लिमिट रीसेट हो चुकी है! आप कोड चला सकते हैं।")
            
#     except Exception as e:
#         print(f"Error checking rate limit: {e}")

# # फंक्शन को रन करें
# check_rate_limit()

import requests


# Print status code

# url = 'https://api.github.com'
url = "https://api.github.com/users/Akash82945"

try:
    
    response = requests.get(url)
    response.raise_for_status()
    
    print(response)

except requests.exceptions.RequestException as e:
    print(f"Error : {e}")
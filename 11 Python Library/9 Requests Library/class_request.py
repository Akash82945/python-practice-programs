import requests


# First internet request
response = requests.get("https://api.github.com")
print(response)
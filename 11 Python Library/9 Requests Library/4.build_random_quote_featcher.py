# import requests


# # Random quotes generator

# def get_random_quote():

#     url = 'https://dummyjson.com/quotes/random'

#     try:
        
#         response = requests.get(url)
#         response.raise_for_status()
        
#         data = response.json()
        
#         quotes = data.get("quote")
#         author = data.get("author")
        
#         print('=== Random Quotes Generator ===')
#         print(f'\nQuotes : {quotes}')
#         print(f"\nAuthor : {author}")
        
#     except requests.exceptions.RequestException as e:
#         print(f"Error : {e}")
        

# get_random_quote()






from geopy.geocoders import Nominatim

def get_city_coordinates(city_name):
    
    geolocatoer = Nominatim(user_agent = 'my_geo_app_v1')
    
    try:
        location = geolocatoer.geocode(city_name)
        
        if location:
            print(f'=== {city_name.upper()} Details ===')
            print(f'Full add : {location.address}')
            print(f"Latitude : {location.latitude}")
            print(f"Longitude : {location.longitude}")
        else:
            print(f"Error : {city_name} not in database")
            
    except Exception as e:
        print(f"Error : {e}")
        
city = 'Delhi'
get_city_coordinates(city)
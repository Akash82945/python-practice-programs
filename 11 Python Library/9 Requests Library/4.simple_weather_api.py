from geopy.geocoders import Nominatim
import requests

# # Find Location Coordinates (latitude / longitude)

# def get_city_coordinates(city_name):
    
#     geolocatoer = Nominatim(user_agent = 'my_geo_app_v1')
    
#     try:
#         location = geolocatoer.geocode(city_name)
        
#         if location:
#             print(f'=== {city_name.upper()} Details ===')
#             print(f'Full add : {location.address}')
#             print(f"Latitude : {location.latitude}")
#             print(f"Longitude : {location.longitude}")
#         else:
#             print(f"Error : {city_name} not in database")
            
#     except Exception as e:
#         print(f"Error : {e}")
        
        
# city = 'Delhi'
# get_city_coordinates(city)



def get_weather(city_name):
    
    print('=== Weater app===')
    geolocator = Nominatim(user_agent = 'my_geo_app_v1')
    
    try:
        location = geolocator.geocode(city_name)
        
        if not location:
            print(f"Error : {city_name} not found")
            return

        lat = location.latitude
        long = location.longitude
        
        url = f'https://wttr.in/{lat},{long}?format=j1'
        
        response = requests.get(url)
        data = response.json()
        
        # print(data)
        
        current = data['current_condition'][0]
        temp = current['temp_C']
        weather_desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        temp_f = current['temp_F']
        visbl = current['visibility']
        
        print(f"Temprature : {temp}'C")
        print(f"Temprature : {temp_f}'f")
        print(f"Humidity : {humidity}%")
        print(f"Visibility : {visbl}km")
        print(f"How weathe : {weather_desc}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        

city = 'Delhi'
get_weather(city)
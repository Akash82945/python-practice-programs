import requests
from geopy.geocoders import Nominatim     #type: ignore


# Weather App

def get_location(city_name):
    
    geolocater = Nominatim(user_agent = 'my_geo_app_v1')
    
    try:
        
        location = geolocater.geocode(city_name)
        
        long = location.longitude
        lat = location.latitude
        
        if not city_name:
            print(f"Error : {city_name} not found.")
            return
        
        url = f'https://wttr.in/{lat},{long}?format=j1'
        
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        # print(data)
        
        current = data['current_condition'][0]
        wind_mile = current['windspeedMiles']
        cloudcover = current['cloudcover']
        humidity = current['humidity']
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        uv_idx = current['uvIndex']
        observation_time = current['observation_time']
        
        
        print(f'''
              === Weather App ===
              City Name : {city}
              Observation Time : {observation_time}
              Temperature : {temp_c}'C  &  {temp_f}'F
              Cloud cover : {cloudcover}%
              Humidity : {humidity}%
              Wind/Miles : {wind_mile}M/H
              UV Index : {uv_idx}
              ''')
        
        
        print('=== 3-Day weather Prediction ===')
        
        for day in data['weather']:
            date = day['date']
            max_temp = day['maxtempC']
            min_temp = day['mintempC']
            
            weather_desc = day['hourly'][4]['weatherDesc'][0]['value']
            
            print(f"""
                Date : {date}
                Max Temperature : {max_temp}'C
                Min Temperature : {min_temp} 'C
                Condition : {weather_desc}
                  """)
        
        
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        
        
city = 'Amritsar'
get_location(city)
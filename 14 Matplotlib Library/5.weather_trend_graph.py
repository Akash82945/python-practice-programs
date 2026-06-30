import pandas as pd
import matplotlib.pyplot as plt
import requests

url = 'https://api.open-meteo.com/v1/forecast'

params = {
    'latitude': 48.8566,      
    'longitude': 2.3522,
    'hourly': 'temperature_2m',
    'forecast_days': 1        
}

headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, params=params, headers=headers)
data_json = response.json()


# df_api = pd.read_json(url)

hourly_data = {
    'Time' : pd.to_datetime(data_json['hourly']['time']),
    'Temperature' : data_json['hourly']['temperature_2m']

}


df = pd.DataFrame(hourly_data).set_index('Time')

plt.figure(figsize=(10,5))
plt.plot(df.index, df['Temperature'], color='red', marker='o', markersize=4, linewidth=2)
plt.grid(True)
plt.title("Weather Temperature Trend Hourly")
plt.xlabel("Hours")
plt.ylabel('Temperature')
plt.tight_layout()
plt.xticks(rotation=30)
plt.show()


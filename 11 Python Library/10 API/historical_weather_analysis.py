import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://archive-api.open-meteo.com/v1/archive'
params = {
    'latitude' : 31.63,
    'longitude' : 74.87,
    'start_date' : '2026-01-01',
    'end_date' : '2026-01-31',
    'daily' : 'temperature_2m_max,temperature_2m_min',
    'timezone' : 'auto'
}

try:
    
    response = requests.get(url,params=params)
    response.raise_for_status()
    
    data = response.json()
    
    daily_data = data['daily']
    
    df = pd.DataFrame({
        'Date' : daily_data['time'],
        'Max_Temp' : daily_data['temperature_2m_max'],
        'Min_Temp' : daily_data['temperature_2m_min']
    })
    
    print(df.head())
    
    plt.figure(figsize=(10,5))
    
    plt.plot(df['Date'], df['Max_Temp'], label = 'Max Temp (C)', color = 'red', marker='o')
    plt.plot(df['Date'], df['Min_Temp'], label = 'Min Temp (C)', color = 'blue', marker='o')
    
    plt.title("Amritsar Weather Analysis - January 2026")
    plt.xlabel('Dates')
    plt.ylabel("Temperature('C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
                                                    
except requests.exceptions.RequestException as e:
    print(f'error : {e}')
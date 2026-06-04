import requests


# Crypto Currency Price Checker

def cryptocurrancy_price():
    
    url = 'https://api.coingecko.com/api/v3/simple/price'
    
    params = {
        'ids' : 'bitcoin,ethereum,ripple,solana',
        'vs_currencies' : 'usd,inr',
        'include_24hr_change' : 'true'
    }
    
    try:
        
        response = requests.get(url,params=params)
        response.raise_for_status()
        
        data = response.json()
        
        print('=== Live Crypto Currency Price Tracker ===')
        
        crypto_coins = [
            ('Bitcoin','bitcoin'),
            ('Ethereum','ethereum'),
            ('Ripple','ripple'),
            ('Solana','solana')
        ]
        
        for name,coin_id in crypto_coins:
            coin_data = data[coin_id]
            usd_price = coin_data['usd']
            inr_price = coin_data['inr']
            change_24h = coin_data['usd_24h_change']
            
            print(f'''
Coin Name : {name}
Prise (USD) : {usd_price}
Prise (INR) : {inr_price}
24h Change : {change_24h:.2f}%
                  ''')
            
            
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
        

cryptocurrancy_price()
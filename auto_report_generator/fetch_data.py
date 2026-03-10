import requests
from config import URL,TIMEOUT
import logging
def get_cripto_price():
    url = URL
    
    logging.info(f"get the url {url}")
    
    params = {
        "ids": "ethereum,bitcoin,solana",
        "vs_currencies": "usd"
    }
    
    try:
        response = requests.get(url, params=params,timeout=TIMEOUT)
        logging.info(f"get the response {response}")
        
        if response.status_code == 200:
            data = response.json()
            logging.info(f"get the data {data}")
            return data
        else:
            logging.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
        
    
    
    
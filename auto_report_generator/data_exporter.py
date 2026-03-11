import pandas as pd
import logging

def export_to_csv(data, FILE_PATH):
    try:
        row =[]
        for coin , price in data.items():
            row.append([coin,price['usd']])
        
        df = pd.DataFrame(row)
        df.to_csv(FILE_PATH,index=False)
        logging.info(f"Data exported to {FILE_PATH}")
        
    except Exception as e:
        logging.error(f"Error exporting data: {e}")

from fetch_data import get_cripto_price
from report_generator import generate_report
from logger import initilize_logger
from data_exporter import export_to_csv
import logging
import argparse
from config import FILE_PATH

def main():        
    initilize_logger()
    parser = argparse.ArgumentParser(description="Auto Report Generator")
    parser.add_argument(
        "--coins",
        type=str,
        default="ethereum,bitcoin,solana",
        help="Comma-separated list of coins to fetch data for"
    )
    args = parser.parse_args()
    coins = args.coins
    logging.info(f"fetching data for: {coins}")
    
    logging.info("Application started...")
    data = get_cripto_price(coins)
    if not data:
        logging.error("Failed to fetch data. Exiting...")
        return
    export_to_csv(data,FILE_PATH)
    logging.info("Data exported to csv...")
    pdf_file = generate_report(data)
    logging.info("Report generated successfully...")
    print(f"Report generated at {pdf_file}")
    
if __name__ == "__main__":    
    main()
    

    
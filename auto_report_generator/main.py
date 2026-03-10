from fetch_data import get_cripty_price
from report_generator import generate_report
from logger import initilize_logger
import logging

def main():        
    initilize_logger()
    logging.info("Application started...")
    data = get_cripty_price()
    if not data:
        logging.error("Failed to fetch data. Exiting...")
        return
    logging.info("Data fetched successfully...")
    file = generate_report(data)
    logging.info("Report generated successfully...")
    print(f"Report generated at {file}")
    
if __name__ == "__main__":    
    main()
    

    
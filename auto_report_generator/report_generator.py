from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import logging
from config import FILE_NAME
def generate_report(data):
    try:
        filename = FILE_NAME
        
        c = canvas.Canvas(filename, pagesize=letter)
        
        c.setFont("Helvetica", 14)
        c.drawString(200, 750, "Daily Crypto Report")
        c.setFont("Helvetica", 12)
        
        y= 700
        logging.info("Generating report...")
        
        for coin, price in data.items():
            text = f"{coin.upper()}: ${price['usd']}"
            c.drawString(100, y, text)
            y -= 30
            logging.info(f"Added {text}")
        date = datetime.now().strftime("%Y-%m-%d")
        c.drawString(100, y-40, f"Generated on: {date}")
        
        c.save()
        logging.info("Report generated successfully")
        return filename
    except Exception as e:
        logging.error(f"Error generating report: {e}")
        return None
    
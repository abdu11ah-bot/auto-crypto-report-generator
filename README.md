# Auto Report Generator

A Python automation tool that fetches cryptocurrency prices from an API and generates a daily PDF report automatically.

## Features

- Fetches live crypto prices using the CoinGecko API
- Generates a professional PDF report
- Uses logging for tracking application activity
- Modular project structure
- Error handling for API failures

## Technologies Used

- Python
- Requests (API calls)
- ReportLab (PDF generation)
- Logging module

## Project Structure
auto_report_generator
│
├── main.py
├── fetch_data.py
├── report_generator.py
├── logger.py
├── requirements.txt
└── README.md


## Installation

1. Clone the repository:
git clone https://github.com/yourusername/auto-report-generator.git


2. Navigate into the project folder:


cd auto-report-generator


3. Install dependencies:


pip install -r requirements.txt


## Usage

Run the program:


python main.py


The script will:

1. Fetch cryptocurrency prices
2. Generate a daily report
3. Save the report as a PDF file

Example output:


daily_crypto_report.pdf


## Example Report


Daily Crypto Report

Bitcoin: $68,200
Ethereum: $3,800
Solana: $145

Generated on: YYYY-MM-DD


## Future Improvements

- Add CSV export
- Add CLI arguments
- Schedule automatic daily reports
- Add more cryptocurrencies

## License

MIT License

creator : ABDULLAH AL MAMUN 
github : https://github.com/abdu11ah-bot
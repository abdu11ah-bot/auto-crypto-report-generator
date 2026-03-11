# Auto Report Generator

A Python automation tool that fetches cryptocurrency prices from the CoinGecko API and automatically generates structured reports in **CSV** and **PDF** formats.

This project demonstrates **API integration, automation workflows, data processing, CLI tools, and report generation** using Python.

---

## 🚀 Features

* Fetch real-time cryptocurrency prices from the **CoinGecko API**
* Export fetched data to a **CSV file**
* Generate a formatted **PDF report**
* Command-line interface (CLI) for custom coin selection
* Logging system for monitoring application activity
* Modular and maintainable project structure

---

## 🛠 Technologies Used

* **Python**
* **Requests** – API communication
* **Pandas** – Data processing and CSV export
* **ReportLab** – PDF report generation
* **Logging** – Application monitoring
* **Argparse** – Command line interface

---

## 📂 Project Structure

```
auto_report_generator
│
├── main.py               # Application entry point
├── fetch_data.py         # API request logic
├── report_generator.py   # PDF report creation
├── data_exporter.py      # CSV export using pandas
├── logger.py             # Logging configuration
├── util.py               # Constants and configuration
├── requirements.txt      # Project dependencies
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/auto-report-generator.git
```

Navigate to the project directory:

```
cd auto-report-generator
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script with default cryptocurrencies:

```
python main.py
```

Run the script with custom coins:

```
python main.py --coins bitcoin,ethereum,dogecoin
```

---

## 📊 Output

After execution, the program generates:

```
crypto_prices.csv
daily_crypto_report.pdf
```

Example PDF content:

```
Daily Crypto Report

Bitcoin: $68,200
Ethereum: $3,800
Solana: $145

Generated on: YYYY-MM-DD
```

---

## 📌 Example Workflow

1. Fetch cryptocurrency prices from API
2. Process and structure the data
3. Export data to CSV
4. Generate a formatted PDF report
5. Log all operations

---

## 🔮 Future Improvements

* Add historical price analysis
* Generate price trend charts
* Add scheduling for automated daily reports
* Support more financial APIs

---

## 📄 License

This project is open-source and available under the MIT License.

# crypto-portfolio-tracker-with-live-exchange-APIs-
A real-time crypto portfolio tracker built with Python and Flask. Fetches live prices using the CoinGecko API, tracks historical portfolio value, and displays interactive charts in a web dashboard.
Crypto Portfolio Tracker Dashboard

Real-time cryptocurrency portfolio tracker built with Python and Flask. Monitor your crypto holdings, visualize distribution, and track historical portfolio growth—all in a local web dashboard.

🔹 Features

Live Price Updates: Fetches real-time prices for multiple cryptocurrencies using the CoinGecko API
.

Portfolio Visualization: Interactive pie chart showing coin distribution.

Historical Tracking: Logs total portfolio value daily and displays growth as a line chart.

Auto-Refresh: Dashboard updates every 60 seconds automatically.

Local Web Dashboard: Runs on your machine via Flask and Chart.js.

🗂 Project Structure
crypto_portfolio_dashboard/
│── app.py                # Main Flask application
│── portfolio.json        # User's crypto holdings
│── history.csv           # Logs portfolio value over time
│── templates/
│    └── index.html       # Dashboard HTML template
│── requirements.txt      # Python dependencies

⚡ Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/crypto-portfolio-tracker.git
cd crypto-portfolio-tracker

2. Create a Virtual Environment (Recommended)
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Setup Portfolio File

Create portfolio.json with your crypto holdings:

{
  "bitcoin": 0.5,
  "ethereum": 2,
  "cardano": 1000
}

5. Initialize History File (Optional)

Create history.csv with headers:

date,total_value


The app will automatically append daily total portfolio values.

6. Run the App Locally
python app.py


Open your browser at http://127.0.0.1:5000
 to view your dashboard.

📊 Screenshots






📦 Dependencies

Flask
 – Backend framework

Requests
 – For API requests

Chart.js
 – Frontend chart visualization

🛠 Future Enhancements

Connect directly to exchange APIs (Binance, Coinbase) for live balances.

Add authentication for multi-user support.

Use a database (PostgreSQL/SQLite) for persistent storage instead of CSV.

Make the dashboard mobile-responsive.




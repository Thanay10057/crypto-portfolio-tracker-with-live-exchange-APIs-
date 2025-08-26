from flask import Flask, render_template, jsonify
import requests
import json
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Load portfolio
with open("portfolio.json", "r") as f:
    portfolio = json.load(f)

API_URL = "https://api.coingecko.com/api/v3/simple/price"
HISTORY_FILE = "history.csv"

def fetch_prices():
    coins = ",".join(portfolio.keys())
    params = {"ids": coins, "vs_currencies": "usd"}
    response = requests.get(API_URL, params=params)
    return response.json()

def calculate_portfolio(prices):
    portfolio_data = []
    total_value = 0
    for coin, amount in portfolio.items():
        price = prices[coin]["usd"]
        value = price * amount
        total_value += value
        portfolio_data.append({
            "coin": coin.capitalize(),
            "amount": amount,
            "price": price,
            "value": value
        })
    return portfolio_data, total_value

def log_history(total_value):
    today = datetime.today().strftime("%Y-%m-%d")
    exists = os.path.exists(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["date", "total_value"])
        writer.writerow([today, total_value])

def read_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    history = []
    with open(HISTORY_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            history.append({"date": row["date"], "total": float(row["total_value"])})
    return history

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio_data():
    prices = fetch_prices()
    portfolio_data, total_value = calculate_portfolio(prices)

    # Log today’s value if not already logged
    history = read_history()
    if not history or history[-1]["date"] != datetime.today().strftime("%Y-%m-%d"):
        log_history(total_value)

    return jsonify({"portfolio": portfolio_data, "total": total_value})

@app.route("/history")
def history():
    return jsonify(read_history())

if __name__ == "__main__":
    app.run(debug=True)

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Stock Alerts").sheet1  # Open the correct sheet

# Determine if today is Friday
today = datetime.today()
is_friday = today.weekday() == 4

# Define date range for the past week
end_date = today
start_date = end_date - timedelta(days=7)

# List of stocks (you can expand this list or make it dynamic)
stocks = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOGL"]

# Download data for the specified stocks
data = yf.download(stocks, start=start_date if is_friday else end_date, end=end_date)

# Calculate daily or weekly volume
volume = data['Volume'].sum()

# Identify the most bought/sold stocks
most_bought = volume.idxmax()
most_sold = volume.idxmin()

# Update Google Sheet
row = [today.strftime('%Y-%m-%d'), most_bought, most_sold]
sheet.append_row(row)

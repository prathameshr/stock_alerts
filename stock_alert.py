import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set the path for the credentials
creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate with Google Sheets
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Stock Alerts").sheet1

# Example: Append a new row
sheet.append_row(["2024-08-12", "AAPL", "TSLA"])

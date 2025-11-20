# main.py
from bot import send_signal

# Example Signal List
symbols = ["NSE:RELIANCE", "NSE:TCS", "NSE:HDFCBANK"]

for symbol in symbols:
    send_signal(symbol)

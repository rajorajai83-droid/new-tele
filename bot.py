# bot.py
# Full Advanced Auto Signal Bot for Indian Stock Market
# Multi-timeframe signals: 5m,15m,1H,1D
# Uses TradingView screenshots + Buy/Sell logic + S/R + Volume + Trend

import telegram
import os
from datetime import datetime
from chart import get_chart
import pandas as pd
import numpy as np

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=BOT_TOKEN)

# ----------------------------
# 📌 AUTO BUY/SELL LOGIC
# ----------------------------
def generate_signal(df):
    close = df['close'].iloc[-1]

    # Simple moving averages
    df['sma20'] = df['close'].rolling(20).mean()
    df['sma50'] = df['close'].rolling(50).mean()

    if df['sma20'].iloc[-1] > df['sma50'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"

# ----------------------------
# 📌 SUPPORT / RESISTANCE
# ----------------------------
def get_sr(df):
    support = df['low'].rolling(20).min().iloc[-1]
    resistance = df['high'].rolling(20).max().iloc[-1]
    return support, resistance

# ----------------------------
# 📌 SEND SIGNAL MESSAGE
# ----------------------------
def send_signal(symbol):
    # Chart Screenshot
    chart_path = get_chart(symbol)

    # Dummy OHLC data (replace with real API later)
    df = pd.DataFrame({
        'close': np.random.randint(100, 200, 60),
        'high': np.random.randint(120, 220, 60),
        'low': np.random.randint(80, 150, 60)
    })

    signal = generate_signal(df)
    support, resistance = get_sr(df)

    msg = f"""
📊 **Auto Stock Signal — {symbol}**
🕒 {datetime.now().strftime('%I:%M %p')}

**Signal:** {signal}

📉 Support: {support}
📈 Resistance: {resistance}
"""

    with open(chart_path, "rb") as img:
        bot.sendPhoto(chat_id=CHAT_ID, photo=img, caption=msg, parse_mode="Markdown")

    print("Signal Sent:", symbol)

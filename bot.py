# bot.py
import telegram
from chart import get_chart
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")   # Channel username or ID

bot = telegram.Bot(token=BOT_TOKEN)

def send_signal(symbol):
    chart_path = get_chart(symbol)

    caption = f"📈 Signal for {symbol}"
    
    with open(chart_path, "rb") as img:
        bot.sendPhoto(chat_id=CHAT_ID, photo=img, caption=caption)

    print("Signal Sent:", symbol)

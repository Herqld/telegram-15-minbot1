import os, random
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

PHRASES = [
    "Я крутой",
    "Абду крут",
    "Нури соска",
    "Хочу тебя",
    "Нурилашкамды хочу"
]

bot = Bot(token=TOKEN)
scheduler = BlockingScheduler()

def send_message():
    text = random.choice(PHRASES)
    bot.send_message(chat_id=CHANNEL_ID, text=text)
    print("✅", text)

scheduler.add_job(send_message, 'interval', minutes=15)
print("🤖 Бот запущен!")
send_message()
scheduler.start()

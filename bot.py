import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

print("Бот запущений!")
bot.infinity_polling()

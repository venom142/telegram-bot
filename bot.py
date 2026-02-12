import telebot
import os

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_audio(message):
    with open("audio.mp3", "rb") as audio:
        bot.send_audio(message.chat.id, audio)

print("Bot started")
bot.infinity_polling()


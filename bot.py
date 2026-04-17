import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который...')


bot.infinity_polling()
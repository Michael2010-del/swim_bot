import telebot
from config import TOKEN
from logic import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот о плавании.\n\nИспользуй команду /menu, чтобы выбрать стиль.')

@bot.message_handler(commands=['menu'])
def menu(message):
    keyboard = get_main_keyboard()
    bot.send_message(
        message.chat.id,
        "Выбери стиль плавания:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: message.text in ["Кроль", "Брасс", "Баттерфляй", "Спина"])
def style_handler(message):
    answer = get_style_info(message.text)
    bot.send_message(message.chat.id, answer)





if __name__ == "__main__":
    bot.polling()


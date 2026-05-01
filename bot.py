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

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Доступные команды:\n/menu - показать меню\n/info - информация о боте\n/help - помощь')

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, 'Бот о плавании. Версия 1.0\nАвтор: Твой Бот')

@bot.message_handler(func=lambda message: message.text in ["Кроль", "Брасс", "Баттерфляй", "Спина"])
def style_handler(message):
    answer = get_style_info(message.text)
    bot.send_message(message.chat.id, answer)
    # Показываем клавиатуру снова после ответа
    keyboard = get_main_keyboard()
    bot.send_message(message.chat.id, "Выбери другой стиль или нажми /menu:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Совет дня")
def tip_of_day(message):
    tip = get_daily_tip()
    bot.send_message(message.chat.id, tip)

@bot.message_handler(func=lambda message: message.text == "Сравнить стили")
def compare_styles(message):
    comparison = get_styles_comparison()
    bot.send_message(message.chat.id, comparison)

@bot.message_handler(func=lambda message: True)
def unknown_command(message):
    bot.send_message(message.chat.id, "Я не понимаю эту команду.\nИспользуй /menu для выбора стиля.")

if __name__ == "__main__":
    print("Бот запущен")
    bot.polling()
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

styles = {
    "Кроль": " Кроль:\nДыши на 3-й гребок. Руки не скрещивай.",
    "Брасс": " Брасс:\nТолчок ногами — сила. Дыши на каждый гребок.",
    "Баттерфляй": " Баттерфляй:\nДва удара ногами — один гребок. Волна всем телом.",
    "Спина": " Спина:\nЛицо вверх. Мизинец входит первым."
}

def get_main_keyboard():
    """Клавиатура из ключей словаря"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(text) for text in styles.keys()]
    keyboard.add(*buttons)  
    return keyboard

def get_style_info(style_name):
    return styles.get(style_name, "Не знаю такой стиль")
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

styles = {
    "Кроль": " Кроль:\n• Дыши на 3-й гребок\n• Руки не скрещивай\n• Ноги работают как ласты\n• Самый быстрый стиль",
    "Брасс": " Брасс:\n• Толчок ногами — сила\n• Дыши на каждый гребок\n• Руки двигаются синхронно\n• Лягушачий стиль",
    "Баттерфляй": " Баттерфляй:\n• Два удара ногами — один гребок\n• Волна всем телом\n• Самый сложный стиль\n• Требует много силы",
    "Спина": " Спина:\n• Лицо вверх\n• Мизинец входит первым\n• Руки прямые\n• Легко дышать"
}

tips = [
    "Не забывай разминаться перед заплывом",
    "Пей воду даже во время плавания",
    "Следи за техникой дыхания",
    "Отдыхай между заплывами",
    "Используй очки для плавания",
    "Шапочка защищает волосы от хлора"
]

def get_main_keyboard():
    """Клавиатура из ключей словаря"""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(text) for text in styles.keys()]
    
    # Добавляем дополнительные кнопки
    buttons.append(KeyboardButton("Совет дня"))
    buttons.append(KeyboardButton("Сравнить стили"))
    
    # Располагаем кнопки по 2 в ряд
    keyboard.add(buttons[0], buttons[1])
    keyboard.add(buttons[2], buttons[3])
    keyboard.add(buttons[4], buttons[5])
    
    return keyboard

def get_style_info(style_name):
    return styles.get(style_name, "Не знаю такой стиль")

def get_daily_tip():
    """Возвращает случайный совет"""
    return f" Совет дня:\n{random.choice(tips)}"

def get_styles_comparison():
    """Сравнение стилей"""
    comparison = """ Сравнение стилей:

 Кроль - самый быстрый
 Брасс - самый популярный
 Баттерфляй - самый сложный
 Спина - самый расслабляющий

Скорость (от 1 до 5):
Кроль: ⭐⭐⭐⭐⭐
Баттерфляй: ⭐⭐⭐⭐
Брасс: ⭐⭐⭐
Спина: ⭐⭐"""
    
    return comparison
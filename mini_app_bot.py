import telebot
from telebot import types

TOKEN = "8155851862:AAE6j861KuE4mobeVEUs_Z48Lpnn2eJVwFI"
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Выбери действие:", reply_markup=main_menu())

# Основное меню с кнопками
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Угадай число 🎲")
    btn2 = types.KeyboardButton("Погода ☀️")
    btn3 = types.KeyboardButton("Привет 👋")
    btn4 = types.KeyboardButton("Помощь ❓")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# Обработка кнопок
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Угадай число 🎲":
        bot.send_message(message.chat.id, "Я загадал число от 1 до 5. Попробуй угадать!")
    elif message.text == "Погода ☀️":
        bot.send_message(message.chat.id, "Сейчас солнечно и тепло! 🌤️")
    elif message.text == "Привет 👋":
        bot.send_message(message.chat.id, "Привет! Рад тебя видеть 😊")
    elif message.text == "Помощь ❓":
        bot.send_message(message.chat.id, "Выбери одну из кнопок, и я покажу, что умею!")
    else:
        bot.send_message(message.chat.id, "Нажми на одну из кнопок ниже", reply_markup=main_menu())

# Запуск бота
bot.polling()

import telebot
from telebot import types

from config import TOKEN


bot = telebot.TeleBot(TOKEN)


def menu():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "🤖 AI Помощник",
        "🎮 Хостинг"
    )

    keyboard.add(
        "🛡 Модерация",
        "💰 Магазин"
    )

    return keyboard


@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id,
        """
🚀 PulSar AI Assistant

Ваш универсальный помощник.

Выберите раздел:
        """,
        reply_markup=menu()
    )


@bot.message_handler(func=lambda message: True)
def message_handler(message):

    text = message.text


    if text == "🤖 AI Помощник":

        bot.send_message(
            message.chat.id,
            "🧠 AI режим включён.\nЗадайте свой вопрос."
        )


    elif text == "🎮 Хостинг":

        bot.send_message(
            message.chat.id,
            "🎮 Раздел игрового хостинга.\n"
            "Помощь с серверами и настройками."
        )


    elif text == "🛡 Модерация":

        bot.send_message(
            message.chat.id,
            "🛡 Модерация включена."
        )


    elif text == "💰 Магазин":

        bot.send_message(
            message.chat.id,
            "💰 Магазин услуг PulSar."
        )


    else:

        bot.send_message(
            message.chat.id,
            "🤖 Я получил сообщение:\n" + text
        )


print("🚀 PulSar AI Assistant запущен")

bot.infinity_polling()

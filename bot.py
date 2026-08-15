import telebot
from telebot import types

from config import TOKEN
from database import setup, add_user, add_message


bot = telebot.TeleBot(TOKEN)


setup()


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

    add_user(
        message.from_user.id,
        message.from_user.username
    )

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

    add_message(
        message.from_user.id
    )

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
            "🛡 Раздел модерации.\n"
            "Защита групп и управление."
        )


    elif text == "💰 Магазин":

        bot.send_message(
            message.chat.id,
            "💰 Магазин PulSar.\n"
            "Услуги и предложения."
        )


    else:

        bot.send_message(
            message.chat.id,
            "🤖 Я получил сообщение:\n" + text
        )


print("🚀 PulSar AI Assistant запущен")


bot.infinity_polling()

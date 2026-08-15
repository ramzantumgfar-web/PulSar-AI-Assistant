import telebot
from telebot import types

from config import TOKEN, ADMIN_ID
from database import (
    setup,
    add_user,
    add_message,
    add_balance,
    get_balance
)

from ai import ask_ai


bot = telebot.TeleBot(TOKEN)


setup()


def menu():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row(
        "🤖 AI Помощник",
        "🎮 Хостинг"
    )

    keyboard.row(
        "📊 Статус серверов",
        "🛠 Поддержка"
    )

    keyboard.row(
        "💰 Баланс",
        "👤 Профиль"
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
🚀 PulSar Host AI

Добро пожаловать!

Я AI-помощник игрового хостинга PulSar.

Выберите раздел 👇
        """,
        reply_markup=menu()
    )



# Баланс
@bot.message_handler(commands=["balance"])
def balance(message):

    money = get_balance(
        message.from_user.id
    )


    bot.send_message(
        message.chat.id,
        f"💰 Ваш баланс: {money}₽"
    )



# Админ пополнение баланса
@bot.message_handler(commands=["addbalance"])
def add_money(message):

    if message.from_user.id != ADMIN_ID:
        bot.send_message(
            message.chat.id,
            "❌ Нет доступа"
        )
        return


    args = message.text.split()


    if len(args) != 3:

        bot.send_message(
            message.chat.id,
            """
Использование:

/addbalance ID СУММА

Пример:
/addbalance 123456 500
            """
        )

        return


    user_id = int(args[1])
    amount = int(args[2])


    add_balance(
        user_id,
        amount
    )


    bot.send_message(
        message.chat.id,
        "✅ Баланс успешно пополнен"
    )



# Админ панель
@bot.message_handler(commands=["admin"])
def admin(message):

    if message.from_user.id != ADMIN_ID:
        return


    bot.send_message(
        message.chat.id,
        """
👑 Админ панель PulSar

Команды:

/addbalance ID СУММА
/balance

Управление пользователями доступно.
        """
    )



@bot.message_handler(func=lambda message: True)
def handler(message):

    user_id = message.from_user.id

    text = message.text


    add_message(user_id)



    if text == "🤖 AI Помощник":

        bot.send_message(
            message.chat.id,
            """
🤖 AI включён.

Напишите вопрос:
            """
        )



    elif text == "🎮 Хостинг":

        bot.send_message(
            message.chat.id,
            """
🎮 PulSar Host

Доступно:

🖥 Игровые серверы
⚡ Быстрые SSD
🛡 Защита
📈 Мониторинг
            """
        )



    elif text == "📊 Статус серверов":

        bot.send_message(
            message.chat.id,
            """
📊 Статус:

🟢 Telegram Bot
🟢 AI System
🟢 Database

Все системы работают.
            """
        )



    elif text == "🛠 Поддержка":

        bot.send_message(
            message.chat.id,
            """
🛠 Поддержка

Опишите проблему.
Администратор поможет.
            """
        )



    elif text == "💰 Баланс":

        money = get_balance(user_id)

        bot.send_message(
            message.chat.id,
            f"💰 Ваш баланс: {money}₽"
        )



    elif text == "👤 Профиль":

        money = get_balance(user_id)

        bot.send_message(
            message.chat.id,
            f"""
👤 Профиль

ID: {user_id}
Username: @{message.from_user.username}

💰 Баланс: {money}₽
            """
        )



    else:

        try:

            bot.send_chat_action(
                message.chat.id,
                "typing"
            )


            answer = ask_ai(
                user_id,
                text
            )


            bot.send_message(
                message.chat.id,
                answer
            )


        except Exception:

            bot.send_message(
                message.chat.id,
                "⚠️ AI временно недоступен"
            )



print("🚀 PulSar Host Bot запущен")


bot.infinity_polling()

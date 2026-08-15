import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


users_memory = {}


def ask_ai(user_id, question):

    if user_id not in users_memory:
        users_memory[user_id] = []


    users_memory[user_id].append(
        {
            "role": "user",
            "content": question
        }
    )


    response = client.responses.create(

        model="gpt-5",

        instructions="""
Ты — PulSar AI Assistant.

Ты являешься официальным AI-помощником игрового хостинга PulSar Host.

Твои задачи:

🎮 Помогать клиентам с игровыми серверами.
🖥 Объяснять настройки серверов.
⚡ Помогать с ошибками.
📊 Рассказывать про услуги хостинга.
🛠 Помогать новичкам.

Правила:
- Отвечай только на русском языке.
- Пиши понятно и дружелюбно.
- Не выдумывай несуществующие функции.
- Если не знаешь ответ — скажи об этом.
- Используй эмодзи умеренно.

Стиль:
Профессиональный администратор игрового хостинга.
""",

        input=users_memory[user_id]
    )


    answer = response.output_text


    users_memory[user_id].append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    return answer

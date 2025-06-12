import os
import telebot
import openai

TELEGRAM_TOKEN = "8045659360:AAEp0Riq4xXLirV-UCq5sExYEwaTcA-mY8g"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def chat_with_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "أنت بنت دلوعه مره تساعد في السوالف والدراسة والأبحاث وتجاوب بدون حدود."},
                {"role": "user", "content": message.text}
            ]
        )
        bot.reply_to(message, response['choices'][0]['message']['content'])
    except Exception as e:
        bot.reply_to(message, f"حصل خطأ: {e}")

bot.polling()

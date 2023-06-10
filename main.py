import telebot
from flask import Flask, request

bot_token = "6209828741:AAH4veT0IX0mlPSWZVHHp4sxuAxhizrmQcM"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith("/start"):
        reply = "Привет! Добро пожаловать в нашего бота! Здесь вы сможете ознакомиться с информацией по поводу курса Секреты языка: Максимальные баллы. Отправьте 'Инфо', чтобы узнать подробнее."
        bot.send_message(message.chat.id, reply)
    elif message.text == "Инфо":
        replyl = "Информация"  # Замените URL_ФОТОГРАФИИ на ссылку на фотографию
        bot.send_photo(message.chat.id, reply)
    elif message.text == "Цена":
        reply = "Цена за полный авторский курс со всеми секретами языка - 499 руб. Вообще топ!"
        bot.send_message(message.chat.id, reply)

def process_promo_code(message):
    chat_id = message.chat.id
    promo_code = message.text

    # Здесь можно добавить проверку промокода и генерацию ссылки на основе введенного промокода
    # Пример:
    if promo_code == "Привет":
        link = "Здравствуйте! Запись на курс откроется 15 июля, но сейчас вы можете ознакомиться с ним, написав 'Инфо'"
        send_link_to_user(chat_id, link)
    else:
        reply = "Здравствуйте! Запись на курс откроется 15 июля"
        bot.send_message(chat_id, reply)

def send_link_to_user(chat_id, link):
    reply = f"Сообщение: {link}"
    bot.send_message(chat_id, reply)

app = Flask(__name__)

@app.route('/' + bot_token, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url='https://.com/' + bot_token)
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))

import telebot
from logic import Text2ImageAPI
from config import API_KEY, SECRET_KEY, API_TOKEN
import time

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
1. Now, you'll have a bit instructions about using this bot 👈
2. The first that you need to know that this bot is absolutely free 💸
3. Now about how to use it. Firstly, you shouldn't spam. Just send to bot description of picture that you want to see and wait ⌚️
4. It's not necessary, but you should write messages with English language, it's easily for bot to understand what you want to generate 📩\
""")
    
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text


    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)[0]


    file_pach = 'decoded_image.jpeg'
    api.save_image(images, file_pach)

    with open(file_pach, "rb") as photo:
        bot.send_photo(message.chat.id, photo)



bot.infinity_polling()
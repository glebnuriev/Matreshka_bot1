import telebot
from config import API_TOKEN
import time


bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Hi, welcome to the bot, if you don't know how to use it, write /help
\
""")
    

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
1. Now, you'll have a bit instructions about using this bot 👈
                 
2. In this bot you can know a lot of information!👌
                 
3. Bot has prices of different currencies, weather in your region and interesting facts, it has photo generation and text generation!🤩
                 
4. To use all of those things, you should write /bots here and click on a bot that you need, you'll also have instructions📄
                 
5. I hope you enjoy using those bots, have a good day🤗
\
""")
    
    

@bot.message_handler(commands=['bots'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
1. @GoldenlolBot - Сurrency bot 👈
                 
2.  - Weather bot 👌
                 
3. @smallbot318_bot - Photo Bot 🤩
                 
4. None - Saving Bot📄
                 
5. I hope you enjoy using those bots, have a good day🤗
\
""")

    
bot.infinity_polling()
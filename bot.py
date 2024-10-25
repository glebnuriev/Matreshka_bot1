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

@bot.message_handler(commands=['help_currency'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
    Hi! It's list of this bot currencies!

    1. Dollar - /dollar_price (USA, UK, others...)
    
    2. BYN - /byn_price - Belarus

    3. AMD - /amd_price - Armenia

    4. BGN - /bgn_price - Bulgaria

    5. BRL - /brl_price - Brazil

    6. KZT - /kzt_price - Kazakhstan

    7. CNY - /cny_price - China

    More soon!...
\
""")

@bot.message_handler(commands=['list_of_currencies'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Hi, welcome to the bot, if you don't know how to use it, write /help
\
""")

# ------------> PRICES <-------------
@bot.message_handler(commands=['dollar_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://www.bloomberg.com/quote/USDRUB:CUR" you can see dollar price, if you want to know some more info about dollar write /dollar
\
""")

# @bot.message_handler(commands=['ethereum_price'])
# def send_welcome(message):
#     bot.send_chat_action(message.chat.id, 'typing')
#     time.sleep(2)
#     bot.reply_to(message, """\
# Okay, here - "https://2bitcoins.ru/coins/ethereum/ " you can see ethereum price, if you want to know some more info about ethereum write /ethereum
# \
# """)
    
# @bot.message_handler(commands=['bitcoin_price'])
# def send_welcome(message):
#     bot.send_chat_action(message.chat.id, 'typing')
#     time.sleep(2)
#     bot.reply_to(message, """\
# Okay, here - "https://2bitcoins.ru/coins/bitcoin/" you can see bitcoin price, if you want to know some more info about bitcoin write /bitcoin
# \
# """)

@bot.message_handler(commands=['byn_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://finance.rambler.ru/currencies/BYN/" you can see byn price, if you want to know some more info about byn write /byn
\
""")

@bot.message_handler(commands=['amd_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://finance.rambler.ru/calculators/converter/1-AMD-RUB/" you can see amd price, if you want to know some more info about amd write /amd
\
""")

@bot.message_handler(commands=['bgn_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://finance.rambler.ru/calculators/converter/1-BGN-RUB/" you can see bgn price, if you want to know some more info about bgn write /bgn
\
""")

@bot.message_handler(commands=['brl_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://finance.rambler.ru/calculators/converter/1-BRL-RUB/" you can see brl price, if you want to know some more info about brl write /brl
\
""")


@bot.message_handler(commands=['kzt_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://finance.rambler.ru/calculators/converter/1-KZT-RUB/" you can see kzt price, if you want to know some more info about kzt write /kzt
\
""")

@bot.message_handler(commands=['cny_price'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Okay, here - "https://finance.rambler.ru/calculators/converter/1-CNY-RUB/" you can see cny price, if you want to know some more info about cny write /cny
\
""")

# information

@bot.message_handler(commands=['dollar'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
До́ллар Соединённых Штатов Америки (англ. United States dollar) — денежная единица США, одна из основных резервных валют мира. 1 доллар = 100 центов. Символьное обозначение в англоязычных текстах: $; в США для замены слова «доллар» знак используется в препозиции, то есть перед числом. Буквенный код валюты: USD.
\
""")

# @bot.message_handler(commands=['ethereum'])
# def send_welcome(message):
#     bot.send_chat_action(message.chat.id, 'typing')
#     time.sleep(2)
#     bot.reply_to(message, """\
# Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна (децентрализованных приложений), работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина. Концепт был предложен Виталиком Бутериным в конце 2013 года, сеть была запущена 30 июля 2015 года.
# \
# """)

# @bot.message_handler(commands=['bitcoin'])
# def send_welcome(message):
#     bot.send_chat_action(message.chat.id, 'typing')
#     time.sleep(2)
#     bot.reply_to(message, """\
# Битко́йн, или битко́ин (от англ. Bitcoin, от bit — бит и coin — монета) — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.
# \
# """)

@bot.message_handler(commands=['byn'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Белору́сский рубль (бел. Беларускі рубель) — законное платёжное средство Белоруссии. Буквенный код ISO 4217 — BYN, цифровой — 933, официальный символ — Br.

В обращении находятся банкноты номиналом 5, 10, 20, 50, 100, 200 и 500 рублей, а также монеты номиналом 1, 2, 5, 10, 20 и 50 копеек, 1 и 2 рубля.
\
""")

@bot.message_handler(commands=['amd'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Драм (арм. դրամ) — денежная единица Армении. Буквенный код ISO 4217 — AMD, цифровой — 051, официальный символ — ֏: перечёркнутая двумя горизонтальными линиями заглавная буква Դ (название буквы: «да»), графика (вид) которой имеется лишь в армянском алфавите и с которой начинается слово «Դրամ» («Драм»). Правом денежной эмиссии обладает Центральный банк Республики Армения.
\
""")

@bot.message_handler(commands=['bgn'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Лев, устар. лёв (болг. лев) — денежная единица Болгарии, содержит 100 стотинок. Код ISO 4217 — BGN.
\
""")

@bot.message_handler(commands=['brl'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Реа́л (порт. real, код ISO 4217: BRL, символ: R$, множественное число: réis (до 1942), reais (с 1994)) — денежная единица Бразилии. Делится на 100 сентаво[2][3]. Является относительно новой валютой. Появлению реала в 1994 году[4] предшествовал период гиперинфляции. С 1942 по 1994 годы в Бразилии национальные валюты обесценивались 7 раз[5][6][7][8][9][10]. За время своего существования курс реала к доллару колебался от 0,8 до 3,7 реалов за $1. С 2009 по 2011 годы курс колебался от 1,5 до 1,7 реалов за $1.
\
""")

@bot.message_handler(commands=['kzt'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Казахста́нский тенге́ (каз. Қазақстан теңгесі, Qazaqstan teñgesi; м. р., нескл.) — денежная единица Казахстана. Введена в обращение 15—16 ноября 1993 года. Буквенный код ISO 4217 — KZT, цифровой — 398, официальный символ — ₸. Один тенге равен 100 тиынам.
\
""")

@bot.message_handler(commands=['cny'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
Юа́нь (кит. трад. 圓, упр. 元, пиньинь Yuán) — современная валюта Китайской Народной Республики, в которой измеряется стоимость жэньминьби (кит. упр. 人民币, пиньинь rénmínbì, палл. жэньминьби, буквально: «народные деньги», сокращённо RMB). Входит в «корзину» специальных прав заимствования МВФ[2]. Международное обозначение валюты в стандарте ISO 4217 — CNY.
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

6. To see list of currencies, /help_currency
                 
5. I hope you enjoy using those bots, have a good day🤗
\
""")


# ---------> starting <---------  
bot.infinity_polling()
import telebot
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
3. Now about how to use it. Firstly, you shouldn't spam. You can broke the bot⌚️
4. It's not necessary, but you should write messages with English language, all commands are English 📩\
5. list of available cities, /list <----- 
""")


@bot.message_handler(commands=['list'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """\
    Here you can see list of cities those aviable in bot!
    
    1. Saint Petersburg, weather - /saint_petersburg , info - /stp_facts
    
    2. Moscow, weather - /moscow , info - /msk_facts
    
    3. Kazan, weather - /kazan , info - /kazan_facts
    
    4. Kaliningrad, weather - /kaliningrad , info - /stp_facts
    
    5. Nizhny_Novgorod, weather - /nizhny_novgorod , info - /nnv_facts
    
    6. Arkhangelsk, weather - /arkhangelsk , info - /ark_facts
                 
    7. Suzdal, weather - /suzdal , info - /suz_facts
                 
    More soon...
""") 
# -----> weather <----- 
@bot.message_handler(commands=['saint_petersburg'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in Saint Petersburg ---> \https://www.gismeteo.ru/weather-sankt-peterburg-4079/, if you want to know more, write - /stp_facts""")


@bot.message_handler(commands=['moscow'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in Moscow ---> https://www.gismeteo.ru/weather-moscow-4368/10-days/, if you want to know more, write - /msk_facts """)


@bot.message_handler(commands=['kazan'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in Kazan ---> https://www.gismeteo.ru/weather-kazan-4364/, if you want to know more, write - /kazan_facts """)


@bot.message_handler(commands=['kaliningrad'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in Kaliningrad ---> https://www.gismeteo.ru/weather-kaliningrad-4225/10-days/, if you want to know more, write - /kng_facts """)


@bot.message_handler(commands=['nizhny_novgorod'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in nizhny_novgorod ---> https://www.gismeteo.ru/weather-nizhny-novgorod-4355/10-days/, if you want to know more, write - /nnv_facts """)
    
@bot.message_handler(commands=['arkhangelsk'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in Arkhangelsk ---> https://www.gismeteo.ru/weather-arkhangelsk-3915/10-days/, if you want to know more, write - /ark_facts """)

@bot.message_handler(commands=['suzdal'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Here you can see weather in Suzdal --->https://www.gismeteo.ru/weather-suzdal-11633/10-days/, if you want to know more, write - /suz_facts""")

# -----> facts <-----

@bot.message_handler(commands=['stp_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Saint Petersburg, formerly known as Petrograd and later Leningrad, is the second-largest city in Russia after Moscow. It is situated on the River Neva, at the head of the Gulf of Finland on the Baltic Sea. The city had a population of 5,601,911 residents as of 2021, with more than 6.4 million people living in the metropolitan area. Saint Petersburg is the fourth-most populous city in Europe, the most populous city on the Baltic Sea, and the world's northernmost city of more than 1 million residents. As the former capital of Imperial Russia, and a historically strategic port, it is governed as a federal city.""")

@bot.message_handler(commands=['msk_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Москва является столицей и крупнейшим городом России . Город стоит на реке Москве в Центральной России , с населением более 13 миллионов жителей в пределах города, более 18,8 миллионов жителей в городской местности, и более 21,5 миллионов жителей в его столичной области. Город занимает площадь 2511 квадратных километров (970 квадратных миль), в то время как городская территория занимает 5891 квадратный километр (2275 квадратных миль), [ 7 ] а столичная область занимает более 26 000 квадратных километров (10 000 квадратных миль). Москва является одним из крупнейших городов мира , являясь самым густонаселенным городом в Европе, крупнейшей городской и столичной территорией в Европе, и крупнейшим городом по площади на европейском континенте.

""")
    
@bot.message_handler(commands=['kazan_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Kazan is the largest city and capital of Tatarstan, Russia. The city lies at the confluence of the Volga and the Kazanka Rivers, covering an area of 425.3 square kilometres (164.2 square miles), with a population of over 1.3 million residents, and up to nearly 2 million residents in the greater metropolitan area. Kazan is the fifth-largest city in Russia, being the most populous city on the Volga, as well as within the Volga Federal District. """)

@bot.message_handler(commands=['kng_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Kaliningrad, known as Königsberg until 1946, is the largest city and administrative centre of Kaliningrad Oblast, a Russian exclave between Lithuania and Poland. The city sits about 663 kilometres (412 mi) west of the bulk of Russia. The city is situated on the Pregolya River, at the head of the Vistula Lagoon on the Baltic Sea, and is the only ice-free Russian port on the Baltic Sea. Its population in 2020 was 489,359. Kaliningrad is the second-largest city in the Northwestern Federal District, after Saint Petersburg, the third-largest city in the Baltic region, and the seventh-largest city on the Baltic Sea.""")
 
@bot.message_handler(commands=['nnv_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Nizhny Novgorod Russian: Нижний Новгород,  colloquially shortened to Nizhny) is the administrative centre of Nizhny Novgorod Oblast and the Volga Federal District in Russia. The city is located at the confluence of the Oka and the Volga rivers in Central Russia, with a population of over 1.2 million residents, up to roughly 1.7 million residents in the urban agglomeration. Nizhny Novgorod is the sixth-largest city in Russia, the second-most populous city on the Volga, as well as the Volga Federal District. It is an important economic, transportation, scientific, educational and cultural centre in Russia and the vast Volga-Vyatka economic region, and the main centre of river tourism in Russia. In the historic part of the city there are many universities, theatres, museums and churches.""")

@bot.message_handler(commands=['ark_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Arkhangelsk[a] (Russian: Архангельск) is a city and the administrative center of Arkhangelsk Oblast, Russia. It lies on both banks of the Northern Dvina near its mouth into the White Sea. The city spreads for over 40 kilometres (25 mi) along the banks of the river and numerous islands of its delta. Arkhangelsk was the chief seaport of medieval and early modern Russia until 1703, when it was replaced by the newly founded Saint Petersburg.""")

@bot.message_handler(commands=['suz_facts'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.reply_to(message, """Suzdal (Russian: Суздаль) is a town that serves as the administrative center of Suzdalsky District in Vladimir Oblast, Russia, which is located near the Kamenka River, 26 kilometers (16 mi) north of the city of Vladimir. As of the 2021 Census, its population was 9,286.

In the 12th century, Suzdal became the capital of the principality. Currently, Suzdal is the smallest of the Russian Golden Ring towns. It is home to Several sites listed as UNESCO World Heritage Sites.""")

bot.infinity_polling()
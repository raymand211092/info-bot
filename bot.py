import os
import telebot

channel = '@teste_forw1'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = ["www.todus.cu"]
#ip = ['google.com', 'yandex.ru', 'facebook.com']

for val in ip:
    response = os.system('ping -c 1 ' + val)
    if response == 0:
        print(val + ' is up!')
        bot.send_message(channel, val + ' is up')
    else:
        print(val + ' is down!')
        bot.send_message(channel, val + ' is down!')

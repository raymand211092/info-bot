import os
import telebot

channel = '-1001420899246'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = ["im.todus.cu", "www.todus.cu", "s3.todus.cu"]
#ip = ['google.com', 'yandex.ru', 'facebook.com']

for val in ip:
    response = os.system('ping -c 1 ' + val)
    if response == 0:
        print(val + ' is up!')
        bot.send_message(channel, val + ' is up')
    else:
        print(val + ' is down!')
        bot.send_message(channel, val + ' is down!')

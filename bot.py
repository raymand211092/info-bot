import socket
import sys
import time
#import os
import telebot

channel = '-1001420899246'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = "im.todus.cu"
port = 22
#ip = ['google.com', 'yandex.ru', 'facebook.com']
retry = 1
delay = 1
timeout = 2

def isOpen(ip, port):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
s.connect((ip, int(port)))
s.shutdown(2)
return True
except:
return False

def checkHost(ip, port):
    ipup = False
        for i in range(retry):
    if isOpen(ip, port):
        ipup = True
    break
        else:
    time.sleep(delay)
return ipup

if checkHost(ip, port):
print ip + " is UP"
bot.send_message(channel, ip + " is UP")

else:
    print ip + " is DOWN"
    bot.send_message(channel, ip + " is DOWN")

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

def tcpCheck(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def checkHost(ip,port):
    ipup = False
    for i in range(retry):
         if tcpCheck(host["ip"], host["port"]):
                ipup = True
                break
            else:
                printD('toDus is down!')
                bot.send_message(channel, val + ' is down!')

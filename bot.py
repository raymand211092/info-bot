import socket
import time
import telebot

channel = '@teste_forw1'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = ["www.todus.cu"]
port = 22
#ip = ['google.com', 'yandex.ru', 'facebook.com']

retry = 5
delay = 10
timeout = 3

def isOpen(ip, port):
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
        print(ip + " is UP")
        bot.send_message(channel, ip + ' is up')

import socket
#import os
import telebot

channel = '-1001420899246'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = "im.todus.cu"
port = 22
#ip = ['google.com', 'yandex.ru', 'facebook.com']

def checkport(port):
    socket_objet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_is = socket_objet.connect_ex((ip, port))
    socket_objet.close()
    if port_is == 0:
        return ("toDus esta funcionando")
        bot.send_message(channel, "toDus esta funcionando")
    else:
        return ("Hay problemas de conexion al toDus")
        bot.send_message(channel, "Hay problemas de conexion al toDus")
    

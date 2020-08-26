import socket
import telebot

channel = '@teste_forw1'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = ["s3.todus.cu"]
port = 80
#ip = ['google.com', 'yandex.ru', 'facebook.com']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  
def port_scan(port): 
    try: 
        s.connect((ip, port)) 
        return True
    except: 
        return False
  
  
if port_scan(port): 
    print('Port', port, 'is open') 
    bot.send_message(channel, 'Port', port, 'is open')
else: 
    print('Port', port, 'is closed')
    bot.send_message(channel, 'Port', port, 'is closed')

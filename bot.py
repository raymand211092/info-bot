import socket
import telebot

channel = '@teste_forw1'
token = '903986387:AAEOTXBHwGkilq9PCvC9NkfohZH259H7pC0'
bot = telebot.TeleBot(token)
ip = ["www.todus.cu"]
port = 22
#ip = ['google.com', 'yandex.ru', 'facebook.com']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
target = (ip, pot ') 
  
# getting the ip address using gethostbyname 
# function 
t_IP = socket.gethostbyname(target) 
print("Starting scan on host: ", t_IP) 
  
  
def port_scan(port): 
    try: 
        s.connect((t_IP, port)) 
        return True
    except: 
        return False
  
  
port = int(input("Enter the port number to be scanned: ")) 
  
if port_scan(port): 
    print('Port', port, 'is open') 
else: 
    print("port", port, "is closed")

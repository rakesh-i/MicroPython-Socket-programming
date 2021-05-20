import socket               # Import socket module
import time

s = socket.socket()         # Create a socket object
host = '111.111.111.111'    # ESP32 ip 
port = 12345                # Reserve a port for your service.

s.connect((host, port))

while True:
    x = "Hello World"
    msg = str.encode(x, 'utf-8') #encode msg to send
    print(msg)
    s.send(msg)
    data = s.recv(1024)
    print(data.decode())    #decode incoming data
    time.sleep(5)

 
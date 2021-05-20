import socket               # Import socket module
import time
import json
from log import key_check



s = socket.socket()         # Create a socket object
host = '111.111.111.111'    # ESP32 ip 
port = 12345                # Reserve a port for your service.


s.connect((host, port))

def key_out(key):
    output = [0, 0, 0, 0]
    if 'A' in key:
        output[0] = 1
    if 'D' in key:
        output[3] = 1
    if 'W' in key:
        output[1] = 1
    if 'S' in key:
        output[2] = 1
    return output


while True:
    key = key_check()
    a = key_out(key)
    x = '{"a":'
    x += str(a[0])
    x += ',"d":'
    x += str(a[3])
    x += ',"w":'
    x += str(a[1])
    x += ',"s":'
    x += str(a[2])
    x += "}"
    msg = str.encode(x, 'utf-8')
    print(msg)
    s.send(msg)
    data = s.recv(1024)
    

 
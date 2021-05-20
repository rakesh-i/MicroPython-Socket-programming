#command_server.py


def soc():
    import socket               # Import socket module
    import time
    import json
    p1 = Pin(13)
    servo = PWM(p1, freq=50)
    
    
    s = socket.socket()         # Create a socket object
    host = '111.111.111.111'    # Ip of esp32 on network
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        while True:
            d = 'thank you for connection'
            data = str(d)
            msg =str.encode(data, 'utf-8')
            c.send(msg)
            a = c.recv(2048)
            com = a.decode()
            x = json.loads(com)
            print(x)
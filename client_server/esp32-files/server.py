#server.py


def soc():
    import socket               # Import socket module
    import time
    
    
    s = socket.socket()         # Create a socket object
    host = '111.111.111.111'    # esp32's ip on network
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    
    
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        while True:
            data = 'Thank you for Connection'
            msg =str.encode(data, 'utf-8')
            c.send(msg)
            a = c.recv(2048)
            com = a.decode()
            print(com)
            time.sleep(5)
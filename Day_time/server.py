import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 2808

s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()
    print("Conected to:", addr)
    msg = c.recv(1024).decode('utf-8')
    currtime = time.ctime(time.time())
    c.send(currtime.encode('utf-8'))
    c.close()

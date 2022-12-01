import socket

s = socket.socket()
host = socket.gethostname()
port = 3805
s.bind((host,port))
s.listen(5)
while True:
    c,addr =s.accept()
    msg = c.recv(1024).decode('utf-8')
    print("got the message as:",msg)
    msg_1 = input()
    c.send(msg_1.encode('utf-8'))
    c.close()

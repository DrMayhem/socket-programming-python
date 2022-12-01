import socket

s = socket.socket()
host = socket.gethostname()
port = 3708

s.connect((host,port))

msg = input("Enter message to send to server: ")
while(msg!='bye'):
    s.send(msg.encode('utf-8'))
    msg_1 = s.recv(1024).decode('utf-8')
    print("Message got from server", msg_1)
    msg = input("Enter message to send to server: ")

s.close()

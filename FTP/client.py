import socket
host = socket.gethostname()
port=4443
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host,port))
data = "Replacing data with this text"
c.send("data.txt".encode())
msg = c.recv(1024).decode()
print("SERVER:", msg)
c.send(data.encode())
msg = c.recv(1024).decode()
print("SERVER:",msg)
c.close()
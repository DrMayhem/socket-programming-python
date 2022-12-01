import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('', 42042)
s.bind(server_address)
s.connect(('192.168.1.5', 4644))
while True:
    msg = input("Enter a command: ")
    s.send(msg.encode('utf-8'))
    confirm =s.recv(1024).decode('utf-8')
    if confirm == "yes":
        print("[+] Command executed successfully.")
    else:
        print("[-] Command failed to execute!!!")

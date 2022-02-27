# socket client
import socket
skt = socket.socket()
hostname = socket.gethostname()
port = 12357
skt.connect((hostname, port))
data = skt.recv(1024)
print('data is ', data.decode()) 
skt.close()
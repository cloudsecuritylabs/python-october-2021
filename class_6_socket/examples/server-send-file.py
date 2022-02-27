# send file to client
import socket
port = 3000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)
print ('Server running')
while True:
    conn, addr = s.accept()
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', bytes.decode(data))
    filename='secret.txt'
    file = open(filename,'rb')
    line = file.read(1024)
    while (line):
       conn.send(line) #
       print('Server received ',bytes.decode(line))
       line = file.read(1024)
    file.close()
    print('Finished sending')
    conn.send(str.encode('Thank you for connecting'))
    conn.close()
    break

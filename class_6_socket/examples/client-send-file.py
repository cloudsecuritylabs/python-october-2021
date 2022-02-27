# Socket Client Program
# receive file from server
# and write it to a new file
import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 3000  # Set the port for your service.
s.connect((host, port))  # connect to server
s.send(str.encode("Client connected"))  # send connect confirmation to user
# open the output file (pjrecfile)
with open('secret.txt', 'wb') as file:
    print('file opened')
    while True:
        print('receiving data from server')
        data = s.recv(
            1024)  # receive each line of data from server (at most 1024 bytes)
        print('data is ',
              bytes.decode(data))  # print the line of data received
        if not data:
            break
        # write data to the file
        file.write(data)
    file.close()  # close the output file
    print('Received file from server')
    print('Written to output file pjrecfile')
    s.close()  # close the connection
    print('connection closed')


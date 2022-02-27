# socket server
import socket
skt = socket.socket()  # Create a socket
hostname = socket.gethostname()
print(hostname)
port = 12357
skt.bind((hostname, port))
skt.listen(5)
while True:
    con, accaddr = skt.accept()  # Accept connection with client.
    # 'con' is the open connection between the server and client,
    # 'accaddr' is the IP address and port number
    print('con is ', con)  # print values to the user
    print('accaddr is ', accaddr)  # print values to the user
    print('Received connection from', accaddr)  # print values to the user
    message = "Got your connection"
    con.send(message.encode())  # send message to client to confirm connect
    con.close()  # Close connection
    break



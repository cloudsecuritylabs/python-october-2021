'''
1. create a server socket using Python
2. connect to the server socket created using Python from nc
3. #nc localhost 50002
'''
import socket
# Create a socket
new_socket = socket.socket()
# Bind a socket
new_socket.bind(("0.0.0.0", 60002)) # this takes a Tuple!
# Start listening
new_socket.listen(4) # amount of allowed connections
# create connection
# print(type(new_socket.accept()))
conn, addr = new_socket.accept() # this takes two variable

print(f'conn is {conn}')
print(f'addr is {addr}')
# when data is received, close connection
new_socket.close()




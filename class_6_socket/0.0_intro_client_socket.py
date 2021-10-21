# https://docs.python.org/3/howto/sockets.html
# INET (i.e. IPv4) sockets account for at least 99% of the sockets in use
# STREAM (i.e. TCP) sockets

import socket
# create an INET, STREAMing socket
clientsocket = socket.socket()
# clientsocket = socket.socket(socket.INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
# Client sockets are normally only used for one exchange and then destroyed
www = "www.python.org"
port = 80
my_client = (www, port)
clientsocket.connect(my_client)
print(clientsocket.getsockname()) # what is the datatype returned?
# s.send("hello")


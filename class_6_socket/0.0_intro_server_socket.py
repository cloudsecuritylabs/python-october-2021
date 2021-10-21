import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
# if we use localhost, it is reachable only to the machine
# if we use private ip, reachable to the internal network
serversocket.bind((socket.gethostname(), 80))

# become a server socket
serversocket.listen(5)


# real world scenario!
# while True:
#     # accept connections from outside
#     (clientsocket, address) = serversocket.accept()
#     # now do something with the clientsocket
#     # in this case, we'll pretend this is a threaded server
#     ct = client_thread(clientsocket)
#     ct.run()
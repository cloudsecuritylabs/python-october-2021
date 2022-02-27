import socket
try:
     mysocket = socket.socket()
     mysocket.connect(('localhost', 2005))
     print("connection establish...")
     while True:
         serverData = mysocket.recv(2048).decode()
         print("server : {}".format(serverData))
         if serverData == "exit":
             print("connection as closed by server")
             mysocket.close()
             break
         sendData = input("client : ")
         mysocket.send(sendData.encode())
         if sendData == "exit":
             print("connection as closed by client")
             mysocket.close()
             break
except Exception as e:
 print(e)
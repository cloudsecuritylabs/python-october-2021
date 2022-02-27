# get user input for a sercive/port
service_port = {}
service = port = "1"
service = input("Service: ")
port = input("Port ")
while service != "0" or port != "0":
    if service == 0 or port ==0:
        break
    else:
        service_port[service] = int(port)
    service = input("Service: ")
    port = input("Port ")
print(service_port)


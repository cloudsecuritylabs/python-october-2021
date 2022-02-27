
IP = input("Give me your IP: ")
# print(type(IP))

ip_octet = IP.split(".")
# print(ip_octet)
# print(type(ip_octet))

first_ip_octet = ip_octet[0]


if int(first_ip_octet ) < 126:
    print("class A")






# find the malicious IP and print "t
private_ips = ["192.168.1.20", "10.0.0.20", "192.168.2.33", "10.1.1.15"]
for ip in private_ips:
    if ip == "10.0.0.20":
        continue
        print("Found it!!")
    else:
        print("Not malicious ..")











# # find the malicious IP from a list
# private_ips = ["192.168.1.20", "10.0.0.20", "192.168.2.33", "10.1.1.15"]
# for ip in private_ips:
#     if ip == "10.0.0.20":
#         print(f"IP found {ip}")
#         break
#     else:
#         print("Continue search ...")

#
# Continue search ...
# IP found 10.0.0.20

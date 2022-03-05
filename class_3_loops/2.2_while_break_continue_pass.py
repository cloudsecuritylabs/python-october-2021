
# counter = 0
#
# while counter < 10:
#     counter = counter + 1
#     if counter == 7:
#         print(f'counter is {counter}')
#         # break # exit out of the loop
#     else:
#         print(f'counter is {counter}')

bad_ip = "10.0.1.2"

ips = [ "10.0.0.1", "10.0.0.2", "10.0.0.4", "10.0.0.7"]
for ip in ips:
    if ip == bad_ip:
        print("Hey I got the bad Ip - top pf continue")
        continue
        print("Hey I got the bad Ip - bottom of continue")
    elif ip ==  "10.0.0.4":
        pass
    else:
        print(f"Good IPs....{ip}")







































# counter = 0
# while counter < 5:
#     counter += 1
#     if counter == 3:
#         # pass
#         # break
#         # continue
#         # bring this print only when explaining pass vs break
#         print(f"passing {counter}")
#     else:
#         print(f"The current number is: {counter}")






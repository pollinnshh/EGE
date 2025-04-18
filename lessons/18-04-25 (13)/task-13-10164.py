from ipaddress import *

cnt = -1
net = ip_network("156.132.15.138/255.255.252.0", False)
for i in net:
    cnt += 1
    if i == ip_address("156.132.15.138"):
        print(cnt)
        break

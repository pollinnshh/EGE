from ipaddress import *

cnt = 0
net = ip_network("172.16.168.0/255.255.248.0")
for i in net:
    i = f"{int(i):032b}"
    if i.count("1") % 5 != 0:
        cnt += 1

print(cnt)

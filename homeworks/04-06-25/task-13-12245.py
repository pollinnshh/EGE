from ipaddress import *

cnt = 0
net = ip_network("192.168.32.48/255.255.255.240")
for i in net:
    i = f"{int(i):032b}"
    if i.count("1") % 2:
        cnt += 1

print(cnt)

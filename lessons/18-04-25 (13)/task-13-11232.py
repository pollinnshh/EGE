from ipaddress import *

ans = []
net = ip_network("192.168.31.80/255.255.255.240")
for i in net:
    i = f"{int(i):032b}"
    summ = i.count("1")
    ans.append(summ)

print(max(ans))

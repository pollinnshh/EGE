from ipaddress import *

cnt = 0
ip_1 = ip_address("95.24.2.9")
ip_2 = ip_address("95.24.3.10")
for mask in range(3, 31):
    net_1 = ip_network(f"{ip_1}/{mask}", False)
    net_2 = ip_network(f"{ip_2}/{mask}", False)
    if net_1.network_address != net_2.network_address:
        if ip_1 in net_1.hosts() and ip_2 in net_2.hosts():
            cnt1 = 0
            for i in net_1.hosts():
                i = f"{int(i):032b}"
                if i[-1] == "0":
                    cnt1 += 1
            cnt2 = 0
            for i in net_2.hosts():
                i = f"{int(i):032b}"
                if i[-1] == "0":
                    cnt2 += 1
            cnt = max(cnt, cnt1, cnt2)
            
print(cnt)

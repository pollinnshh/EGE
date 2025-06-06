from ipaddress import *

ip_1 = ip_address("121.171.5.70")
ip_2 = ip_address("121.171.5.107")

for mask in range(31, 1, -1):
    net_1 = ip_network(f"{ip_1}/{mask}", False)
    net_2 = ip_network(f"{ip_2}/{mask}", False)
    cnt = 0
    if net_1 == net_2:
        if ip_1 in net_1.hosts() and ip_2 in net_2.hosts():
            for i in net_1:
                cnt += 1
            print(cnt)
            break
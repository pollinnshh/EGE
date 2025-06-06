from ipaddress import *

ip_1 = ip_address("10.96.180.231")
ip_2 = ip_address("10.96.140.118")

for mask in range(32):
    net_1 = ip_network(f"{ip_1}/{mask}", False)
    net_2 = ip_network(f"{ip_2}/{mask}", False)
    if net_1 != net_2:
        if ip_1 in net_1.hosts() and ip_2 in net_2.hosts():
            print(32 - mask)
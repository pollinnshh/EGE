from ipaddress import *

ip_1 = ip_address("216.54.187.235")
ip_2 = ip_address("216.54.174.128")

for mask in range(30, 2, -1):
    net_1 = ip_network(f"{ip_1}/{mask}", False)
    net_2 = ip_network(f"{ip_2}/{mask}", False)
    if ip_1 in net_1.hosts() and ip_2 in net_2.hosts():
        if net_1.network_address != net_2.network_address:
            print(mask)
            break

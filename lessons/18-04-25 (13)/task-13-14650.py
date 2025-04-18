from ipaddress import *

ip1 = ip_address("216.54.187.235")
ip2 = ip_address("216.54.174.128")
for mask in range(33):
    net1 = ip_network(f"{ip1}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if ip1 != net1.broadcast_address and ip1 != net1.network_address:
        if ip2 != net2.broadcast_address and ip2 != net2.network_address:
            if net1.network_address != net2.network_address:
                print(mask)

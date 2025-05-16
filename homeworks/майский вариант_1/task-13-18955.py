from ipaddress import *

ip_1 = ip_address("200.154.190.12")
ip_2 = ip_address("200.154.184.0")
for mask in range(32, 1, -1):
    net1 = ip_network(f"{ip_1}/{mask}", False)
    net2 = ip_network(f"{ip_2}/{mask}", False)
    if net1 == net2:
        if net1.broadcast_address != ip_1 and net1.network_address != ip_1:
            if net2.network_address != ip_2 and net2.network_address != ip_2:
                print(mask)

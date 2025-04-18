from ipaddress import *

ip1 = ip_address("121.171.5.70")
ip2 = ip_address("121.171.5.107")
for mask in range(32, 1, -1):
    net1 = ip_network(f"{ip1}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if ip1 != net1.network_address and ip1 != net1.broadcast_address:
        if ip2 != net2.network_address and ip2 != net2.broadcast_address:
            if net1.network_address == net2.network_address:
                print(2 ** (32 - mask))
                break
                # net1.num_addresses

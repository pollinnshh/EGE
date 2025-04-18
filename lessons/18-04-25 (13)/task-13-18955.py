from ipaddress import ip_network, ip_address

ip1 = ip_address("200.154.190.12")
ip2 = ip_address("200.154.184.0")
for mask in range(33):
    net1 = ip_network(f"{ip1}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if ip1 != net1.network_address and ip1 != net1.broadcast_address:
        if ip2 != net2.network_address and ip2 != net2.broadcast_address:
            if net1.network_address == net2.network_address:
                print(mask)

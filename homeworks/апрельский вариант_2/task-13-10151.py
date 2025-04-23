from ipaddress import *

ip = ip_address("111.81.192.0")
for mask in range(16, 33):
    net = ip_network(f"111.81.208.27/{mask}", False)
    if ip == net.network_address:
        print(net.netmask)

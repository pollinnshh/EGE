from ipaddress import *

for mask in range(33):
    net1 = ip_network(f"157.127.172.56/{mask}", False)
    net2 = ip_network(f"157.127.191.78/{mask}", False)
    if net1.network_address != net2.network_address:
        print(mask)

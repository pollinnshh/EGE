from ipaddress import *

ip_1 = ip_address("157.127.182.76")
ip_2 = ip_address("157.127.190.80")

for mask in range(32):
    net_1 = ip_network(f"{ip_1}/{mask}", False)
    net_2 = ip_network(f"{ip_2}/{mask}", False)
    if net_1 != net_2:
        if ip_1 in net_1.hosts() and ip_2 in net_2.hosts():
            print(mask)
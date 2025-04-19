from ipaddress import *

ans = []
for a in range(1, 256):
    net = ip_network(f"248.112.{a}.35/255.255.255.240", False)
    for i in net:
        i = f"{int(i):032b}"
        if i[:16].count("0") > i[16:].count("0"):
            break
    else:
        ans.append(a)

print(max(ans))

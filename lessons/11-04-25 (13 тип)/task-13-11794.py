from ipaddress import *

ans = []
for a in range(256):
    net = ip_network(f"223.167.{a}.167/255.255.255.192", False)
    for i in net:
        i = f"{int(i):032b}"
        lev = i[:16]
        prav = i[16:]
        if lev.count("0") > prav.count("0"):
            break
    else:
        ans.append(a)
print(max(ans))

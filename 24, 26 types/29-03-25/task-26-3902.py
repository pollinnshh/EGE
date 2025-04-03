from ipaddress import ip_address
from itertools import groupby

with open("26_3902.txt") as file:
    n = int(file.readline())
    ips = []
    for i in file:
        ip = f"{int(ip_address(".".join(i.split()))):032b}"
        ips.append([ip[:19], ip[19:]])

ips = sorted(ips)
ans = {}
for ip in ips:
    if ip[0] in ans:
        ans[ip[0]].append(ip[1])
    else:
        ans[ip[0]] = [ip[1]]


ans_ip = ""
ans_cnt = 0
for i in ans.items():
    if ans_cnt <
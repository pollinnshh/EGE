from operator import index
from string import ascii_lowercase, digits
alf = digits + ascii_lowercase
for x in alf[1:35]:
    a = int("6" + x + "qr" + x,35)
    b = int(x + "59sh",35)
    c = int("ph" + x + "69yw",35)
    num = a + b + c
    count = [0] * 10
    for i in str(num):
        count[int(i)] += 1
    chisl_1 = count[::-1].index(max(count))
    maxx = 9 - chisl_1
    if num % maxx**2 == 0:
        print(num // maxx**2)

# digit = int(sorted(Counter(str(num)).most_common(), key=lambda x: (-x[1], -int(x[0])))[0][0])
# альтернатива
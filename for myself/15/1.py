def f(a):
    for x in range(1,10000):
        x_90 = (90 % a) == 0
        x_a = (x % a) != 0
        x_15 = (x % 15) == 0
        x_20 = (x % 20) != 0
        f = (x_90 and (x_a <= x_15 <= x_20))
        if f == 0:
            return 0
        else:
            return 1
for a in range(10000,1,-1):
    if f(a) == 1:
        print(a)
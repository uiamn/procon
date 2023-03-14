N = int(input())
f = lambda x, y: x**3 + (x**2 * y) + (x * y**2) + y**3

ans = 10**18

for a in range(10**6 + 1):
    mi = a
    ma = 10**6 + 1
    while ma - mi >= 2:
        b = (ma + mi) // 2
        v = f(a, b)
        if v >= N:
            ans = min(v, ans)
            ma = b
        else:
            mi = b

print(ans)

K, T = map(int, input().split())
a = map(int, input().split())

amax = max(a)
if amax <= (K+1) // 2:
    print(0)
else:
    print(K - (K-amax)*2 - 1)

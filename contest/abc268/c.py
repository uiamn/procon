N = int(input())
p = list(map(int, input().split()))

arr = [(i - p[i]) % N for i in range(N)]

hoge = {i: 0 for i in range(N)}

for a in arr:
    hoge[a] += 1
    hoge[(a-1) % N] += 1
    hoge[(a+1) % N] += 1

print(max(hoge.items(), key=lambda x: x[1])[1])

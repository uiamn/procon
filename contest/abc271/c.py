from collections import deque

N = int(input())
a = sorted(list(map(int, input().split())))
aa = deque([])

free = 0

i = 0
while i < N:
    aa.append(a[i])

    j = 1
    while i + j < N:
        if a[i] == a[i+j]:
            free += 1
            j += 1
        else:
            break

    i+=j

res = 0
while len(aa) or free >= 2:
    if len(aa) == 0:
        free -= 2
        res += 1
        continue
    if aa[0] == res + 1:
        res += 1
        aa.popleft()
        continue
    else:
        if free >= 2:
            free -= 2
            res += 1
            continue
        elif free >= 1:
            free = 0
            if len(aa) >= 1:
                aa.pop()
                res += 1
                continue
        else:
            if len(aa) >= 2:
                aa.pop()
                aa.pop()
                res += 1
                continue

    break

print(res)

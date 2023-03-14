from bisect import bisect, bisect_left


walls_r = {}  # i 行目に存在する壁
walls_c = {}  # i 列目に存在する壁

H, W, rs, cs = map(int, input().split())
N = int(input())

for _ in range(N):
    r, c = map(int, input().split())
    if r in walls_r:
        walls_r[r].append(c)
    else:
        walls_r[r] = [c]

    if c in walls_c:
        walls_c[c].append(r)
    else:
        walls_c[c] = [r]


for v in walls_r.values():
    v.sort()

for v in walls_c.values():
    v.sort()

Q = int(input())

nowr, nowc = rs, cs

for _ in range(Q):
    d, l = input().split()
    l = int(l)

    if d == 'L':
        if nowr not in walls_r:
            nowc = nowc-l
        else:
            a = walls_r[nowr]
            index1 = bisect_left(a, nowc-l)
            index2 = bisect_left(a, nowc)

            if index1 == index2:
                nowc = nowc-l
            else:
                nowc = a[index2-1]+1

    elif d == 'R':
        if nowr not in walls_r:
            nowc = nowc+l
        else:
            a = walls_r[nowr]
            index1 = bisect_left(a, nowc)
            index2 = bisect(a, nowc+l)

            if index1 == index2:
                nowc = nowc+l
            else:
                nowc = a[index1]-1

    elif d == 'U':
        if nowc not in walls_c:
            nowr = nowr-l
        else:
            a = walls_c[nowc]
            index1 = bisect_left(a, nowr-l)
            index2 = bisect_left(a, nowr)

            if index1 == index2:
                nowr = nowr-l
            else:
                nowr = a[index2-1]+1

    elif d == 'D':
        if nowc not in walls_c:
            nowr = nowr+l
        else:
            a = walls_c[nowc]
            index1 = bisect_left(a, nowr)
            index2 = bisect(a, nowr+l)

            if index1 == index2:
                nowr = nowr+l
            else:
                nowr = a[index1]-1

    if nowr <= 0:
        nowr = 1
    if nowr >= H + 1:
        nowr = H

    if nowc <= 0:
        nowc = 1
    if nowc >= W + 1:
        nowc = W

    print(nowr, nowc)

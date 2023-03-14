N, Q = map(int, input().split())

users = {}

for _ in range(Q):
    t, a, b = map(int, input().split())

    if t == 1:
        if a in users:
            users[a].add(b)
        else:
            users[a] = {b}
    elif t == 2:
        if a in users and b in users[a]:
            users[a].remove(b)
        else:
            pass
    else:
        if a in users and b in users[a] and b in users and a in users[b]:
            print('Yes')
        else:
            print('No')

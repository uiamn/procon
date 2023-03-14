from collections import deque

A = deque([])

note = {}

Q = int(input())

ans = []

for _ in range(Q):
    q = input()

    if q[0] == 'D':
        if len(A) != 0:
            A.pop()
    else:
        kind, n = q.split()
        n = int(n)

        if kind == 'ADD':
            A.append(n)
        elif kind == 'SAVE':
            note[n] = deque(A)
        else:
            if n in note:
                A = note[n]
            else:
                A = deque([])
    ans.append(A[-1] if len(A) != 0 else -1)

print(' '.join(map(str, ans)))

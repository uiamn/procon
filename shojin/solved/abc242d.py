tbl = {'A': 'B', 'B': 'C', 'C': 'A'}
inv_tbl = {'A': 'C', 'B': 'A', 'C': 'B'}
f = {'A': 'BC', 'B': 'CA', 'C': 'AB'}

def solve(t, k, S):
    if t == 0:
        return S[k]
    elif k == 1:
        if t % 3 == 0:
            return S[1]
        elif t % 3 == 1:
            return tbl[S[1]]
        else:
            return inv_tbl[S[1]]
    else:
        a = solve(t-1, (k+1)//2, S)
        s = f[a]

        if k % 2 == 0:
            return s[1]
        else:
            return s[0]

S = ' ' + input()
Q = int(input())

for _ in range(Q):
    t, k = map(int, input().split())
    print(solve(t, k, S))

N = int(input())

for _ in range(N):
    T = list('atcoder')
    S = list(input())
    ans = None

    while len(S) > 0 and len(T) > 0 and ans is None:
        s = S.pop()
        t = T.pop()

        if t < s:
            ans = 0
        elif s < t:
            for i, ss in enumerate(S):
                if t < ss:
                    ans = i+1
                    break

    if ans is not None:
        print(ans)
    else:
        if len(S) == 0:
            print(-1)
        elif len(T) == 0:
            print(0)

N, _ = map(int, input().split())
D = set(map(str, input().split()))

ans = N

while ans < 100000+1:
    if not (D & set(str(ans))):
        print(ans)
        exit(0)

    ans += 1

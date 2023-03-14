def n_divs(n):
    if memo[n] is not None:
        return memo[n]

    last_div = 1
    count = 0
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            count += 1
            last_div = i

    if last_div ** 2 == n:
        count = count * 2 - 1
    else:
        count = count * 2

    memo[n] = count
    return count

N = int(input())

if N == 2:
    print(1)
    exit(0)

memo = [None for _ in range(N+1)]
memo[1] = 1
memo[2] = 2
memo[3] = 2
ans = 0

for ab in range(1, N):
    cd = N - ab
    ans += n_divs(ab) * n_divs(cd)

print(ans)

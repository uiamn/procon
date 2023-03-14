import math
def primes(n):
    # 2 以上 n 以下の全素数のリストを返す
    p = [True for _ in range(n+1)]
    p[1] = False
    result = []

    for i in range(2, n+1):
        if p[i]:
            result.append(i)
            if i <= n**(1/2):
                for j in range(i*i, n+1, i):
                    p[j] = False

    return result

def n_divs(n):
    nn = n
    count = 1
    for p in ps:
        tmp = 0
        while nn % p != 0:
            tmp += 1
            nn //= p

        count *= (tmp + 1)

    return count

N = int(input())
ps = primes(math.ceil(N))
ans = 0

divlist = [None for _ in range(N+1)]
divlist[1] = 1
for i in range(2, N+1):
    divlist[i] = n_divs(i)

print(divlist)

if N % 2 == 1:
    for ab in range(1, N // 2):
        cd = N - ab
        ans += n_divs(ab) + n_divs(cd)

    ans *= 2
else:
    for ab in range(1, N // 2 - 1):
        cd = N - ab
        ans += n_divs(ab) + n_divs(cd)

    ans *= 2

print(ans)


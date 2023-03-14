def nCr(n, r):
    ans = 1
    for i in range(r):
        ans *= (n-i)

    for i in range(r):
        ans //= (i+1)

    return ans


def f(n, k):
    strn = str(n)
    digit = len(strn)

    if digit < k:
        return 0

    m = digit - 1

    ans = 0
    # 最上位桁を 0 とするとき
    if m >= k:
        ans += nCr(m, k) * (9 ** k)

    # n の最上位桁を a とする．最上位桁を 1, ..., a-1 とするとき
    a = int(strn[0])
    ans += (a-1) * nCr(m, k-1) * (9 ** (k-1))

    # 最上位桁を a とするとき
    if k == 1:
        ans += 1
    else:
        ans += f(n - (a * (10 ** m)), k-1)

    return ans

N = int(input())
K = int(input())

print(f(N, K))

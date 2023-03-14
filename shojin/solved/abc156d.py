def factorial(lo: int, hi: int, MOD=10**9 + 7):
    """
        lo 以上 hi 以下の階乗のリストを返す
        ただし lo は負数で，絶対値が hi 以下である必要がある．
        返り値
            fact[i]     = i! % MOD
            factinv[i]  = i!^{-1} % MOD
    """
    lo = -lo

    fact = [1]
    v = 1
    for i in range(1, hi+1):
        v *= i
        v %= MOD
        fact.append(v)

    factinv = [None for _ in range(lo+1)]
    v = pow(fact[lo], MOD-2, MOD)
    factinv[lo] = v

    for i in range(1, lo+1):
        n = lo - i
        v *= (n+1)
        v %= MOD
        factinv[n] = v

    return fact, factinv


def mod_bin(n: int, r: int, factorial_inv, MOD=10**9 + 7) -> int:
    """
        nCr mod MOD を求める．
        事前に calc_factorial を使って factorial_inv を求めておく必要がある
    """
    nCr = 1
    for i in range(r):
        nCr *= (n-i)
        nCr %= MOD

    return (nCr * factorial_inv[r]) % MOD


MOD = 10**9 + 7

n, a, b = map(int, input().split())
_, factinv = factorial(-b, b+1)

nCa = mod_bin(n, a, factinv)
nCb = mod_bin(n, b, factinv)

print((pow(2, n, MOD) - 1 - nCa - nCb) % MOD)

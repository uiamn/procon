def calc_factorial(lo: int, hi: int, MOD=10**9 + 7):
    """
        lo 以上 hi 以下の階乗のリストを返す
        ただし lo は負数で，絶対値が hi 以下である必要がある．
        返り値
            factorial[i]     = i! % MOD
            factorial_inv[i] = i!^{-1} % MOD
    """
    lo = -lo

    factorial = [1]
    v = 1
    for i in range(1, hi+1):
        v *= i
        v %= MOD
        factorial.append(v)

    factorial_inv = [None for _ in range(lo+1)]
    v = pow(factorial[lo], MOD-2, MOD)
    factorial_inv[lo] = v

    for i in range(1, lo+1):
        n = lo - i
        v *= (n+1)
        v %= MOD
        factorial_inv[n] = v

    return factorial, factorial_inv


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

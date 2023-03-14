from typing import List

def primes(n: int) -> List[int]:
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

def prime_table(n: int) -> List[bool]:
    # 長さ n+1 のリスト X で， i が素数 <=> X[i] が真 となるリストを返す
    P = primes(n)
    result = [False for _ in range(n+1)]
    for p in P:
        result[p] = True

    return result

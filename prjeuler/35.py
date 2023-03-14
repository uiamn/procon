from typing import Iterator, List

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

oneM = 10 ** 6
result = 4

PRIME_TABLE = prime_table(oneM)


def num_rotate(n: int) -> Iterator[int]:
    s = str(n)
    for _ in range(len(s)):
        yield int(s)
        s = s[1:] + s[0]


def is_circular_prime(n: int) -> bool:
    if len(set(str(n)) & set('02468')) != 0:
        return False

    for m in num_rotate(n):
        if not PRIME_TABLE[m]:
            return False

    return True

for i in range(11, 1000000, 2):
    if is_circular_prime(i):
        result += 1

print(result)

from typing import List

def primes(n: int) -> List[int]:
    # 2 以上 n 以下の全素数のリストを返す
    p = [True]*(n+1)
    print('hoge')
    p[1] = False
    result = []

    for i in range(2, n+1):
        if p[i]:
            result.append(i)
            if i*i <= n:
                for j in range(i*i, n+1, i):
                    p[j] = False
            print(i)

    return result

def prime_table(n: int) -> List[bool]:
    # 長さ n+1 のリスト X で， i が素数 <=> X[i] が真 となるリストを返す
    P = primes(n)
    result = [False for _ in range(n+1)]
    for p in P:
        result[p] = True

    return result



MAX = 10 ** 9
P = primes(MAX)

print("hoge")

PT = prime_table(MAX)

print("prime table ok")

def is_valid(n):
    a = ['3', '7', '109', '673']
    s = str(n)

    for ss in a:
        print(int(s + ss), int(ss + s))
        if not PT[int(s + ss)] or not PT[int(ss + s)]:
            return False

    return True

for p in P:
    if p < 674:
        continue

    if is_valid(p):
        print(p)
        print(p + 792)
        break



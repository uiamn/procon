import sys
sys.setrecursionlimit(100000)

def solve(A, K):
    import time
    time.sleep(1)
    nonzero_A = list(filter(lambda x: x != 0, A))
    n = len(nonzero_A)
    m = min(nonzero_A)
    alpha = K // n

    print(n*m, K)

    if n*m > K:
        beta = K % n
        res = []

        for i, a in enumerate(A):
            if a == 0:
                res.append(0)
            elif i < beta:
                res.append(a - alpha - 1)
            else:
                res.append(a - alpha)

        return res
    else:
        nextA = [a - n*m if a != 0 else 0 for a in A]
        return solve(nextA, K - n*m)

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve(A, K))

from math import ceil


A, B, T = map(int, input().split())

n = ceil((T-A) / (B-A))

print(A + (B-A) * n)

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
val = sum(A)

xcand = [val]  # xcand[i] = (x = i を選んだときの操作 1 直後の値)

for i in range(N):
    val = val - A[i] + L
    xcand.append(val)

# xcand が最小となるインデクスを選ぶ
a = 10 ** 18
idx = -1

for i, v in enumerate(xcand):
    if v < a:
        a = v
        idx = i

for i in range(idx):
    A[i] = L

val = sum(A)

ycand = [val]  # ycand[i] = (y = i を選んだときの操作 2 直後の値)
for i in range(1, N+1):
    val = val - A[-i] + R
    ycand.append(val)

print(min(ycand))

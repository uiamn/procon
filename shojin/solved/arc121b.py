from bisect import bisect

def dist(X, Y):
    # ソート済みリスト X, Y に対して， min_{x \in X, y \in Y} |x-y| を求める
    d = 10 ** 18
    for x in X:
        i = bisect(Y, x)
        if i == 0:
            d = min(d, abs(x - Y[0]))
        elif i == len(Y):
            d = min(d, abs(x - Y[-1]))
        else:
            d = min(d, abs(x - Y[i-1]), abs(x - Y[i]))

    return d

N = int(input())
rdog = []
gdog = []
bdog = []

for _ in range(2*N):
    a, c = input().split()
    if c == 'R':
        rdog.append(int(a))
    elif c == 'G':
        gdog.append(int(a))
    else:
        bdog.append(int(a))

# 各色の犬がそれぞれ偶数匹ゐる場合
if len(rdog) % 2 == 0 and len(gdog) % 2 == 0 and len(bdog) % 2 == 0:
    print(0)
    exit(0)

# さうでないなら，犬の数は 偶数 奇数 奇数の筈
if len(rdog) % 2 == 0:
    even_dog = rdog
    odd1_dog = gdog
    odd2_dog = bdog
elif len(gdog) % 2 == 0:
    even_dog = gdog
    odd1_dog = rdog
    odd2_dog = bdog
else:
    even_dog = bdog
    odd1_dog = rdog
    odd2_dog = gdog

even_dog.sort()
odd1_dog.sort()
odd2_dog.sort()

if len(even_dog) == 0:
    print(dist(odd1_dog, odd2_dog))
else:
    print(min(dist(odd1_dog, odd2_dog), dist(odd1_dog, even_dog) + dist(odd2_dog, even_dog)))

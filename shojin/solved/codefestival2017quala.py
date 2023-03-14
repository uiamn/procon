H, W = map(int, input().split())
count = {}

for _ in range(H):
    s = input()
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

if H % 2 == 0 and W % 2 == 0:
    # H も W も偶数なら，全ての文字が 4 の倍数個存在すれば達成できる
    if all([v % 4 == 0 for v in count.values()]):
        print('Yes')
    else:
        print('No')
elif H % 2 == 1 and W % 2 == 1:
    # H も W も奇数なら
    count_v = list(count.values())
    k = (H-1) // 2
    l = (W-1) // 2

    # まず 4 個ある文字を角に配置していく
    flag = True
    for _ in range(k*l):
        n = max(count_v)
        if n <= 3:
            # 達成不可能
            flag = False
            break
        else:
            count_v[count_v.index(n)] -= 4

    if not flag:
        print('No')
        exit(0)

    # 2 個ある文字を配置していく
    for _ in range(k+l):
        n = max(count_v)
        if n <= 1:
            # 達成不可能
            flag = False
            break
        else:
            count_v[count_v.index(n)] -= 2

    if not flag:
        print('No')
        exit(0)

    print('Yes')
else:
    # 片方が奇数のとき
    count_v = list(count.values())
    if H % 2 == 0:
        k = H // 2
        l = (W-1) // 2
    else:
        l = (H-1) // 2
        k = W // 2

    # まず 4 個ある文字を角に配置していく
    flag = True
    for _ in range(k*l):
        n = max(count_v)
        if n <= 3:
            # 達成不可能
            flag = False
            break
        else:
            count_v[count_v.index(n)] -= 4

    if not flag:
        print('No')
        exit(0)

    for _ in range(k):
        n = max(count_v)
        if n <= 1:
            # 達成不可能
            flag = False
            break
        else:
            count_v[count_v.index(n)] -= 2

    if not flag:
        print('No')
        exit(0)

    print('Yes')

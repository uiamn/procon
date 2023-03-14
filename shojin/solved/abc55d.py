N = int(input())
s = input()

# S = True, W = False とする
# 0 番目と N-1 番目を S or W で仮定して矛盾がないかを調べれば良い

for t in [(True, True), (True, False), (False, True), (False, False)]:
    tmp = [None for _ in range(N)]
    tmp[0] = t[0]
    tmp[-1] = t[1]

    for i in range(1, N):
        if tmp[i-1] == True:
            if s[i-1] == 'o':
                tmp[i] = tmp[i-2]
            else:
                tmp[i] = not tmp[i-2]
        else:
            if s[i-1] == 'x':
                tmp[i] = tmp[i-2]
            else:
                tmp[i] = not tmp[i-2]

    if tmp[N-1] != t[1]:
        continue

    if tmp[N-1]:  # 最後が羊
        if s[N-1] == 'o':
            if tmp[N-2] == tmp[0]:
                break
        else:
            if tmp[N-2] != tmp[0]:
                break
    else:  # 最後が狼
        if s[N-1] == 'x':
            if tmp[N-2] == tmp[0]:
                break
        else:
            if tmp[N-2] != tmp[0]:
                break
else:
    print(-1)
    exit(0)

print(''.join(['S' if t else 'W' for t in tmp]))

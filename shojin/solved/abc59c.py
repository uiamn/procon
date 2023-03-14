n = int(input())
a = list(map(int, input().split()))

ans1 = 0
tmpsum = 0
# 偶数番目を正にするパタン
for i, aa in enumerate(a):
    tmpsum += aa
    if i % 2 == 0 and (not tmpsum > 0):
        ans1 += abs(tmpsum) + 1
        tmpsum = 1
    elif i % 2 == 1 and (not tmpsum < 0):
        ans1 += abs(tmpsum) + 1
        tmpsum = -1

ans2 = 0
tmpsum = 0
# 奇数番目を正にするパタン
for i, aa in enumerate(a):
    tmpsum += aa
    if i % 2 == 1 and (not tmpsum > 0):
        ans2 += abs(tmpsum) + 1
        tmpsum = 1
    elif i % 2 == 0 and (not tmpsum < 0):
        ans2 += abs(tmpsum) + 1
        tmpsum = -1

print(min(ans1, ans2))

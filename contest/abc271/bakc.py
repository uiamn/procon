from collections import deque


N = int(input())

a = sorted(list(map(int, input().split())))
aa = []

res = 0
free = 0

i = 0
while i < N:
    aa.append(a[i])

    j = 1
    while i + j < N:
        if a[i] == a[i+j]:
            free += 1
            j += 1
        else:
            break

    i+=j


head = 0
tail = len(aa) - 1

res = 0

while head < len(aa):
    if aa[head] == res+1:
        head += 1
        res += 1
    else:
        if free >= 2:
            free -= 2
            head += 1
            res += 1
        elif free == 1:
            if tail - head >= 1:
                free -= 1
                tail -= 1
                head += 1
                res += 1
            else:
                break
        elif free == 0:
            if tail - head >= 2:
                tail -= 2
                head += 1
                res += 1
            else:
                break

print(res + free // 2)



# while True:
#     if len(a) == 0:
#         break
#     elif a[0] == res + 1:
#         a.popleft()
#         while len(a) and a[0] == res+1:
#             a.popleft()
#             free += 1
#         res += 1
#     else:
#         if free >= 2:
#             free -= 2
#             res += 1
#         elif free == 1:
#             if len(a) == 0:
#                 break
#             free -= 1
#             a.pop()
#             res += 1
#         else:
#             if len(a) <= 1:
#                 break
#             a.pop()
#             a.pop()
#             res += 1

# print(res + free // 2)

# while True:
#     print(res, free)
#     if len(a) == 0:
#         res += free // 2
#         break
#     elif a[0] == res+1:
#         while a[0] == res+1:
#             a.popleft()
#             free += 1
#         res += 1
#     elif free >= 2:
#         free -= 1
#         res += 1
#     elif free == 1:
#         if len(a) >= 1:
#             a.pop()
#             res += 1
#         else:
#             break
#     elif free == 0:
#         if len(a) >= 2:
#             a.pop()
#             a.pop()
#             res += 1
#             free += 1
#         else:
#             break

# print(res)

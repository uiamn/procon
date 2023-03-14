def is_valid_time(h, m):
    if h <= 23 and m <= 59:
        return True
    else:
        return False

def after_1_min(h, m):
    if m != 59:
        return (h, m+1)
    else:
        if h == 23:
            return (0, 0)
        else:
            return (h+1, 0)

def f(h, m):
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10

    if is_valid_time(a*10 + c, b*10 + d):
        return True
    else:
        return False

H, M = map(int, input().split())

while 1:
    if f(H, M):
        print(H, M)
        exit(0)
    H, M = after_1_min(H, M)

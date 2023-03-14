import itertools

board = [input() for _ in range(9)]
pones = []

for x in range(9):
    for y in range(9):
        if board[x][y] == '#':
            pones.append((x, y))

ans = 0

for p1, p2, p3, p4 in itertools.combinations(pones, 4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    d12 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    d34 = (x3 - x4) ** 2 + (y3 - y4) ** 2
    d13 = (x1 - x3) ** 2 + (y1 - y3) ** 2
    d24 = (x2 - x4) ** 2 + (y2 - y4) ** 2
    d14 = (x1 - x4) ** 2 + (y1 - y4) ** 2
    d23 = (x2 - x3) ** 2 + (y2 - y3) ** 2

    if (
        (d12 == d23 and d23 == d34 and d34 == d14)
        or (d13 == d34 and d34 == d24 and d24 == d12)
        or (d12 == d24 and d24 == d34 and d34 == d13)
    ):
        ans += 1
        print(p1, p2, p3, p4)


print(ans)

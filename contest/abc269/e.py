N = int(input())

possible_area = [1, 1, N, N]

for _ in range(10):
    tlx, tly, brx, bry = possible_area

    if brx - tlx != 0:
        print(f'? {1} {N} {tlx} {tlx + (brx-tlx)//2}', flush=True)  # 左半分に何個あるか？
        T = int(input())

        if T == (brx-tlx)//2 + 1:
            # 左半分にはもう置けない
            possible_area[0] = tlx + (brx-tlx)//2 + 1
        else:
            # 右半分にはもう置けない
            possible_area[2] = tlx + (brx-tlx)//2

    if bry - tly != 0:
        print(f'? {tly} {(tly + (bry - tly) // 2)} {1} {N}', flush=True)  # 上半分に何個あるか？
        T = int(input())

        if T == (bry - tly) // 2 + 1:
            # 上半分にはもう置けない
            possible_area[1] = (tly + (bry - tly) // 2) + 1
        else:
            # 右半分にはもう置けない
            possible_area[3] = tly + (bry - tly) // 2

    if possible_area[2] - possible_area[0] == 0 and possible_area[3] - possible_area[1] == 0:
        print(f'! {possible_area[1]} {possible_area[0]}', flush=True)
        exit(0)

print(f'! {possible_area[1]} {possible_area[0]}', flush=True)

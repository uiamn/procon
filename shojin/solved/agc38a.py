H, W, A, B = map(int, input().split())

a = ''.join(['1' if i < A else '0' for i in range(W)])
b = ''.join(['0' if i < A else '1' for i in range(W)])
for i in range(H):
    if i < B:
        print(a)
    else:
        print(b)

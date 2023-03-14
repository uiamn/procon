N = int(input())

if N < 16:
    print(f'0{hex(N)[2:].upper()}')
else:
    print(f'{hex(N)[2:].upper()}')

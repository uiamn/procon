def is_palindrome(s: str) -> bool:
    l = len(s)
    for i in range(l//2 + (l%2)):
        if s[i] != s[-(i+1)]:
            return False

    return True

oneM = 10 ** 6
result = 0

for i in range(1, oneM, 2):
    binary = bin(i)[2:]

    if is_palindrome(str(i)) and is_palindrome(binary):
        result += i

print(result)

import math

A, B = map(int, input().split())
p = A + B
q = A - B
t = math.asin(p / math.sqrt((p**2 + q**2)))
theta = -t
alpha = math.radians(15) - theta
alpha = alpha - math.radians(90)
x = A / math.cos(alpha)

print(x)

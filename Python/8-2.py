import math
a = int(input())
b = int(input())

x = (-b + (2 * a * math.sin(math.radians(60)) * math.cos(math.radians(60))) ** 0.5) / (2 * a)
print(x)
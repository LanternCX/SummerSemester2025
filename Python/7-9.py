eps = float(input())

i = 1

ans = 0
temp = 1e9

while not abs(temp) < eps:
    temp = 1 / ((2 * i) - 1)
    if abs(temp) < eps:
        break
    ans += (1 if i % 2 == 1 else -1) * temp
    i += 1
ans *= 4
print(f"{ans:.6f}")


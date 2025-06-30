a,b = map(int,input().split(' '))

x = (4 * a - b) // 2

if (4 * a - b) % 2 or a < 0 or b < 0:
    print("Data Error")
    exit()

if (a - x) < 1 or x < 1:
    print("Data Error")
    exit()

print(f"{x} {a - x}")

# x + y = a
# 2 * x + 4 * y = b
# y = a - x
# 2 * x + 4 * (a - x) = b
# 2 * x - 4 * x + 4 * a = b
# -2 * x = b - 4 * a
# 2 * x = 4 * a - b


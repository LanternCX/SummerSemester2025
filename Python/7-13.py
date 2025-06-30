import random

m, n, k = input().split()
m = int(m)
n = int(n)
k = int(k)

seed = int(n)

for _ in range(m):
    random.seed(seed)
    low = 10 ** (k - 1)
    high = 10 ** k - 1
    code = random.randint(low, high)
    print(code)
    seed = code

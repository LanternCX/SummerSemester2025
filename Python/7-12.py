n = int(input())

for i in range(pow(10, n - 1), pow(10, n)):
    s = str(i)
    res = 0
    for ch in s:
        res += pow(int(ch), n)
    if res == i:
        print(res)

n = int(input())

cnt = 0
l = n

for i in range(1, (n * (n + 1)) // 2 + 1):
    print(f"{chr(ord('A') + i - 1)}", end=' ')
    cnt += 1
    if cnt % l == 0:
        print('')
        l -= 1
        cnt = 0

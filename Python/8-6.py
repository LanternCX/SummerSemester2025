n = int(input())

ans = [0] * 32

idx = 0
while n > 0:
    ans[idx] = n % 2
    n >>= 1
    idx += 1
ans = ans[::-1]
for i in range(0, 32):
    print(ans[i], end='')


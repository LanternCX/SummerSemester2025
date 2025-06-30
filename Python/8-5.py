T = int(input())
while T > 0:
    T -= 1
    n, k = map(int, input().split())
    print(n, end=' ')
    if n == 0:
        print(0)
        continue
    if n < 0:
        print('-', end='')
    ans = ""
    n = abs(n)
    while n > 0:
        if n % k >= 10:
            ans += str(chr(ord('A') + (n % k) - 10))
        else:
            ans += str(n % k)
        n //= k
    print(ans[::-1])

m, n = map(int, input().split())

ans = []
for i in range(m, n + 1):
    s = str(i)
    res = 0
    for ch in s:
        res += int(ch) ** 3
    if res == i:
        ans.append(res)

print(ans[0], end='')
for s in ans[1:]:
    print(f", {s}", end='')

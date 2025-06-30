a = input().strip()
b = input().strip()

rt = float(b)
if rt <= 0:
    print("Data error!")
    exit()

if a.endswith('$'):
    res = float(a[:-1])
    if res <= 0:
        print("Data error!")
        exit()
    print(f"{res * rt:.2f}￥")
    exit()
elif a.endswith('￥'):
    res = float(a[:-1])
    if res <= 0:
        print("Data error!")
        exit()
    print(f"{res / rt:.2f}$")
    exit()
else:
    print("Data error!")
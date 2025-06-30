a = int(input())
b = int(input())
ch = input()

if ch == '女':
    print(f"{int((a * 0.923 + b) / 2)}")

elif ch == '男':
    print(f"{int(((a + b) * 1.08) / 2)}")
else:
    print("无对应公式")
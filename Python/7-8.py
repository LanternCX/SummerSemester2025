s = input()

n = int(s[:-1])
ch = s[-1]


if not 'A' <= ch <= 'F' or not 1 <= n <= 17:
    print("输入错误")
    exit()

if not tag:
    print("输入错误")
    exit()

if not (1 <= n <= 17):
    print("输入错误")
    exit()

if ch == 'A' or ch == 'F':
    print('过道')
    exit()
if ch == 'C' or ch == 'D':
    print('窗口')

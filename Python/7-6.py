sc = input().strip()

if not sc.isdigit():
    print("Data Error")
    exit()

sc = float(sc)

if sc > 100 or sc < 0:
    print("Data Error")
    exit()
if sc >= 90:
    print("A")
elif 80 <= sc < 90:
    print("B")
elif 70 <= sc < 80:
    print("C")
elif 60 <= sc < 70:
    print("D")
else:
    print("E")

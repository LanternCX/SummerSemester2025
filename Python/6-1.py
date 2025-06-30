PI = 3.14159
R = eval(input())
r = eval(input())
n = eval(input())


def areaCircle(radius):
    return PI * radius * radius


# 计算垫片总面积
areaSum = n * (areaCircle(R) - areaCircle(r))

print('{:.2f}'.format(areaSum))

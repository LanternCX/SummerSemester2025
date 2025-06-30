def distance(x, y, z):
    return x * x + y * y + z * z ** 0.5


x, y, z = input().split(',')
d = distance(float(x), float(y), float(z))
print("{:.2f}".format(d))  #输出距离值，保留三维小数

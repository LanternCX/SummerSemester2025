s = input()

lower = upper = digit = space = other = 0

for c in s:
    if c.islower():
        lower += 1
    elif c.isupper():
        upper += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        other += 1

print(f"{lower} {upper} {digit} {space} {other}")

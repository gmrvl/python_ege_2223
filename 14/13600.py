a = 4 ** 255 + 2 ** 255 - 255

a = bin(a)[2:]

print(a.count('1'))

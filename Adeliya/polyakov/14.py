a = 8 ** 20 + ((8 ** 22 - 8 ** 17) * (8 ** 13 + 8 ** 16))
n = oct(a)[2:]
print(n)
n = n.replace('7', '0')
n = n[3:]
print(n)

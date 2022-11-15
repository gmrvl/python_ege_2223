a = (16**44) * (16**30) - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
n = hex(a)[2:]
n = n.replace('f', '0')
n = n[3:]
print(n)
first = n.find('e')
n = n[first:]
print(n)
print(n.count('0'))


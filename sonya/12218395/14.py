s = 4**2018 + 2**2017 - 5
s = bin(s)[2:]
print(s.count('1'))
#
s = 4**2018 + 2**2017 - 5
count = 0
while s > 0:
    if s % 2 == 1:
        count += 1
    s //= 2
print(count)

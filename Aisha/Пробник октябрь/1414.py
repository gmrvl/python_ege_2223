s = 36 ** 8 + 6 ** 20 - 12

count = 0
while s != 0:
   if s % 6 == 5:
      count += 1
   s //= 6
print(count)

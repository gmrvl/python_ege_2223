s = 49**6 + 7**19 - 21

count = 0
while s > 0:
   if s % 7 == 0:
       count += 1
   s //= 7
print(count)
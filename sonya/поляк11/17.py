file = open('17-1.txt')
minsrarf = 10000
count = 0

min15 = 10000
for n in file:
    n = int(n)
    if n > 0 and n % 15 == 0:
        min15 = min(min15, n)

file = open('17-1.txt')
last = int(file.readline())
for n in file:
     n = int(n)
     if abs(n) % 2 == 1 and abs(last) % 2 == 1:
         srarf = (n + last)//2
         if srarf >= min15:
             count += 1
             minsrarf = min(minsrarf, srarf)
     last = n
print(count, minsrarf)

file = open('6752.txt')

count = 0
maxSum = 0
count3 = 0

for digit in file:
    digit = int(digit)
    if digit % 3 == 0:
        count3 += 1

file = open('6752.txt')
last = int(file.readline())

for digit in file:
    digit = int(digit)
    s = last + digit
    if (s < count3) and (last < 0 or digit < 0):
        count += 1
        maxSum = max(maxSum, s)
print(count, maxSum)

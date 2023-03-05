file = open('107_17.txt')

count = 0
max_pair = 0
min21 = 10**10

for i in file:
    digit = int(i)
    if digit % 21 == 0 and digit < min21:
        min21 = digit

file = open('107_17.txt')
last = int(file.readline())

for line in file:
    digit = int(line)
    if digit % min21 == 0 or last % min21 == 0:
        count += 1
        max_pair = max(last + digit, max_pair)
    last = digit
print(max_pair, count)

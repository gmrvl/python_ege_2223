file = open('48438.txt')

count = 0
max_sum = 0
min_7 = 0

for digit in file:
    digit = int(digit)
    if abs(digit) % 10 == 7:
        min_7 = min(min_7, digit)
print(min_7)

file = open('48438.txt')
last = int(file.readline())
# min_7 = min_7 ** 2
for digit in file:
    digit = abs(int(digit))
    if ((digit % 10 == 7) and (last % 10 != 7)) or ((digit % 10 != 7) and (last % 10 == 7)):
        sq = last ** 2 + digit ** 2
        if sq < (min_7 ** 2):
            print(last, digit)
            count += 1
            max_sum = max(sq, max_sum)
    last = digit
print(count, max_sum)


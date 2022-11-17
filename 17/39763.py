file = open('39763.txt')

count = 0
max_sum = 0
first = int(file.readline())
second = int(file.readline())

for digit in file:
    third = int(digit)
    summ = first + second + third
    max_digit = max(first, second, third)
    min_digit = min(first, second, third)
    aver_digit = summ - max_digit - min_digit
    if max_digit**2 < min_digit**2 + aver_digit**2:
        count += 1
        if summ > max_sum:
            max_sum = summ
    first = second
    second = third
print(count, max_sum)

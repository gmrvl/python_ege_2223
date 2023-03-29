file = open('р26.2.txt')
numbers = [int(i) for i in file]
ns = set(numbers)
count = 0
maxsumm = 0
for x in range(0, len(numbers) - 1):
    for y in range(x + 1, len(numbers)):
        if (numbers[x] % 2 == 0 and numbers[y] % 2 != 0) or (numbers[y] % 2 == 0 and numbers[x] % 2 != 0):
            summ = numbers[x] + numbers[y]
            if summ in ns:
                count += 1
                maxsumm = max(maxsumm, summ)
print(count, maxsumm)
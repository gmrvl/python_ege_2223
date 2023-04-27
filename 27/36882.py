file = open('36882-b.txt')

n = int(file.readline())
data = []
for i in file:
    x, y = map(int, i.split(' '))
    if y % 2 == 1:
        data.append([x, y])

max_sum = 0
min_sum = 0

min_pair_ch_n = 20000
min_pair_n_ch = 20000
min_pair_n_n = 20000
for i in data:
    a = max(i)
    b = min(i)
    max_sum += a
    min_sum += b
    if a % 2 == 1 and b % 2 == 1:
        min_pair_n_n = min(min_pair_n_n, (a + b))
    elif a % 2 == 0 and b % 2 == 1:
        min_pair_ch_n = min(min_pair_ch_n, (a + b))
    elif a % 2 == 1 and b % 2 == 0:
        min_pair_n_ch = min(min_pair_n_ch, (a + b))

print(max_sum, min_sum)
print(max_sum + min_sum - min_pair_n_n)
print(max_sum + min_sum - min_pair_ch_n - min_pair_n_ch)


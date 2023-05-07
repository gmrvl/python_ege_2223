f = open('37162A.txt')

n = int(f.readline())
nums = list(map(int, f.readlines()))
min_len, max_sum = n, 0

for i in range(len(nums)):
    for j in range(i, len(nums)):
        s = sum(nums[i:j + 1])
        if s % 89 == 0 and s > max_sum:
            max_sum, min_len = s, j - i + 1
        if s % 89 == 0 and s == max_sum:
            min_len = min(min_len, j - i + 1)
print(min_len)
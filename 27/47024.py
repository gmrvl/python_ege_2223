file = open('47024A.txt')

n = file.readline()

count = 0
curr_sum = 0
curr = []

for i in file:
    i = int(i)
    curr.append(i)
    curr_sum += i
    if curr_sum == 1111:
        count += 1
    elif curr_sum > 1111:
        while curr_sum > 1111:
            curr_sum -= curr.pop(0)
        if curr_sum == 1111:
            count += 1
print(count)

file = open('46982.txt').read()

group_count = 0
count = 0
for i in file:
    if i == 'E':
        count += 1
        if count >= 12:
            group_count += 1
        count = 1
    elif i == 'F':
        count = 0
    else:
        if count > 0:
            count += 1
print(group_count)



file = open('24.txt').readline()
maxcount = count = 0
for i in range(len(file) - 1):
    if file[i] not in 'RQS' or file[i+1] not in 'RQS':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 1
print(maxcount)
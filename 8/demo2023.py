count = 0
for i in range(8**4, 8**5):
    i = oct(i)[2:]
    if i.count('6') == 1:
        s = i.index('6')
        if s == 0:
            if int(i[1]) % 2 == 0:
                count += 1
        elif s == 4:
            if int(i[3]) % 2 == 0:
                count += 1
        else:
            if int(i[s+1]) % 2 == 0 and int(i[s-1]) % 2 == 0:
                count += 1
print(count)

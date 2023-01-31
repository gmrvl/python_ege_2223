count = 0
for i in range(12345678, 876543211):
    i = str(i)
    if len(i) < 9:
        i = '0' + i
    if i.count('0') == 1 and i.count('1') == 1 and i.count('2') == 1 and i.count('3') == 1 and i.count(
        '4') == 1 and i.count('5') == 1 and i.count('6') == 1 and i.count('7') == 1 and i.count('8') == 1 and i.count(
        '9') == 0:
        if i.find('0') == 7:
            if i[0] < i[1] < i[2] < i[3]:
                print(i)
                count += 1
print(count)

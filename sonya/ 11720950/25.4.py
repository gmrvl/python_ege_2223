count = 0
i = 500000
while count < 5:
    min_dell_8 = i
    for dell in range(2, int(i ** 0.5)):
        if i % dell == 0 and dell != 8:
            dell2 = i // dell
            if dell % 10 == 8 or (dell2 % 10) == 8:
                print(i, dell, dell2)
                count += 1
    i += 1
# 1 вариант - проходиться по всем делителям и если нашли делитель меньше, то заменить
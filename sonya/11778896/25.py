count = 0
i = 460000001
while count < 5:
    dels = []
    sqn = int(i ** 0.5)
    for d in range(2, sqn + 1):
        if i % d == 0:
            d2 = i // d
            if d == d2:
                dels.append(d)
            else:
                dels.append(d)
                dels.append(d2)
        # if len(dels) > 10:
        #     break

    if len(dels) >= 5:
        dels.sort()
        count += 1
        print(dels[-5])
    i += 1
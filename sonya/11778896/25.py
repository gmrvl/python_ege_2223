count = 0
i = 460000001
while count < 5:
    dels = []
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            if d == (i // d):
                dels.append(d)
            else:
                dels.append(d)
                dels.append(i // d)
        # if len(dels) > 10:
        #     break

    if len(dels) >= 5:
        dels.sort()
        count += 1
        print(dels[-5])
    i += 1
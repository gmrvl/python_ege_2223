for i in range(45000000, 50000001):
    sqn = int(i**0.5)
    arr = []
    for dell in range(1, sqn + 1):
        if i % dell == 0:
            dell2 = i // dell
            if dell == dell2:
                if dell % 2 != 0:
                    arr.append(dell)
            else:
                if dell % 2 != 0:
                    arr.append(dell)
                if dell2 % 2 != 0:
                    arr.append(dell2)
            if len(arr) > 5:
                break
    if len(arr) == 5:
        print(i)

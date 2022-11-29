for n in range(289123456, 389123457):
    sqn = int(n ** 0.5)
    dels = []
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dels.append(dell)
            else:
                dels.append(dell)
                dels.append(dell2)
            if len(dels) > 3:
                break
    if len(dels) == 3:
        print(n, max(dels))
n = 500000 + 1
count = 0

#while count < 5:
 #   sqn = int(n ** 0.5)
 #   dells = []
 #   for dell in range(9, sqn + 1):
  #      if n % dell == 0:
  #          if dell % 10 == 8:
   #             print(n, dell)
   #             count += 1
   #             break
   #         elif (n // dell) % 10 == 8:
   #             print(n, n // dell)
    #            count += 1
    #            break
   # n += 1

while count < 5:
    sqn = int(n ** 0.5)
    dells = []
    for dell in range(9, sqn + 1):
        if n % dell == 0:
            if dell % 10 == 8:
                dells.append(dell)
            elif (n // dell) % 10 == 8:
                dells.append(n // dell)
    if len(dells) != 0 and dell == sqn:
        print(n, min(dells))
        count += 1
    n += 1

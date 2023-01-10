for x in range(1, 1007):
    for y in range(0, 9):
        x = str(x)
        y = str(y)
        s = '3' + x + '52' + y
        dells = []
        sqs = int(s) ** 0.5
        if sqs != int(sqs):
            continue
        sqs = int(sqs)
        dells = [sqs]
        s = int(s)
        for dell in range(2, sqs + 1):
            if s % dell == 0:
                dells.append(dell)
                dells.append(s // dell)
        print(s, max(dells))


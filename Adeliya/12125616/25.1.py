for i in range(110203, 110246):
    sq = i**0.5
    if sq!=int(sq):
        continue
    sq = int(sq)
    a=[sq]
    for dell in range(2,sq):
        if i % dell == 0:
            a.append(dell)
            a.append(i//dell)
        if len(a)>4:
          break
    if len(a)==4:
        print()


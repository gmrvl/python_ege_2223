for i in range(95632,95651):
    sq=int(i**0.5)
    dells=[]
    for dell in range(1, sq + 1):
        if i % dell == 0:
            if dell%2!=0:
                dells.append(dell)
            if (i//dell != dell) and ((i//dell) % 2 !=0):
                dells.append(i//dell)
        if len(dells) > 6:
            break
    if len(dells)==6:
        dells=sorted(dells)
        print(dells)



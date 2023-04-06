for i in range(125256, 125331):
    sq=int(i**0.5)
    a=[]
    for dell in range(1,sq+1):
        if i % dell ==0:
            if dell%2==0:
              a.append(dell)
            if ((i//dell)%2==0) and (i//dell != dell):
              a.append(i//dell)
        if len(a) >6:
            break
    if len(a)==6:
        a=sorted(a)
        print(a)

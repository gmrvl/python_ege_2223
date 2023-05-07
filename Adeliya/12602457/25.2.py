count=0
for i in range(245690, 245757):
    count+=1
    sq=int(i**0.5)
    dells=[]
    for dell in range(1,sq+1):
        if i%dell==0:
            dell2=i//dell
            if dell==dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells)==2:
        print(count,i)



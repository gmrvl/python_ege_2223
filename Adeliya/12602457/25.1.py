n=452022
count=0
while count < 5:
    sq=int(n**0.5)
    dells=[]
    for dell in range(2,sq+1):
        if n%dell==0:
            dell2=n//dell
            if dell==dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)



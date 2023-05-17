for i in range(273,10**8,273):
    i=str(i)
    if i[0]=='1' and i[1]=='2' and i[4:6]=='36' and i[-1]=='1':
        i=int(i)
        print(i,i//273)
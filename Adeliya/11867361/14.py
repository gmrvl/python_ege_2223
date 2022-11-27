for i in range(0,10):
    a=int('8'+str(i)+'834',16)
    b=int('44'+str(i)+'27',16)
    if (a+b)%23==0:
        print((a+b)//23)

for x in '0123456789':
    s=int('8'+x+'834',16)+int('44'+x+'27',16)
    if s%23==0:
        print(s//23)
        break

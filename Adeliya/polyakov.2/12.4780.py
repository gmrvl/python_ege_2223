for i in range(251,1000):
    a='5'*i
    while '55555' in a:
        a=a.replace('55555','88',1)
        a=a.replace('888','555',1)
    print(i,a.count('5'))


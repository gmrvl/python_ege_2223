max1=0
for i in range(200,300):
    a='1'*i
    while '1111' in a:
        a=a.replace('1111','22',1)
        a=a.replace('222','1',1)
        print(i,a.count('1'))

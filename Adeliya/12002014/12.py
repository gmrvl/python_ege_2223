a='1'*10 +'2'*3
while '11' in a:
    if '112' in a:
        a=a.replace('112','6',1)
    else:
        a=a.replace('11','3',1)
print(a)


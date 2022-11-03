a='5'*54 + '7'
while '722' in a or '557' in a:
    if '722' in a:
        a=a.replace('722','57',1)
    else:
        a=a.replace('557','72',1)
print(a)
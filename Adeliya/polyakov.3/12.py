a='9'*96
while '22222' in a or '9999' in a:
    if '22222' in a:
        a=a.replace('22222','99',1)
    else:
        a=a.replace('9999','2',1)
print(a)
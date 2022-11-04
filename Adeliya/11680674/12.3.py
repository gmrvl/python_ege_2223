a='1'*40+'2'*40
while '111' in a:
    a=a.replace('111','2',1)
    a=a.replace('222','1',1)
print(a)
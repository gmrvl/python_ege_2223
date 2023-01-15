a='0'+'1'*12+'2'*15+'3'*17
while '01' in a or '02' in a or '03' in a:
     a=a.replace('01','103',1)
     a=a.replace('02','10',1)
     a=a.replace('03','210',1)

print(a.count('2'))

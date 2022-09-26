s= '1'*15 + '2'*10 + '3'*60
while '30' in s or '101' in s or '202' in s:
    s=s.replace('30','01',1)
    s=s.replace('101','02',1)
    s=s.replace('202','03',1)
print(s.count('1'))
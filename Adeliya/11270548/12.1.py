s = '1'*77
while '111' in s:
    if "111" in s:
        s=s.replace('111','2',1)
        s=s.replace('222','3',1)
        s=s.replace('333','1',1)
print(s)
s = '1' * 77
while '111' in s:
    s = s.replace('111', '2', 1)
    s =s.replace('222', '11', 1)
print(s)
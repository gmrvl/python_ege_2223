s = '7' * 85
while '333' in s or '777' in s:
    if '333' in s:
        s = s.replace('333', '7',1)
    else:
        s = s.replace('777', '3', 1)
print(s)
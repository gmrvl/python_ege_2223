prost = []
for i in range(1,1000):
    sqi = int(i**0.5)
    dells = 0
    for d in range(1,sqi + 1):
        if i % d == 0:
            if d == (i // d):
                dells += 1
            else:
                dells += 2
    if dells == 2:
        prost.append(i)
set(prost)
count = 0
for n in range(10, 100):
    s = '1' + n * '0'
    while '10' in s:
        if '10' in s:
            s = s.replace('10', '001')
        if '1' in s:
            s = s.replace('1', '01')
    if len(s) in prost:
        count += 1
print(count)
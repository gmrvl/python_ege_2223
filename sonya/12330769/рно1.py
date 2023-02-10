#Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.
file = open('рно1.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if char == 'a':
        if last == 'd':
            maxcount = max(maxcount,count)
            count = 1
        else:
            count += 1
    elif char == 'd':
        if last == 'a':
            maxcount = max(maxcount,count)
            count = 1
        else:
            count += 1
    else:
        count += 1
    last = char
print(maxcount)

f = open('рно1.txt')
s = f.readline()
s = s.replace('ad', 'a d')
s = s.replace('da', 'd a')
w = list(map(len, s.split()))
print(max(w))

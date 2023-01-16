file = open('24.5.txt').read()
count = [0] * 26
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last = ''
for i in file:
    if len(last) < 3:
        last += i
    else:
        if last[0] == last[2]:
            a = alth.find(last[1])
            count[a] += 1
        last = last[1:] + i
maxx = 0
maxChar = ''
for i in range(26):
    if count[i] > maxx:
        maxx = count[i]
        maxChar = alth[i]
print(maxChar)
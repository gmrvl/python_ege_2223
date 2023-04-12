file=open('24.4.txt')
max_r=0
alth='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for string in file:
    if string.count('G') < 25:
        for i in alth:
            r = string.rfind(i) - string.find(i)
            if r > max_r:
                max_r = r
print(max_r)

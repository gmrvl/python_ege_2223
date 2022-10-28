# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида согласная + гласная.
file=open('24.12.txt')
count=0
maxcount=0
s=['C','D','F']
g=['A','O']
str=str(file.readline)
for i in range(0,len(str)):
    if (str[i] in s) and (str[i+1] in g):
        count+=2
    else:
        if count>maxcount:
            maxcount=count
        count=0
print(maxcount)


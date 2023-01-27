file = open('inf_26_04_21_27a.txt')
n = file.readline()


summbolsh = 0
summmensh = 0
min1 = 100000 #оба нечетн
min2 = 100000 # наим неченое наиб четное
min3 = 100000 # наим четное наиб нечетное


for i in file:
    a, b = i.split('  ')
    a, b = int(a), int(b)
    if a % 2 != 0:
        summbolsh += max(a, b)
        summmensh += min(a, b)
        if b % 2 != 0:
            min1 = min(min1, a + b)
        if max(a, b) % 2 == 0:
            min2 = min(min2, a + b)
        if min(a, b) % 2 == 0:
            min3 = min(min3, a + b)
if summmensh % 2 == 0 and summbolsh % 2 != 0:
    print(summbolsh + summmensh)
elif summmensh % 2 != 0 and summbolsh % 2 != 0:
    print(summbolsh + summmensh - min2)
elif summmensh % 2 != 0 and summbolsh % 2 == 0:
    print(summbolsh + summmensh - min1)
elif summmensh % 2 == 0 and summbolsh % 2 == 0:
    print(summbolsh + summmensh - min3)


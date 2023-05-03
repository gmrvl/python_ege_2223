#Определите количество троек, в которых для каждого числа тройки сумма цифр в чётных разрядах нацело делится на
# сумму цифр в нечётных разрядах. В ответе запишите два числа: сначала количество найденных троек
# , а затем – минимальную сумму элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
file = open('17-343.txt')
count = 0
minsumm = 30000
plast = int(file.readline())
last = int(file.readline())
for n in file:
    n = int(n)
    chplast = 0
    nchplast = 0
    for i in range(0, len(str(plast))):
        plast = str(plast)
        if i % 2 == 0:
            chplast += int(plast[i])
        else:
            nchplast += int(plast[i])
    if nchplast > 0 and chplast > 0:
        if chplast % nchplast == 0:
            plasts = 1
        else:
            plasts = 0
    chlast = 0
    nchlast = 0
    for i in range(0, len(str(last))):
        last = str(last)
        if i % 2 == 0:
            chlast += int(last[i])
        else:
            nchlast += int(last[i])
    if nchlast > 0 and chlast > 0:
        if chlast % nchlast == 0:
            lasts = 1
        else:
            lasts = 0
    chn = 0
    nchn = 0
    for i in range(0, len(str(n))):
        n = str(n)
        if i % 2 == 0:
            chn += int(n[i])
        else:
            nchn += int(n[i])
    if nchn > 0 and chn > 0:
        if chn % nchn == 0:
            ns = 1
        else:
            ns = 0
    if (ns + lasts + plasts) == 3:
        count += 1
        minsumm = min(minsumm, int(n) + int(last) + int(plast))
    plast = last
    last = n
print(count, minsumm)

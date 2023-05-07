#Определите количество троек, в которых для каждого числа тройки сумма цифр в чётных разрядах нацело делится на
# сумму цифр в нечётных разрядах. В ответе запишите два числа: сначала количество найденных троек
# , а затем – минимальную сумму элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
file = open('17-343.txt')
count = 0
minsumm = 30000
plast = int(file.readline())
last = int(file.readline())
digits = [plast, last, '']
for n in file:
    digits[2] = int(n)
    flag = True
    for d in digits:
        ch = 0
        nch = 0
        strd = str(d)
        diff = d
        for i in range(0, len(str(d))):
            if i % 2 == 0:
                ch += diff % 10
            else:
                nch += diff % 10
            diff //= 10
        if nch > 0 and ch > 0:
            # if len(strd) % 2 == 0:
            #     if ch % nch != 0:
            #         flag = False
            # else:
            if nch % ch != 0:
                flag = False
        else:
            flag = False
    if flag:
        count += 1
        minsumm = min(minsumm, sum(digits))
    digits[0] = digits[1]
    digits[1] = digits[2]

print(count, minsumm)

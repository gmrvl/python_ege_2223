
for i in range(0, 10):
    summ = int('26' + str(i) + '98') + int('4' + str(i) + '296')
    if summ % 34 == 0:
        print(i)
        break

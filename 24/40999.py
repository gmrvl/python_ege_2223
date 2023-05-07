# проходим по файлу, смотрим, чтобы не было Е
# если встрели Е - прерываем цепочку, и смотрим, сколько А встречалось в цепочке. нужна переменная countA
# если встретила А - countA += 1 (когда обрываем цепочку - countA обнуляем)
file = open('40999.txt').read()

maxcount = 0
countA = 0
string = ''
for i in file:
    if i != 'E':
        string += i
for i in string:
    if string.count('A') >= 3:
        countA += 1
    else:
        if countA > maxcount:
            maxcount = countA
    countA = 0
print(maxcount)

#пределите и запишите в ответе сначала количество пар элементов последовательности,
#для которых произведение элементов кратно 26,
#затем максимальную из сумм элементов таких пар.

file = open('17.1.txt')

strins = [int(i) for i in file]
count = 0
maxsumm = 0

for x in range(0,len(strins) - 1):
    for y in range(x + 1, len(strins)):
        if strins[x]*strins[y] % 26 == 0:
            count += 1
            maxsumm = max(maxsumm, strins[x] + strins[y])
print(count,maxsumm)
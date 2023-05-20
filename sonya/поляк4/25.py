#Найдите числа большие 2000000, сумма и произведение делителей которых нечётны. В ответе укажите наименьшие 6 таких чисел,
# количество делителей которых больше 30. В ответе запишите найденные числа в порядке возрастания,
# справа от каждого числа запишите его наибольший делитель, являющийся простым числом.


n = 2000000 + 1
count = 0
ns=[]
while count < 6:
    sqn = int(n**0.5)
    sumdells = 0
    ndells = 1
    dells = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                sumdells += dell
                ndells *= dell
                dells += 1
            else:
                sumdells += dell
                sumdells += dell2
                ndells *= dell
                ndells *= dell2
                dells += 2
    if dells > 30 and ndells % 2 == 1 and sumdells % 2 == 1:
        count += 1
        ns.append(n)
    n += 1
prost = []
for i in range(1,1000):
    sqn = int(i ** 0.5)
    dells = []
    for dell in range(2, sqn + 1):
        if i % dell == 0:
            dell2 = i // dell
            if dell == dell2:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if len(dells) == 0:
        prost.append(i)
print(prost)
prost = set(prost)
for i in ns:
    sqn = int(i ** 0.5)
    dells = []
    for dell in range(1, sqn + 1):
        if i % dell == 0:
            dell2 = i // dell
            if dell == dell2 and dell in prost:
                dells.append(dell)
            else:
                if dell in prost:
                    dells.append(dell)
                if dell2 in prost:
                    dells.append(dell2)
    print(i, max(dells))




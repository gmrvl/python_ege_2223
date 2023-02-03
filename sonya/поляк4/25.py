#Найдите числа большие 2000000, сумма и произведение делителей которых нечётны. В ответе укажите наименьшие 6 таких чисел,
# количество делителей которых больше 30. В ответе запишите найденные числа в порядке возрастания,
# справа от каждого числа запишите его наибольший делитель, являющийся простым числом.


n = 2000000 + 1
count = 0

while count < 6:
    sqn = int(n**0.5)
    dells = 0
    ndells = 0
    for dell in range(1, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell == dell2:
                dells += 1
            else:
                dells += 2
            if dell % 2 == 1 and dell2 % 2 == 1:
                if dell == dell2:
                    ndells += 1
                else:
                    ndells += 2
    if dells > 30 and dells == ndells:
        count += 1
        print(n)
    n += 1




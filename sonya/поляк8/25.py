#(№ 5227) Пусть N(k) = 500 000 000 + k, где k – натуральное число. Найдите пять наименьших значений k, при
# которых N(k) нельзя представить в виде произведения трёх натуральных чисел, больших 1. В
# отвеne запишите найденные значения k в порядке убывания, справа от каждого значения запишите на
# ибольший делитель N(k), не равный самому числу.


n = 500000000
for k in range(1, 10000):
    n += k
    sqn = int(n**0.5)
    dells = [1]
    for dell in range(2, sqn + 1):
        if n % dell == 0:
            dell2 = n // dell
            if dell2 == dell:
                dells.append(dell)
            else:
                dells.append(dell)
                dells.append(dell2)
    if 0 < len(dells) < 4:
        print(k, max(dells))
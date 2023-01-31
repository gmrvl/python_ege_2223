# 123*НЧ56, делящиеся на 206 без остатка

H = [1, 3, 5, 7, 9]
CH = [0, 2, 4, 6, 8]
z = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in z:
    for n in H:
        for ch in CH:
            s = '123' + str(i) + str(n) + str(ch) + '56'
            s = int(s)
            if s % 206 == 0:
                print(s, s // 206)

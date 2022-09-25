# очень тупое решение, НИКОГДА не используйте тройную вложенность цикла! НИ-КОГ-ДА (если только вам вообще ничего в голову больше не приходит и вы перебираете очень мало цифр - до ста)
res = False
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            s = '0' + '1' * a + '2' * b + '3' * c
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 40 and s.count('2') == 10 and s.count('3') == 8:
                print(a)
                res = True
                break
        if res:  # if res == True:
            break
    if res:
        break

chisla = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','F']


for x in chisla:
    s10 = int(('8' + str(x) + '834'), 16) + int(('44' + str(x) + '27'), 16)
    if s10 % 23 == 0:
        print(s10 // 23)
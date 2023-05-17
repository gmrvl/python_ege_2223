file = open('26-85.txt')
n = int(file.readline())
f = []
fg = [] #места занятые участниками из другого города
fn = []
for i in file:
    ryad, mesto, gorod = map(int, i.split())
    f.append([ryad, mesto, gorod])
    if gorod == 0:
        fn.append([ryad, mesto])
    else:
        fg.append([ryad, mesto])
fg = sorted(fg)
fn = sorted(fn)
maxx = 0
for i in range(1,len(fg)):
    if fg[i-1][0] == fg[i][0]:
        if fg[i][1] - fg[i - 1][1] == 101:
            for j in range(0,len(fn)):
                n = 0
                if fn[j][0] == fg[i][0]:
                    n += 1
        if n == 500:
            maxx = fg[i][0]
print(maxx)



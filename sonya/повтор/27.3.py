file = open('3-27-B_2.txt')
N = int(file.readline())
maxx = -1
max7 = 0
max2 = 0
max14 = 0
for i in file:
    i = int(i)
    if max14 < i and i % 14 == 0:
        max14 = i
    elif max7 < i and i % 7 == 0:
        max7 = i
    elif max2 < i and i % 2 == 0:
        max2 = i
    elif maxx < i:
        maxx = i
print(max(max7*max2, max14*maxx))
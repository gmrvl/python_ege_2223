f = open("36882-b.txt")
n = int(f.readline())
sum0 = 0
sum1 = 0
min1 = 20001
min2 = 20001
min3 = 20001
for i in f:
    x, y = i.split()
    x = int(x)
    y = int(y)
    if y % 2 == 1:
        if x > y:
            sum1 = sum1 + y
            sum0 = sum0 + x
            if (y % 2 == 1) and (x % 2 == 1) and ((x + y) < min1):
                    min1 = x + y
            if (y % 2 == 0) and (x % 2 == 1) and ((x + y) < min2):
                    min2 = x + y
            if (y % 2 == 1) and (x % 2 == 0) and ((x + y) < min3):
                    min3 = x + y
        else:
            sum1 = sum1 + x
            sum0 = sum0 + y
            if (y % 2 == 1) and (x % 2 == 1) and ((x + y) < min1):
                min1 = x + y
            if (x % 2 == 0) and (y % 2 == 1) and ((x + y) < min2):
                    min2 = x + y
            if (x % 2 == 1) and (y % 2 == 0) and ((x + y) < min3):
                    min3 = x + y
if (sum0 % 2 == 0) and (sum1 % 2 == 1):
    print(sum0 + sum1)
elif (sum0 % 2 == 1) and (sum1 % 2 == 0):
    if min1 < min2 + min3:
        print(sum0 + sum1 - min1)
    else:
        print(sum0 + sum1 - min2 - min3)
elif (sum0 % 2 == 1) and (sum1 % 2 == 1):
    if min2 < min3 + min1:
        print(sum0 + sum1 - min2)
    else:
        print(sum0 + sum1 - min3 - min1)
elif (sum0 % 2 == 0) and (sum1 % 2 == 0):
    if min3 < min2 + min1:
        print(sum0 + sum1 - min3)
    else:
        print(sum0 + sum1 - min2 - min1)

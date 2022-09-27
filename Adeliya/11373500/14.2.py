s = 2 * 216**6 + 3 * 36**9 - 432
count=0
while s!=0:
    if s % 6 == 5:
        count+=1
    s//=6
print(count)


for i in range(100,1000):
    n = str(i)
    a = n[:2] + n[0:2]
    b = n[0:2] + n[2:]
    if a > b:
        n = b + a
    else:
        n = a + b
    if n == 1216 :
       print (i)
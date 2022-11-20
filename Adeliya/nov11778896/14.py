a=6*343**5 + 5*49**7 - 50
count=0
while a!=0:
    if a%7==6:
        count+=1
    a//=7
print(count)


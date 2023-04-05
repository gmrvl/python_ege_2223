a=125**4 + 25**8 - 30
count=0
while a!=0:
    if a%5==4:
        count+=1
    a//=5
print(count)
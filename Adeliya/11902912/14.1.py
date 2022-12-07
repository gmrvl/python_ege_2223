a= 25**6 + 5**18 - 5
count=0
while a!=0:
    if a%5==4:
        count+=1
    a//=5
print(count)
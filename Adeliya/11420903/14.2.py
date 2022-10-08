a = 81**17 + 3**24 - 45
count=0
while a!=0:
    if a%9==8:
     count+=1
    a//=9
print(count)

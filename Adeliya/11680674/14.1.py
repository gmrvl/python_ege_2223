a=9**8*3**20-3**10-3
count=0
while a!=0:
    if a%3==2:
        count+=1
    a//=3
print(count)
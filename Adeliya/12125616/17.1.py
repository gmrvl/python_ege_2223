file=open('17.1.txt')
count=0

k2=0
k13=0
k26=0

max26=0
max13=0
max2=0

for i in file:
    i=int(i)
    if i%13==0 and i%2==0:
        k2+=1
        k13+=1
        k26+=1
        if i>max26:
            max26=i
    elif i%13==0 and i%2!=0:
        count+=k2
        k13+=1
        if i>max13:
            max13=i
    elif i%13!=0 and i%2==0:
        count+=k13
        k2+=1
        if i>max2:
            max2=i
    elif i%13!=0 and i%2!=0:
        count+=k26

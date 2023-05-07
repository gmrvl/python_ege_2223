file=open('inf_26_04_21_27a.txt')
n=int(file.readline())

for i in file:
    x,y=i.split()
    x=int(x)
    y=int(y)
    if y%2==1:

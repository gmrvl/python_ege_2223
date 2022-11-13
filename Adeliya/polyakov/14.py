a=8**20+((8**22-8**17)*(8**13+8**16))
n=str(oct(a)[3:])
if '7'in n:
    n=n.replace('7','0')
print(n)

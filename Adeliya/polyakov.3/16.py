import sys

sys.setrecursionlimit(3600)


def F(n):
    if n==1:
        return 1
    if n>1:
        return (2*n - 1)*F(n - 1)
print(F(3516)/F(3513))

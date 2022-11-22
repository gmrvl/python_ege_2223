
def f(x, A):
    return ((x in A) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in A))

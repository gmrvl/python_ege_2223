P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A1 = []
def F(x, A):
    return ((x in A1) <= (x in P) ) and ( (x in Q) <= (not(x in A1)))

for A in range(1000):
    OK = True
    for x in range(1000):
        if F(x, A) != 1:
            OK = False
    if OK:
        A1.append(A)
print(len(A1))

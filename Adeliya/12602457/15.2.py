# (A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 18)))

def Dell(n, m):
    if n % m == 0:
        return True
    else:
        return False

def F(x, A):
    return ((A < 50) and (not Dell(x, A)) <= (Dell(x, 10) <= (not Dell(x, 18))))


for A in range(1, 1000):
    OK = True
    for x in range(0, 1000):
        if not F(x, A):
            OK = False
            break
    if OK:
        print(A)

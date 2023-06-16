for n in range (1, 100):
    def F(n):
        if n == 2:
            return 1
        elif n == 1:
            return 2
        elif n > 2:
            return F(n - 2) + F(n - 1)
        print(n)
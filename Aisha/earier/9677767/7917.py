for i in range(100, 1000):
    # математический способ
    third = i % 10
    first = i // 100
    second = (i // 10) % 10
    # строковый способ
    n = str(i)
    first = int(n[0])
    second = int(n[1])
    third = int(n[2])
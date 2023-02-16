for x in range(0,9):
    s = int('88' + str(x) + '4' + str(x), 9) + int('7' + str(x) + '344', 9)
    if s % 67 == 0:
        print(s // 67)
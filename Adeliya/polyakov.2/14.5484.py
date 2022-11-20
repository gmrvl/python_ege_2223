for i in range(0, 10):
    a = int('9759' + str(i), 17)
    b = int('3' + str(i) + '108', 17)
    if (a + b) % 11 == 0:
        print((a + b) // 11)
        break
  
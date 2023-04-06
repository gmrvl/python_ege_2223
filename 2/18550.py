for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((y <= z) or ((not x) and w)) == (w == z)) == 1:
                    print(x, y, z, w)


def F(w, z, y, x): #демонстрация неправильного ответа
    return (((y <= z) or ((not x) and w)) == (w == z))


print(F(1, 1, 0, 0))
print(F(0, 0, 0, 1))
print(F(0, 1, 1, 1))  # тут будет false

# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы A.
maxx = 0
file = open('24 (12).txt').readline().split('A')
for i in range(0, len(file) - 1):
    if len(file[i]) + len(file[i + 1]) + 1 > maxx:
        maxx = len(file[i]) + len(file[i + 1]) + 1
print(maxx)

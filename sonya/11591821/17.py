file = open('17.txt')
last = 0
count = -1 #так как первое число в файле не делится на 3, но last будет раняться 0 и тогда программа почитает count += 1, а нам это не нужно
for string in file:
    if int(string) % 3 == 0 or int(last) % 3 == 0:
        count += 1
    last = string
print(count)
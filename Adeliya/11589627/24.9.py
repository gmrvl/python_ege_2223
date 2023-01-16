file = open('24.9.txt').read() # переписать то что есть в 11 задачку

count = 0  # количество символов в цепочке
string = ''
for i in file:
    if i == 'F':
        string = ''
    # если встретилась е - надо начать ИЛИ закончить цепочку
    else:
        string += i
        # if string.count('E') >= 3:
            count += 1
            # if count > maxcount:
            #     maxcount = count
if count > maxcount:
    maxcount = count
print(maxcount)

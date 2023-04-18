file = open('35998.txt')
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_dist = 0
for i in file:
    if i.count('A') < 25:
        for k in alth:
            max_dist = max(i.rfind(k) - i.find(k), max_dist)
print(max_dist)

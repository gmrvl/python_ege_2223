#Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.

file = open('рно3.txt')
s = file.readline()
s = s.replace('KL', 'K L')
s = s.replace('LK', 'L K')
lenn = list(map(len, s.split()))
print(max(lenn))
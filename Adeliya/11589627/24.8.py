file=open('24.8.txt').read()

count=0
countA = 0 # количество букв А которые уже есть в строке.
maxcount=0

for i in file:
    if i=='A':

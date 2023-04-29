file = open('36037.txt').readline()

stringg = file.replace('XZZY', '*')
data = stringg.split('*')
print(len(max(data)) + 6)

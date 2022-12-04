#задание25
n = []
for i in range(10068, 17000000):
    number = str(i)
    if number.count('1') != 0:
        if number.find('6') - number.find('1') >= 3 and number.find('8') - number.find('6') == 1:
            number = int(number)
            if number % 161 == 0:
                n.append(number)

print(len(n))
print(n[0], n[499], n[999])
print(n[0]//161, n[499]//161, n[999]//161)
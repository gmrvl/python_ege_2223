for x in '0123456789ABCDE':
    for y in '0123456789ABCDEFG':
        s=int('131'+x+'1',15)+int('13'+y+'3',17)
        if s%11==0:
            print(s//11)
            
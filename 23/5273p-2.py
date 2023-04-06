def f(x, y, commands):
    if x > y:
        return 0
    elif x == y:
        if commands.count('1') <= 4 and commands.count('2') >= 2 and commands.count('3') == 5:
            return 1
        else:
            return 0
    else:
        return f(x * 5, y, commands + '1') + f(x * 3, y, commands + '2') + f(x + 45, y, commands + '3')


print(f(1, 2970, ''))

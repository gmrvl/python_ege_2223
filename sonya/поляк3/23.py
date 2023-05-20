def f(x,y):
    if x == y:
        return True
    if x < y:
        return False
    return f(x//10 + x % 10, y) or f(x//10 * x % 10, y)
count = 0
for x in range(10, 100):
    if f(x,8):
        count += 1
print(count)

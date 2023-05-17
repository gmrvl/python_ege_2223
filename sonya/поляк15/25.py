from fnmatch import*
n = 700000 + 1
count = 0
while count < 5:
    if n % 13 == 0 and not(fnmatch(str(n), '*0??3*') or fnmatch(str(n), '*4??2') or fnmatch(str(n), '*1*')):
        count += 1
        print(n)
    n += 1

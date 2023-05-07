for i in range(103, 123456789, 103):
    n = str(i)
    na = list(n)
    flag = True
    for j in '0123456789':
        if n.count(j) > 1:
            flag = False
            break
    if flag:
        if na == sorted(na):
            print(i, i // 103)
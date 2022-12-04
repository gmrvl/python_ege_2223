for i in range(1000000, 2000001):
    sq=int(i**0.5)
    count=0
    for dell in range(1,sq):
        if i % dell ==0:
            if i//dell - dell <= 100:
                count+=1
                if count>=3:
                    print(i)
                    break

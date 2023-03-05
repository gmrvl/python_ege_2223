file = open('47230.txt')
n = file.readline()
arr = [int(i) for i in file]
arr = sorted(arr, reverse=True)
gift = [arr[0]]

for i in arr[1:]:
    if gift[-1] - i >= 3:
        gift.append(i)
print(gift[-1], len(gift))

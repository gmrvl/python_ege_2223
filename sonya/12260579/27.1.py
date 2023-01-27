file = open('28130_B.txt')
n = file.readline()

ost_m_50 = [0] * 51
ost_b_50 = [0] * 80

for string in file:
    string = int(string)
    if string <= 50:
        ost_m_50[string % 80] += 1
    if string > 50:
        ost_b_50[string % 80] += 1

count = 0

for ost in range(1, 51):
    count += ost_m_50[ost] * ost_b_50[80 - ost]

# for ost in range(1, 80):
# count += ost_m_50[0] * ost_b_50[80 - ost]
count += ost_b_50[0] * (ost_b_50[0] - 1) // 2
count += ost_b_50[40] * (ost_b_50[40] - 1) // 2

for ostii in range(1, 40):
    count += ost_b_50[ostii] * ost_b_50[80 - ostii]

print(count)

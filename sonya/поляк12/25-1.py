def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_permutations(number):
    s_num = str(number)
    result = set()
    for i in range(len(s_num)):
        for j in range(i + 1, len(s_num)):
            if s_num[i] == '0' or s_num[j] == '0' or s_num[i] == s_num[j]:
                continue
            swap_nums = list(s_num)
            swap_nums[i], swap_nums[j] = swap_nums[j], swap_nums[i]
            result.add(int(''.join(swap_nums)))
    return result

found = 0
number = 1411111111

while found < 5:
    number += 2
    if not (is_prime(number) and '0' not in str(number)):
        continue
    primes_permutations = {perm for perm in get_permutations(number) if is_prime(perm)}
    if len(primes_permutations) >= 12:
        print(number, max(primes_permutations))
        found += 1


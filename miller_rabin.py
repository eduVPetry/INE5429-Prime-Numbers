# https://softwaredominos.com/home/software-engineering-and-computer-science/large-prime-number-generation-for-rsa-cryptography/

import random
 
def power(x, y, p):
    # This function calculates (x^y)%p in O(log y) time complexity
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res
 
def miller_rabin(n, k):
    # This function returns True if n is probably prime, False if composite
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
     
    # Find r and d such that n = 2^r * d + 1
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2
     
    # Do k rounds of Miller-Rabin tests
    for i in range(k):
        a = random.randint(2, n-2)
        x = power(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            x = power(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

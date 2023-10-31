from miller_rabin import miller_rabin
from linear_congruential_generator import lcg
from time import perf_counter


# Parameters for LCG taken from the book "Numerical Recipes"
# from the "quick and dirty generators" list, Chapter 7.1, Eq. 7.1.6
# parameters from Knuth and H. W. Lewis, as cited in Wikipedia
a = 1_664_525
c = 1_013_904_223
seed = 123_456_789

k = 10  # number of rounds of Miller-Rabin tests

for bit_length in (40, 56, 80, 128, 168, 224, 256, 512, 1_024, 2_048, 4_096):
    start_time = perf_counter()
    # create lcg
    modulus = 2 ** bit_length
    _lcg = lcg(modulus, a, c, seed)
    while True: # loop until probable prime is found
        n = next(_lcg)  # generate a random number of `bit_length` bits
        if n % 2 == 0:
            n += 1  # if n is even, make it odd 
        if miller_rabin(n, k):
            break
    end_time = perf_counter()
    total_time = end_time - start_time  # execution time in total (ns)
    print(f"Probable prime number of {bit_length} bits: {n}")
    print(f"Total execution time: {total_time:.3f} seconds", end="\n\n")

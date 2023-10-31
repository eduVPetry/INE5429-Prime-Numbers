from linear_congruential_generator import lcg
from time import perf_counter_ns


# Parameters for LCG taken from the book "Numerical Recipes"
# from the "quick and dirty generators" list, Chapter 7.1, Eq. 7.1.6
# parameters from Knuth and H. W. Lewis, as cited in Wikipedia
a = 1_664_525
c = 1_013_904_223
seed = 0

n = 100_000  # amount of numbers to be generated

for bit_length in (40, 56, 80, 128, 168, 224, 256, 512, 1_024, 2_048, 4_096):
    start_time = perf_counter_ns()
    # create lcg
    modulus = 2 ** bit_length
    _lcg = lcg(modulus, a, c, seed) 
    [next(_lcg) for _ in range(n)]  # generate 100_000 numbers of `bit_length` bits
    end_time = perf_counter_ns()
    total_time = end_time - start_time  # execution time in total (ns)
    average_time = total_time / n  # execution time per number generated (ns)
    print(f"LCG generated {n:,} pseudorandom numbers of {bit_length:,} bits.")
    print(f"Total execution time: {1e-6*total_time:.3f} milliseconds")
    print(f"Average execution time: {average_time} nanoseconds", end="\n\n")

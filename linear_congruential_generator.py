# https://en.wikipedia.org/wiki/Linear_congruential_generator

from typing import Generator, List


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

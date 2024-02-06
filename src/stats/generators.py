import time

from collections.abc import Iterator

__all__ = ['gcc_random_number', 'posix_random_number']

# System time in seconds (s)
SEED_1 = time.time()
# System time in milliseconds (ms)
SEED_2 = time.time() * 1000


def _lcg(mod: int, multiplier: int, increment: int, seed: float) -> Iterator[int]:
    """
    Linear Congruential Generator.

    :param mod: Modulus.
    :param multiplier: Multiplier.
    :param increment: Increment.
    :param seed: Seed.
    :return: Generator object that yields a pseudo-random number.
    """
    while True:
        seed = (multiplier * seed + increment) % mod
        yield seed


def gcc_random_number() -> float:
    """
    Generates a pseudorandom number using the parameters of the gcc. The gcc
    is a pseudorandom number generator that is used by the GNU C Library
    (glibc) and other C runtimes.
    """
    _lcg(mod=(2 ** 31) - 1, multiplier=1103515245, increment=12345, seed=SEED_1)
    return SEED_1 / (2 ** 31 - 1)


def posix_random_number() -> float:
    """
    Generates a pseudorandom number using the parameters of the POSIX standard.
    The POSIX standard is a family of standards specified by the IEEE Computer
    Society for maintaining compatibility between operating systems.
    """
    _lcg(mod=(2 ** 48) - 1, multiplier=25214903917, increment=11, seed=SEED_2)
    return SEED_2 / (2 ** 48 - 1)

# from decimal import Decimal
import math as mt
import numpy as np
from scipy import stats
import time


# ---- Random Variable bounds ----
MIN_VALUE = 0
MAX_VALUE = 0.8


# Tiempo del sistema en segundos (s), usado como
# semilla del primer generador
SEED_1 = time.time()

# Tiempo del sistema en milisegundos (ms) usado como
# semilla del segundo generador
SEED_2 = time.time()*1000


def cong_mixto_posix():
    """
    Congruential generator used by JAVA and POSIX
    """
    global SEED_1
    a = 25214903917
    m = (2**48) - 1
    SEED_1 = (a*SEED_1 + 11) % m
    return SEED_1/m


def cong_mixto_gcc():
    """
    Congruential generator used by gcc
    """
    global SEED_2
    a = 1103515245
    m = (2**31) - 1
    SEED_2 = (a*SEED_2 + 12345) % m
    return SEED_2/m


def var_checker(var):
    """
    Verify that the generated random variable is within the established range of values
    """
    if var < 0:
        return 0
    return var if var < 0.75 else 0.75


def bernoulli(args):
    """
    Generates a random variable that has a Bernoulli distribution with a probability of success 'p'
    """
    u = cong_mixto_posix()
    return 1 if u < args[0].value else 0


def beta(args):
    """
    Generates a random variable that has a Beta distribution according to the parameters sent
    """
    r_v = stats.beta.rvs(args[0], args[1], loc=args[2], scale=args[3])
    return var_checker(r_v)


def gamma(args):
    """
    Generates a random variable that has a Gamma distribution according to the parameters sent
    """
    r_v = stats.gamma.rvs(args[0], loc=args[2], scale=args[1])
    return var_checker(r_v)


def gumbel(args):
    """
    Generates a random variable that has a Gumbel distribution according to the parameters sent
    """
    r_v = np.random.gumbel(loc=args[0], scale=args[1])
    return var_checker(r_v)


def laplace(args):
    """
    Generates a random variable that has a Laplace distribution according to the parameters sent
    """
    r_v = stats.laplace.rvs(loc=args[0], scale=args[1])
    return var_checker(r_v)


def lognormal(args):
    """
    Generates a random variable that has a Lognorm distribution according to the parameters sent
    """
    r_v = stats.lognorm.rvs(args[1], loc=args[2], scale=mt.exp(args[0]))
    return var_checker(r_v)


def normal(args):
    """
    Generates a random variable that has a Norm distribution according to the parameters sent
    """
    r_v = stats.norm.rvs(loc=args[0], scale=args[1])
    return var_checker(r_v)


def rayleigh(args):
    """
    Generates a random variable that has a Rayleigh distribution according to the parameters sent
    """
    r_v = stats.rayleigh.rvs(loc=args[1], scale=args[0])
    return r_v


def uniform(args):
    """
    Generates a random variable that has a continuous Uniform distribution according to the parameters sent,
    using the inverse transformation algorithm
    """
    u = cong_mixto_posix()
    x = args[0] + (args[1]-args[0])*u
    print(x)
    return var_checker(x)


def weibull(args):
    """
    Generates a random variable that has a Uniform distribution according to the parameters sent
    """
    r_v = stats.weibull_min.rvs(c=args[0], loc=args[2], scale=args[1])
    return var_checker(r_v)

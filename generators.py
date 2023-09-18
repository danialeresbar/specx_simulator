import numpy as np 
from scipy import stats 
import math as mt
import time

# Tiempo del sistema en segundos (s), usado como semilla del primer generador
seed1 = time.time()
# Tiempo del sistema en milisegundos (ms) usado como semilla del segundo generador
seed2 = time.time()*1000

# Generador congruencial usado por JAVA y POSIX
def cong_mixto():
    global seed1
    a = 25214903917
    m = (2**48) - 1
    seed1 = (a*seed1 + 11) % m
    return seed1/m

# Generador congruencial usado por GCC
def cong_mixto():
    global seed2
    a = 1103515245
    m = (2**31) - 1
    seed2 = (a*seed2 + 12345) % m
    return seed2/m

def bounder(var):
    if var < 0:
        return 0

    elif var > 0.75:
        return 0.75

    else:
        return var

# Generador de VA con distribución Bernoulli
def bernoulli(args):
    U = cong_mixto()
    if U < args[0]:
        return 1
    return 0

# Generador de VA con distribución Gamma
def gamma(args):
    r_v = stats.gamma.rvs(args[0], loc=0, scale=args[1], size=1)    
    return r_v[0]

# Generador de VA con distribución Beta
def beta(args):
    r_v = stats.beta.rvs(args[0], args[1], loc=args[2], scale=args[3], size=1)
    return bounder(r_v[0])

# Generador de VA con distribución Gumbel
def gumbel_inverse_transformation(u, B):
    U = cong_mixto()
    X = u-(B*mt.log(-1*mt.log(1-U)))
    return X

# Generador de VA con distribución Gumbel
def gumbel(args):
    r_v = np.random.gumbel(loc=args[0], scale=args[1], size=1)
    var = r_v[0]
    return bounder(var)

# Generador de VA con distribución Laplace
def laplace(args):
    r_v = stats.laplace.rvs(loc=args[0], scale=args[1], size=1)
    #r_v = np.random.laplace(loc=u, scale=l, size=1)
    return bounder(r_v[0])

# Generador de VA con distribución Log-normal
def lognormal_3p(args):
    #r_v = np.random.lognormal(mean=u, sigma=o, size=1)
    r_v = stats.lognorm.rvs(s=args[1], loc=args[2], scale=mt.exp(args[0]), size=1)
    var = r_v[0]
    return bounder(var)

# Generador de VA con distribución Log-normal(3p)
def lognormal(args):
    r_v = np.random.lognormal(mean=args[0], sigma=args[1], size=1)
    var = r_v[0]
    return bounder(var)

# Generador de VA con distribución Normal
def normal_scheimen(args):
    U = cong_mixto()
    Z = (U**0.135 - (1-U)**0.135)/0.1975
    X = args[0] + Z*args[1]
    if X < 0:
        return 0
    return X

# Generador de VA con distribución Normal
def normal(args):
    r_v = np.random.normal(loc=args[0], scale=args[1], size=1)
    #r_v = stats.norm.rvs(loc=u, scale=o, size=1)
    var = r_v[0]
    return var
    #return bounder(var)

# Generador de VA con distribución Rayleigh
def rayleigh(args):
    if len(args) == 2:
        r_v = stats.rayleigh.rvs(loc=args[1], scale=args[0], size=1)

    else:
        r_v = stats.rayleigh.rvs(loc=0, scale=args[0], size=1)

    return r_v[0]

# Generador de VA con distribución Uniforme
def uniform_inverse_transformation(args):
    U = cong_mixto()
    X = args[0] + (args[1]-args[0])*U
    return X

# Generador de VA con distribución Uniforme
def uniform(args):
    r_v = np.random.uniform(low=args[0], high=args[1], size=1)
    return r_v[0]

# Generador de VA con distribución Weibull
def weibull_inverse_transformation(a, b, y):
    U = cong_mixto()
    X = b*(mt.pow(-1*mt.log(1-U), 1/a)) + y
    return X

# Generador de VA con distribución Weibull
def weibull(args):
    r_v = stats.weibull_min.rvs(c=args[0], loc=args[2], scale=args[1], size=1)
    var = r_v[0]
    return bounder(var)

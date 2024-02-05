from typing import Final, Set, Tuple

PDF_LONG: Final[str] = 'Probability Density Function'
PDF_SHORT: Final[str] = 'PDF'

########################### #
# PROBABILITY DISTRIBUTIONS #
########################### #
BERNOULLI: Final[str] = 'Bernoulli'
BETA: Final[str] = 'Beta'
GAMMA: Final[str] = 'Gamma'
GUMBEL: Final[str] = 'Gumbel'
LAPLACE: Final[str] = 'Laplace'
LOGNORMAL: Final[str] = 'LogNormal'
NORMAL: Final[str] = 'Normal'
RAYLEIGH: Final[str] = 'Rayleigh'
UNIFORM: Final[str] = 'Uniform'
WEIBULL: Final[str] = 'Weibull'
AVAILABLE_PROBABILITY_DISTRIBUTIONS: Final[Set[str]] = {
    BERNOULLI, BETA, GAMMA, GUMBEL, LAPLACE, LOGNORMAL, NORMAL, RAYLEIGH, UNIFORM, WEIBULL
}
CONTINUOUS_PROBABILITY_DISTRIBUTIONS: Final[Tuple[str, ...]] = (
    BETA, GAMMA, GUMBEL, LAPLACE, LOGNORMAL, NORMAL, RAYLEIGH, UNIFORM, WEIBULL
)
DISCRETE_PROBABILITY_DISTRIBUTIONS: Final[Tuple[str]] = (BERNOULLI,)

######################### #
# DISTRIBUTION ATTRIBUTES #
######################### #
DISTRIBUTION_DESCRIPTION_DEFAULT: Final[str] = 'No description available.'

######################### #
# DISTRIBUTION PARAMETERS #
######################### #
DISTRIBUTION_PARAMETER_NAME_MIN_LENGTH: Final[int] = 1
DISTRIBUTION_PARAMETER_NAME_MAX_LENGTH: Final[int] = 20

##### #
# PDF #
##### #
PDF_SAMPLE_SIZE: Final[int] = 1000
PPF_LOWER_BOUND: Final[float] = 0.001
PPF_UPPER_BOUND: Final[float] = 0.999

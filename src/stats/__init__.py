from constants.distributions import (
    BERNOULLI,
    BETA,
    GAMMA,
    GUMBEL,
    LAPLACE,
    LOGNORMAL,
    NORMAL,
    RAYLEIGH,
    UNIFORM,
    WEIBULL
)
from stats.probability_distributions import (
    BernoulliPMF,
    BetaPDF,
    GammaPDF,
    GumbelPDF,
    LaplacePDF,
    LogNormalPDF,
    NormalPDF,
    RayleighPDF,
    UniformPDF,
    WeibullPDF
)

AVAILABLE_PROBABILITY_DISTRIBUTIONS = {
    BERNOULLI: BernoulliPMF,
    BETA: BetaPDF,
    GAMMA: GammaPDF,
    GUMBEL: GumbelPDF,
    LAPLACE: LaplacePDF,
    LOGNORMAL: LogNormalPDF,
    NORMAL: NormalPDF,
    RAYLEIGH: RayleighPDF,
    UNIFORM: UniformPDF,
    WEIBULL: WeibullPDF
}

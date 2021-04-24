from src.model.distributions.continuous import beta, gamma, gumbel, laplace, lognorm, normal, rayleigh, uniform, weibull

DISTRIBUTIONS = {
    'Beta': beta.Beta,
    'Gamma': gamma.Gamma,
    'Gumbel': gumbel.Gumbel,
    'Laplace': laplace.Laplace,
    'Lognorm': lognorm.Lognorm,
    'Normal': normal.Normal,
    'Rayleigh': rayleigh.Rayleigh,
    'Uniform': uniform.Uniform,
    'Weibull': weibull.Weibull
}

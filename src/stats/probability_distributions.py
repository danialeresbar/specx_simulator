import math
import numpy as np

from numpy import ndarray
from scipy import stats as st

from constants.distributions import PDF_SAMPLE_SIZE, PPF_LOWER_BOUND, PPF_UPPER_BOUND
from constants.field_names import FAILURE_PROBABILITY_STR, SUCCESS_PROBABILITY_STR
from stats import generators
from stats.abc import PMF, PMFValueSet, PDF, PDFVectorPoints

__all__ = [
    'BernoulliPMF',
    'BetaPDF',
    'GammaPDF',
    'GumbelPDF',
    'LaplacePDF',
    'LogNormalPDF',
    'NormalPDF',
    'RayleighPDF',
    'UniformPDF',
    'WeibullPDF',
]


class BernoulliPMF(PMF):
    def __init__(self, p: float):
        self.success = p

    def rvs(self, size: int) -> ndarray:
        u: float = generators.posix_random_number()
        return np.array([1 if u < self.success else 0 for _ in range(size)])

    def get_value_set(self) -> PMFValueSet:
        x = np.array([SUCCESS_PROBABILITY_STR, FAILURE_PROBABILITY_STR])
        y = np.array([self.success, 1 - self.success])
        return x, y


class BetaPDF(PDF):
    def __init__(self, alpha: float, beta: float, loc: float = 0.05, scale: float = 1.0):
        self.alpha = alpha
        self.beta = beta
        self.location = loc
        self.scale = scale

    def rvs(self, size: int) -> ndarray:
        return st.beta.rvs(self.alpha, self.beta, loc=self.location, scale=self.scale, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.beta.ppf(PPF_LOWER_BOUND, self.alpha, self.beta),
            st.beta.ppf(PPF_UPPER_BOUND, self.alpha, self.beta),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.beta.pdf(x, self.alpha, self.beta)
        return x, y


class GammaPDF(PDF):
    def __init__(self, shape: float, scale: float):
        self.shape = shape
        self.scale = scale

    def rvs(self, size: int) -> ndarray:
        return st.gamma.rvs(self.shape, scale=self.scale, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.gamma.ppf(PPF_LOWER_BOUND, self.shape, scale=self.scale),
            st.gamma.ppf(PPF_UPPER_BOUND, self.shape, scale=self.scale),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.gamma.pdf(x, self.shape, scale=self.scale)
        return x, y


class GumbelPDF(PDF):
    def __init__(self, loc: float, scale: float):
        self.location = loc
        self.scale = scale

    def rvs(self, size: int) -> ndarray:
        return st.gumbel_r.rvs(loc=self.location, scale=self.scale, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.gumbel_r.ppf(PPF_LOWER_BOUND, loc=self.location, scale=self.scale),
            st.gumbel_r.ppf(PPF_UPPER_BOUND, loc=self.location, scale=self.scale),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.gumbel_r.pdf(x, loc=self.location, scale=self.scale)
        return x, y


class LaplacePDF(PDF):
    def __init__(self, mean: float, diversity: float):
        self.mean = mean
        self.diversity = diversity

    def rvs(self, size: int) -> ndarray:
        return st.laplace.rvs(loc=self.mean, scale=self.diversity, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.laplace.ppf(PPF_LOWER_BOUND, loc=self.mean, scale=self.diversity),
            st.laplace.ppf(PPF_UPPER_BOUND, loc=self.mean, scale=self.diversity),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.laplace.pdf(x, loc=self.mean, scale=self.diversity)
        return x, y


class LogNormalPDF(PDF):
    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std

    def rvs(self, size: int) -> ndarray:
        return st.lognorm.rvs(self.std, loc=self.mean, scale=math.exp(self.mean), size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.lognorm.ppf(PPF_LOWER_BOUND, self.std, loc=self.mean, scale=math.exp(self.mean)),
            st.lognorm.ppf(PPF_UPPER_BOUND, self.std, loc=self.mean, scale=math.exp(self.mean)),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.lognorm.pdf(x, self.std, loc=self.mean, scale=np.exp(self.mean))
        return x, y


class NormalPDF(PDF):
    def __init__(self, mean: float, std: float):
        self.mean = mean
        self.std = std

    def rvs(self, size: int) -> ndarray:
        return st.norm.rvs(loc=self.mean, scale=self.std, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.norm.ppf(PPF_LOWER_BOUND, loc=self.mean, scale=self.std),
            st.norm.ppf(PPF_UPPER_BOUND, loc=self.mean, scale=self.std),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.norm.pdf(x, loc=self.mean, scale=self.std)
        return x, y


class RayleighPDF(PDF):
    def __init__(self, scale: float):
        self.scale = scale

    def rvs(self, size: int) -> ndarray:
        return st.rayleigh.rvs(scale=self.scale, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.rayleigh.ppf(PPF_LOWER_BOUND, scale=self.scale),
            st.rayleigh.ppf(PPF_UPPER_BOUND, scale=self.scale),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.rayleigh.pdf(x, scale=self.scale)
        return x, y


class UniformPDF(PDF):
    def __init__(self, low: float, high: float):
        self.low = low
        self.high = high

    def rvs(self, size: int) -> ndarray:
        u: float = generators.gcc_random_number()
        return np.array([self.low + (self.high - self.low) * u for _ in range(size)])

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(self.low, self.high, PDF_SAMPLE_SIZE)
        y: ndarray = st.uniform.pdf(x, loc=self.low, scale=self.high - self.low)
        return x, y


class WeibullPDF(PDF):
    def __init__(self, shape: float, loc: float, scale: float):
        self.shape = shape
        self.location = loc
        self.scale = scale

    def rvs(self, size: int) -> ndarray:
        return st.weibull_min.rvs(self.shape, loc=self.location, scale=self.scale, size=size)

    def get_vector_points(self) -> PDFVectorPoints:
        x: ndarray = np.linspace(
            st.weibull_min.ppf(PPF_LOWER_BOUND, self.shape, loc=self.location, scale=self.scale),
            st.weibull_min.ppf(PPF_UPPER_BOUND, self.shape, loc=self.location, scale=self.scale),
            PDF_SAMPLE_SIZE
        )
        y: ndarray = st.weibull_min.pdf(x, self.shape, loc=self.location, scale=self.scale)
        return x, y

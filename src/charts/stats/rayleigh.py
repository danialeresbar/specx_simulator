import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts.stats import common

DEFAULT_LAMBDA_VALUE = 0
DEFAULT_SIGMA_VALUE = 1


class RayleighPDF(common.PDFChart):
    """

    """

    def __init__(self, **kwargs):
        self.__lambda = kwargs.get('location', DEFAULT_LAMBDA_VALUE)
        self.__sigma = kwargs.get('scale', DEFAULT_SIGMA_VALUE)
        super(RayleighPDF, self).__init__(
            title=kwargs.get('title')
        )

        self.base_series = QSplineSeries()
        self._plot()

    def _plot(self):
        x = np.linspace(
            st.rayleigh.ppf(0.01, loc=self.__lambda, scale=self.__sigma),
            st.rayleigh.ppf(0.99, loc=self.__lambda, scale=self.__sigma),
            common.SAMPLES
        )
        y = st.rayleigh.pdf(x, loc=self.__lambda, scale=self.__sigma)
        self.base_series.setName(f'{common.MU}={self.__mean:.4f}, {common.SIGMA}={self.__sigma:.4f}')
        self.switch_series(x, y)

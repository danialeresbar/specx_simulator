import math
import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts.stats import common

DEFAULT_GAMMA_VALUE = 1
DEFAULT_MEAN_VALUE = 0
DEFAULT_SIGMA_VALUE = 1


class LognormPDF(common.PDFChart):
    """

    """

    def __init__(self, **kwargs):
        self.__gamma = kwargs.get('gamma', DEFAULT_GAMMA_VALUE)
        self.__mean = kwargs.get('location', DEFAULT_MEAN_VALUE)
        self.__sigma = kwargs.get('scale', DEFAULT_SIGMA_VALUE)
        self.base_series = QSplineSeries()
        super(LognormPDF, self).__init__(
            title=kwargs.get('title')
        )

        self._plot()

    def _plot(self):
        x = np.linspace(
            st.lognorm.ppf(0.01, self.__sigma, loc=self.__gamma, scale=math.exp(self.__mean)),
            st.lognorm.ppf(0.99, self.__sigma, loc=self.__gamma, scale=math.exp(self.__mean)),
            common.SAMPLES
        )
        y = st.lognorm.pdf(x, self.__sigma, loc=self.__gamma, scale=math.exp(self.__mean))
        self.base_series.setName(
            f'{common.MU}={self.__mean:.4f}, {common.SIGMA}={self.__sigma:.4f}, {common.GAMMA}={self.__gamma:.4f}'
        )
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

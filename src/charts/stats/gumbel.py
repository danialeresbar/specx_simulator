import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts.stats import common

DEFAULT_MEAN_VALUE = 0
DEFAULT_SIGMA_VALUE = 1


class GumbelPDF(common.PDFChart):
    """

    """

    def __init__(self, **kwargs):
        self.__mean = kwargs.get('location', DEFAULT_MEAN_VALUE)
        self.__sigma = kwargs.get('scale', DEFAULT_SIGMA_VALUE)
        super(GumbelPDF, self).__init__(
            title=kwargs.get('title')
        )

        self.base_series = QSplineSeries()
        self._plot()

    def _plot(self):
        x = np.linspace(
            st.gumbel_r.ppf(0.01, loc=self.__mean, scale=self.__sigma),
            st.gumbel_r.ppf(0.99, loc=self.__mean, scale=self.__sigma),
            common.SAMPLES
        )
        y = st.gumbel_r.pdf(x, loc=self.__mean, scale=self.__sigma)
        self.base_series.setName(f'{common.MU}={self.__mean:.4f}, {common.SIGMA}={self.__sigma:.4f}')
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

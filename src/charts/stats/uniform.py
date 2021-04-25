import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts.stats import common

DEFAULT_LOWER_LIMIT_VALUE = 0
DEFAULT_UPPER_LIMIT_VALUE = 1


class UniformPDF(common.PDFChart):
    """

    """

    def __init__(self, **kwargs):
        self.__lower_limit = kwargs.get('lower', DEFAULT_LOWER_LIMIT_VALUE)
        self.__upper_limit = kwargs.get('upper', DEFAULT_UPPER_LIMIT_VALUE)
        self.base_series = QSplineSeries()
        super(UniformPDF, self).__init__(
            title=kwargs.get('title')
        )

        self._plot()

    def _plot(self):
        x = np.linspace(
            st.uniform.ppf(0.01, loc=self.__lower_limit, scale=self.__upper_limit-self.__lower_limit),
            st.uniform.ppf(0.99, loc=self.__lower_limit, scale=self.__upper_limit-self.__lower_limit),
            common.SAMPLES
        )
        y = st.uniform.pdf(x, loc=self.__lower_limit, scale=self.__upper_limit-self.__lower_limit)
        self.base_series.setName(f'a={self.__lower_limit:.4f}, b={self.__upper_limit:.4f}')
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

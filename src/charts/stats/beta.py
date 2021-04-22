import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts.stats import common

DEFAULT_ALPHA_VALUE = 0
DEFAULT_BETA_VALUE = 1
DEFAULT_A_VALUE = 0
DEFAULT_B_VALUE = 1


class BetaPDF(common.PDFChart):
    """

    """

    def __init__(self, **kwargs):
        self.__alpha = kwargs.get('alpha', DEFAULT_ALPHA_VALUE)
        self.__beta = kwargs.get('beta', DEFAULT_BETA_VALUE)
        self.__a = kwargs.get('a', DEFAULT_A_VALUE)
        self.__b = kwargs.get('b', DEFAULT_B_VALUE)
        super(BetaPDF, self).__init__(
            title=kwargs.get('title')
        )

        self.base_series = QSplineSeries()
        self._plot()

    def _plot(self):
        x = np.linspace(
            st.beta.ppf(0.01, self.__alpha, self.__beta, loc=self.__a, scale=self.__b),
            st.beta.ppf(0.99, self.__alpha, self.__beta, loc=self.__a, scale=self.__b),
            common.SAMPLES
        )
        y = st.beta.pdf(x, self.__alpha, self.__beta, loc=self.__a, scale=self.__b)
        self.base_series.setName(
            f'{common.ALPHA}={self.__alpha:.4f}, {common.BETA}={self.__beta:.4f}, a={self.__a:.4f}, b={self.__b:.4f}'
        )
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

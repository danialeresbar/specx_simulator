import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts.stats import common

DEFAULT_ALPHA_VALUE = 0
DEFAULT_GAMMA_VALUE = 1
DEFAULT_LAMBDA_VALUE = 0


class GammaPDF(common.PDFChart):
    """

    """

    def __init__(self, **kwargs):
        self.__alpha = kwargs.get('alpha', DEFAULT_ALPHA_VALUE)
        self.__gamma = kwargs.get('gamma', DEFAULT_GAMMA_VALUE)
        self.__lambda = kwargs.get('lambd', DEFAULT_LAMBDA_VALUE)
        self.base_series = QSplineSeries()
        super(GammaPDF, self).__init__(
            title=kwargs.get('title')
        )

        self._plot()

    def _plot(self):
        x = np.linspace(
            st.gamma.ppf(0.01, self.__alpha, loc=self.__gamma, scale=self.__lambda),
            st.gamma.ppf(0.99, self.__alpha, loc=self.__gamma, scale=self.__lambda),
            common.SAMPLES
        )
        y = st.gamma.pdf(x, self.__alpha, loc=self.__gamma, scale=self.__lambda)
        self.base_series.setName(
            f'{common.ALPHA}={self.__alpha:.4f}, {common.GAMMA}={self.__gamma:.4f}, {common.LAMBDA}={self.__lambda:.4f}'
        )
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

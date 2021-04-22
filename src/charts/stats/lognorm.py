import math
import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts import base

DEFAULT_GAMMA_VALUE = 1
DEFAULT_MEAN_VALUE = 0
DEFAULT_SIGMA_VALUE = 1


class LognormPDF(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        self.__gamma = kwargs.get('gamma', DEFAULT_GAMMA_VALUE)
        self.__mean = kwargs.get('location', DEFAULT_MEAN_VALUE)
        self.__sigma = kwargs.get('scale', DEFAULT_SIGMA_VALUE)
        super(LognormPDF, self).__init__(
            title=kwargs.get('title')
        )

        self.base_series = QSplineSeries()

        # Series style customization
        pen = self.base_series.pen()
        pen.setColor(base.SERIES_COLOR)
        pen.setWidth(base.CHART_DEFAULT_SERIES_WIDTH)

        self.addSeries(self.base_series)
        self.createDefaultAxes()

    def plot(self):
        x = np.linspace(
            st.lognorm.ppf(0.01, self.__sigma, loc=self.__gamma, scale=math.exp(self.__mean)),
            st.lognorm.ppf(0.99, self.__alpha, loc=self.__gamma, scale=math.exp(self.__mean)),
            base.SAMPLES
        )
        y = st.lognorm.pdf(x, self.__alpha, loc=self.__gamma, scale=math.exp(self.__mean))
        self.base_series.setName(
            f'{base.MU_LETTER}={self.__mean:.4f}, {base.SIGMA_LETTER}={self.__sigma:.4f}, {base.GAMMA_LETTER}={self.__gamma:.4f}'
        )
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts import base

DEFAULT_MEAN_VALUE = 0
DEFAULT_DIVERSITY_VALUE = 1


class LaplacePDF(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        self.__mean = kwargs.get('location', DEFAULT_MEAN_VALUE)
        self.__diversity = kwargs.get('diversity', DEFAULT_DIVERSITY_VALUE)
        super(LaplacePDF, self).__init__(
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
            st.laplace.ppf(0.01, loc=self.__mean, scale=self.__diversity),
            st.laplace.ppf(0.99, loc=self.__mean, scale=self.__diversity),
            base.SAMPLES
        )
        y = st.laplace.pdf(x, loc=self.__mean, scale=self.__diversity)
        self.base_series.setName(f'{base.MU_LETTER}={self.__mean:.4f}, b={self.__sigma:.4f}')
        self.switch_series(x, y)

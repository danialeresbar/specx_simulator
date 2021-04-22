import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts import base

DEFAULT_LAMBDA_VALUE = 0
DEFAULT_SIGMA_VALUE = 1


class RayleighPDF(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        self.__lambda = kwargs.get('location', DEFAULT_LAMBDA_VALUE)
        self.__sigma = kwargs.get('scale', DEFAULT_SIGMA_VALUE)
        super(RayleighPDF, self).__init__(
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
            st.rayleigh.ppf(0.01, loc=self.__lambda, scale=self.__sigma),
            st.rayleigh.ppf(0.99, loc=self.__lambda, scale=self.__sigma),
            base.SAMPLES
        )
        y = st.rayleigh.pdf(x, loc=self.__lambda, scale=self.__sigma)
        self.base_series.setName(f'{base.MU_LETTER}={self.__mean:.4f}, {base.SIGMA_LETTER}={self.__sigma:.4f}')
        self.switch_series(x, y)

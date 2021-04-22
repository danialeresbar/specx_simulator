import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QSplineSeries
from src.charts import base

DEFAULT_MEAN_VALUE = 0
DEFAULT_SIGMA_VALUE = 1


class NormalPDF(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        self.__mean = kwargs.get('location', DEFAULT_MEAN_VALUE)
        self.__sigma = kwargs.get('scale', DEFAULT_SIGMA_VALUE)
        super(NormalPDF, self).__init__(
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
            st.norm.ppf(0.01, loc=self.__mean, scale=self.__sigma),
            st.norm.ppf(0.99, loc=self.__mean, scale=self.__sigma),
            base.SAMPLES
        )
        y = st.norm.pdf(x, loc=self.__mean, scale=self.__sigma)
        self.base_series.setName(f'{base.MU_LETTER}={self.__mean:.4f}, {base.SIGMA_LETTER}={self.__sigma:.4f}')
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

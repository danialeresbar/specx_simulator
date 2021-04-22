import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QLegend, QSplineSeries
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

        # Axis settings
        self.addSeries(self.base_series)
        self.createDefaultAxes()
        self.x_axis = self.axes(base.Qt.Horizontal, self.series()[0])[0]
        self.y_axis = self.axes(base.Qt.Vertical, self.series()[0])[0]

        # Chart attributes
        self.legend().setVisible(True)
        self.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.setAnimationOptions(base.QChart.SeriesAnimations)
        self._plot()

    def _plot(self):
        x = np.linspace(
            st.rayleigh.ppf(0.01, loc=self.__lambda, scale=self.__sigma),
            st.rayleigh.ppf(0.99, loc=self.__lambda, scale=self.__sigma),
            base.SAMPLES
        )
        y = st.rayleigh.pdf(x, loc=self.__lambda, scale=self.__sigma)
        self.base_series.setName(f'{base.MU}={self.__mean:.4f}, {base.SIGMA}={self.__sigma:.4f}')
        self.switch_series(x, y)

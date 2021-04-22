import numpy as np
import scipy.stats as st

from PyQt5.QtChart import QLegend, QSplineSeries
from src.charts import base

DEFAULT_ALPHA_VALUE = 0
DEFAULT_BETA_VALUE = 0
DEFAULT_GAMMA_VALUE = 1


class WeibullPDF(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        self.__alpha = kwargs.get('alpha', DEFAULT_ALPHA_VALUE)
        self.__beta = kwargs.get('lambda', DEFAULT_BETA_VALUE)
        self.__gamma = kwargs.get('gamma', DEFAULT_GAMMA_VALUE)
        super(WeibullPDF, self).__init__(
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
            st.weibull_min.ppf(0.01, self.__alpha, loc=self.__gamma, scale=self.__beta),
            st.weibull_min.ppf(0.99, self.__alpha, loc=self.__gamma, scale=self.__beta),
            base.SAMPLES
        )
        y = st.weibull_min.pdf(x, self.__alpha, loc=self.__gamma, scale=self.__beta)
        self.base_series.setName(
            f'{base.ALPHA}={self.__alpha:.4f}, {base.GAMMA}={self.__gamma:.4f}, {base.BETA}={self.__beta:.4f}'
        )
        self.base_series.remove(0, len(self.base_series.pointsVector()))
        self.plot_series(x, y)

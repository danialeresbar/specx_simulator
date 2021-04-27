from PyQt5.QtChart import QLineSeries, QSplineSeries
from PyQt5.QtCore import Qt

from src.charts import base

DEFAULT_X_TICKCOUNT = 5
DEFAULT_Y_TICKCOUNT = 3

X_LOWER_LIMIT = 0
X_UPPER_LIMIT = 10
Y_LOWER_LIMIT = 0
Y_UPPER_LIMIT = 0.8


class PercentageBarChart(base.BaseBarChart):
    """

    """

    def __init__(self, **kwargs):
        super(PercentageBarChart, self).__init__(
            title=kwargs.get('title'),
            x_categories=kwargs.get('categories'),
            bars=kwargs.get('bars')
        )


class CurvedChart(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        super(CurvedChart, self).__init__(
            title=kwargs.get('title')
        )

        self.base_series = QSplineSeries()
        self.base_series.setPointsVisible(True)

        # Series style customization
        pen = self.base_series.pen()
        pen.setColor(base.SERIES_COLOR)
        pen.setWidth(base.CHART_DEFAULT_SERIES_WIDTH)

        # Axis settings
        self.addSeries(self.base_series)
        self.createDefaultAxes()
        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setRange(X_LOWER_LIMIT, X_UPPER_LIMIT)
        self.x_axis.setTickCount(DEFAULT_X_TICKCOUNT)
        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setRange(Y_LOWER_LIMIT, Y_UPPER_LIMIT)
        self.y_axis.setTickCount(DEFAULT_Y_TICKCOUNT)


class LinearChart(base.BaseChart):
    """

    """

    def __init__(self, **kwargs):
        super(LinearChart, self).__init__(
            title=kwargs.get('title')
        )

        self.base_series = QLineSeries()
        self.base_series.setPointsVisible(True)

        # Series style customization
        pen = self.base_series.pen()
        pen.setColor(base.SERIES_COLOR)
        pen.setWidth(base.CHART_DEFAULT_SERIES_WIDTH)

        # Axis settings
        self.addSeries(self.base_series)
        self.createDefaultAxes()
        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setRange(X_LOWER_LIMIT, X_UPPER_LIMIT)
        self.x_axis.setTickCount(DEFAULT_X_TICKCOUNT)
        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setRange(Y_LOWER_LIMIT, Y_UPPER_LIMIT)
        self.y_axis.setTickCount(DEFAULT_Y_TICKCOUNT)

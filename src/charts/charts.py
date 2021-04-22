import numpy as np
import scipy.stats as stats

from PyQt5.QtChart import (
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QChart,
    QLegend,
    QLineSeries,
    QSplineSeries,
    QValueAxis
)
from PyQt5.QtCore import Qt, QMargins, QPointF
from PyQt5.QtGui import QColor, QColorConstants, QFont


class SplineChart(BaseChart):
    """

    """

    def __init__(self, **kwargs):
        super(SplineChart, self).__init__(
            title=kwargs.get('title', CHART_DEFAULT_TITLE)
        )

        self.base_series = QSplineSeries()
        self.base_series.setPointsVisible(True)
        self.set_customize_pen()
        self.addSeries(self.base_series)
        self.setup_axes()

        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setRange(0, 10)
        self.x_axis.setTickCount(5)

        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setRange(0, 0.8)
        self.y_axis.setTickCount(3)


class LineChart(BaseChart):
    """

    """

    def __init__(self, **kwargs):
        super(LineChart, self).__init__(
            title=kwargs.get('title', CHART_DEFAULT_TITLE)
        )

        self.base_series = QLineSeries()
        self.base_series.setPointsVisible(True)
        self._set_customize_pen()
        self.addSeries(self.base_series)
        self.setup_axes()

        self.x_axis = self.axes(Qt.Horizontal, self.series()[0])[0]
        self.x_axis.setRange(0, 10)
        self.x_axis.setTickCount(5)

        self.y_axis = self.axes(Qt.Vertical, self.series()[0])[0]
        self.y_axis.setRange(0, 0.8)
        self.y_axis.setTickCount(3)
